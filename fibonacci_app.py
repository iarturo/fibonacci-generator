import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
import sys

# Increase the limit for large Fibonacci numbers
sys.set_int_max_str_digits(0)  # Remove limit for integer string conversion

class FibonacciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Generator")
        self.root.geometry("500x450")
        self.root.resizable(True, True)  # Enable window resizing
        self.root.minsize(450, 400)  # Set minimum size
        
        # Fullscreen state
        self.is_fullscreen = False
        
        # Dark mode state
        self.is_dark_mode = False
        
        # Threading control
        self.calculation_thread = None
        self.stop_calculation = False
        self.result_queue = queue.Queue()
        
        # Configure styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TEntry", font=("Arial", 12))
        
        # Create header frame for dark mode toggle
        self.header_frame = ttk.Frame(root)
        self.header_frame.pack(fill=tk.X, padx=20, pady=(10, 0))
        
        # Dark mode toggle button (positioned on the right)
        self.dark_mode_button = ttk.Button(self.header_frame, text="🌙 Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.pack(side=tk.RIGHT)
        
        # Fullscreen toggle button (positioned on the right, before dark mode)
        self.fullscreen_button = ttk.Button(self.header_frame, text="⛶ Fullscreen", command=self.toggle_fullscreen)
        self.fullscreen_button.pack(side=tk.RIGHT, padx=(0, 5))
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create input elements
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.quantity_label = ttk.Label(self.input_frame, text="Quantity of Numbers:")
        self.quantity_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.quantity_var = tk.StringVar()
        
        # Register validation function
        vcmd = (self.root.register(self.validate_number_input), '%P')
        
        self.quantity_entry = ttk.Entry(self.input_frame, width=10, textvariable=self.quantity_var, 
                                      validate='key', validatecommand=vcmd)
        self.quantity_entry.pack(side=tk.LEFT)
        self.quantity_entry.bind('<KeyRelease>', self.on_quantity_change)
        
        self.run_button = ttk.Button(self.input_frame, text="🚀 Generate", command=self.generate_fibonacci)
        self.run_button.pack(side=tk.LEFT, padx=(10, 0))
        
        self.stop_button = ttk.Button(self.input_frame, text="⏹️ Stop", command=self.stop_generation, state="disabled")
        self.stop_button.pack(side=tk.LEFT, padx=(5, 0))
        
        # Create Fibonacci number lookup section
        self.fibonacci_frame = ttk.Frame(self.main_frame)
        self.fibonacci_frame.pack(fill=tk.X, pady=(10, 10))
        
        self.fibonacci_label = ttk.Label(self.fibonacci_frame, text="Fibonacci Number:")
        self.fibonacci_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.fibonacci_var = tk.StringVar()
        self.fibonacci_entry = ttk.Entry(self.fibonacci_frame, width=10, textvariable=self.fibonacci_var,
                                       validate='key', validatecommand=vcmd)
        self.fibonacci_entry.pack(side=tk.LEFT)
        self.fibonacci_entry.bind('<KeyRelease>', self.on_fibonacci_change)
        
        self.find_button = ttk.Button(self.fibonacci_frame, text="🔍 Find", command=self.find_fibonacci_number)
        self.find_button.pack(side=tk.LEFT, padx=(10, 0))
        
        # Progress bar and info
        self.progress_frame = ttk.Frame(self.main_frame)
        self.progress_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=(0, 5))
        
        self.status_label = ttk.Label(self.progress_frame, text="Ready to generate Fibonacci numbers")
        self.status_label.pack()
        
        # Create output area
        self.output_frame = ttk.Frame(self.main_frame)
        self.output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_label = ttk.Label(self.output_frame, text="Fibonacci Numbers will appear here")
        self.output_label.pack(pady=10)
        
        # Create frame for text widget and scrollbar
        self.text_frame = ttk.Frame(self.output_frame)
        self.text_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create text widget
        self.result_text = tk.Text(self.text_frame, height=12, width=50, wrap=tk.WORD, state="disabled")
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create and configure scrollbar
        self.scrollbar = ttk.Scrollbar(self.text_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure text widget to work with scrollbar
        self.result_text.configure(yscrollcommand=self.scrollbar.set)
        
        # Apply initial light theme after all widgets are created
        self.configure_light_theme()
        
        # Bind keyboard shortcuts
        self.root.bind('<F11>', lambda e: self.toggle_fullscreen())
        self.root.bind('<Escape>', lambda e: self.exit_fullscreen() if self.is_fullscreen else None)
        
        # Start queue processing
        self.process_queue()
        
    def validate_number_input(self, value):
        """Validate that input contains only numbers"""
        if value == "":  # Allow empty string
            return True
        try:
            int(value)  # Try to convert to integer
            return True
        except ValueError:
            return False  # Reject if not a valid number
    
    def on_quantity_change(self, event):
        """Handle changes in quantity field"""
        if self.quantity_var.get().strip():
            # Disable fibonacci entry when quantity has content
            self.fibonacci_entry.config(state="disabled")
            self.find_button.config(state="disabled")
        else:
            # Enable fibonacci entry when quantity is empty
            self.fibonacci_entry.config(state="normal")
            self.find_button.config(state="normal")
    
    def on_fibonacci_change(self, event):
        """Handle changes in fibonacci field"""
        if self.fibonacci_var.get().strip():
            # Disable quantity entry when fibonacci has content
            self.quantity_entry.config(state="disabled")
            self.run_button.config(state="disabled")
        else:
            # Enable quantity entry when fibonacci is empty
            self.quantity_entry.config(state="normal")
            self.run_button.config(state="normal")
    
    def find_fibonacci_number(self):
        """Find a specific Fibonacci number"""
        try:
            position = int(self.fibonacci_var.get())
            if position <= 0:
                messagebox.showerror("Invalid Input", "Please enter a positive number")
                return
            
            # Limit for single number calculation
            if position > 1000000:
                messagebox.showerror("Number Too Large", 
                    "The position must be 1,000,000 or less for single number lookup.")
                return
            
            # Show calculating status
            self.status_label.config(text=f"Calculating Fibonacci number at position {position:,}...")
            self.progress_bar.config(mode='indeterminate')
            self.progress_bar.start()
            
            # Calculate in thread to avoid freezing
            self.calculation_thread = threading.Thread(target=self.fibonacci_single_worker, args=(position,))
            self.calculation_thread.daemon = True
            self.calculation_thread.start()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def fibonacci_single_worker(self, position):
        """Calculate a single Fibonacci number in a separate thread"""
        try:
            # Calculate the specific Fibonacci number (1-indexed: F(1)=1, F(2)=1, F(3)=2, ...)
            if position == 1 or position == 2:
                result = 1
            else:
                a, b = 1, 1
                for _ in range(position - 2):
                    a, b = b, a + b
                result = b
            
            # Send result
            self.result_queue.put(("single_result", (position, result)))
            
        except Exception as e:
            self.result_queue.put(("error", f"Error calculating Fibonacci number: {str(e)}"))
        
    def generate_fibonacci(self):
        try:
            quantity = int(self.quantity_var.get())
            if quantity <= 0:
                messagebox.showerror("Invalid Input", "Please enter a positive number")
                return
            
            # Hard limit for hardware protection
            if quantity > 100000:
                messagebox.showerror("Number Too Large", 
                    "The input number must be 100,000 or less.\n"
                    "Larger numbers would consume too much memory and time.")
                return
            
            # Warning for medium-large numbers (20k - 100k)
            if quantity > 20000:
                result = messagebox.askyesno("Large Number Warning", 
                    f"Generating {quantity:,} numbers will take some time and memory.\n"
                    f"Estimated time: {self.estimate_time(quantity)}\n"
                    "Are you sure you want to continue?")
                if not result:
                    return
                    
            # Reset stop flag and clear previous results
            self.stop_calculation = False
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            self.result_text.config(state="disabled")
            
            # Update UI state
            self.run_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.progress_bar.config(maximum=quantity, value=0)
            self.status_label.config(text="Generating Fibonacci numbers...")
            
            # Start calculation in separate thread
            self.calculation_thread = threading.Thread(target=self.fibonacci_worker, args=(quantity,))
            self.calculation_thread.daemon = True
            self.calculation_thread.start()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def fibonacci_worker(self, n):
        """Generate Fibonacci numbers in a separate thread"""
        try:
            # Send initial message
            self.result_queue.put(("start", "Fibonacci Sequence:\n\n"))
            
            a, b = 0, 1
            batch_size = 100  # Process in batches for better responsiveness
            batch_results = []
            
            for i in range(n):
                if self.stop_calculation:
                    self.result_queue.put(("stopped", "Generation stopped by user."))
                    return
                
                # Add current number to batch
                batch_results.append(f"{i+1}. {a}\n")
                
                # Calculate next Fibonacci number
                a, b = b, a + b
                
                # Send batch when full or at the end
                if len(batch_results) >= batch_size or i == n - 1:
                    self.result_queue.put(("batch", "".join(batch_results)))
                    batch_results = []
                    
                # Update progress
                self.result_queue.put(("progress", i + 1))
            
            # Send completion message
            self.result_queue.put(("complete", f"\nGeneration complete! Generated {n} Fibonacci numbers."))
            
        except Exception as e:
            self.result_queue.put(("error", f"Error during generation: {str(e)}"))
    
    def stop_generation(self):
        """Stop the current Fibonacci generation"""
        self.stop_calculation = True
        self.stop_button.config(state="disabled")
        self.status_label.config(text="Stopping generation...")
    
    def process_queue(self):
        """Process messages from the worker thread"""
        try:
            while True:
                message_type, data = self.result_queue.get_nowait()
                
                if message_type == "start":
                    self.result_text.config(state="normal")
                    self.result_text.insert(tk.END, data)
                    self.result_text.config(state="disabled")
                    
                elif message_type == "batch":
                    self.result_text.config(state="normal")
                    self.result_text.insert(tk.END, data)
                    self.result_text.see(tk.END)  # Auto-scroll to bottom
                    self.result_text.config(state="disabled")
                    
                elif message_type == "progress":
                    self.progress_bar.config(value=data)
                    self.status_label.config(text=f"Generated {data} numbers...")
                    
                elif message_type in ["complete", "stopped", "error"]:
                    self.result_text.config(state="normal")
                    self.result_text.insert(tk.END, data)
                    self.result_text.config(state="disabled")
                    
                    # Reset UI state
                    self.run_button.config(state="normal")
                    self.stop_button.config(state="disabled")
                    self.status_label.config(text="Ready to generate Fibonacci numbers")
                    
                elif message_type == "single_result":
                    position, result = data
                    
                    # Display single result
                    self.result_text.config(state="normal")
                    self.result_text.delete(1.0, tk.END)
                    
                    # Format large numbers with digit count
                    result_str = str(result)
                    digit_count = len(result_str)
                    
                    output_text = f"Fibonacci Number Lookup:\n\n"
                    output_text += f"Position: {position:,}\n"
                    output_text += f"Number of digits: {digit_count:,}\n\n"
                    output_text += f"Result:\n{result_str}"
                    
                    self.result_text.insert(tk.END, output_text)
                    self.result_text.config(state="disabled")
                    
                    # Reset progress bar and status
                    self.progress_bar.stop()
                    self.progress_bar.config(mode='determinate')
                    self.status_label.config(text="Fibonacci number found successfully!")
                    
        except queue.Empty:
            pass
        
        # Schedule next queue check
        self.root.after(50, self.process_queue)
    
    def estimate_time(self, n):
        """Estimate generation time based on quantity"""
        if n <= 5000:
            return "a few seconds"
        elif n <= 20000:
            return "10-30 seconds"
        elif n <= 50000:
            return "1-3 minutes"
        elif n <= 80000:
            return "3-5 minutes"
        else:
            return "5-8 minutes"
    
    def configure_light_theme(self):
        """Configure light theme colors"""
        # Configure ttk styles for light theme
        self.style.configure("TButton", font=("Arial", 10), foreground="black", background="white")
        self.style.configure("TLabel", font=("Arial", 12), foreground="black", background="white")
        self.style.configure("TEntry", font=("Arial", 12), foreground="black", fieldbackground="white")
        self.style.configure("TFrame", background="white")
        
        # Configure root and text widget
        self.root.configure(bg="white")
        self.result_text.configure(bg="white", fg="black", insertbackground="black")
    
    def configure_dark_theme(self):
        """Configure dark theme colors"""
        # Configure ttk styles for dark theme - TEXTO SIEMPRE NEGRO
        self.style.configure("TButton", font=("Arial", 10), foreground="black", background="#c0c0c0")
        self.style.configure("TLabel", font=("Arial", 12), foreground="white", background="#2d2d2d")
        self.style.configure("TEntry", font=("Arial", 12), foreground="black", fieldbackground="white")
        self.style.configure("TFrame", background="#2d2d2d")
        
        # Configure root and text widget
        self.root.configure(bg="#2d2d2d")
        self.result_text.configure(bg="#2d2d2d", fg="white", insertbackground="white")
    
    def toggle_dark_mode(self):
        """Toggle between light and dark mode"""
        self.is_dark_mode = not self.is_dark_mode
        
        if self.is_dark_mode:
            self.configure_dark_theme()
            self.dark_mode_button.configure(text="☀️ Light Mode")
        else:
            self.configure_light_theme()
            self.dark_mode_button.configure(text="🌙 Dark Mode")
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        self.is_fullscreen = not self.is_fullscreen
        
        if self.is_fullscreen:
            self.root.attributes('-fullscreen', True)
            self.fullscreen_button.configure(text="⛶ Exit Fullscreen")
        else:
            self.root.attributes('-fullscreen', False)
            self.fullscreen_button.configure(text="⛶ Fullscreen")
    
    def exit_fullscreen(self):
        """Exit fullscreen mode"""
        if self.is_fullscreen:
            self.is_fullscreen = False
            self.root.attributes('-fullscreen', False)
            self.fullscreen_button.configure(text="⛶ Fullscreen")

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()