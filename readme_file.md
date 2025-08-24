# 🔢 Fibonacci Generator

A powerful, multithreaded Fibonacci number generator built with Python and Tkinter. Generate sequences up to 100,000 numbers or find specific Fibonacci numbers up to position 1,000,000 instantly!

## ✨ Features

- 🚀 **Fast Generation**: Multithreaded calculation for responsive UI
- 🔍 **Individual Number Lookup**: Find specific Fibonacci numbers instantly
- 🌙 **Dark/Light Mode**: Toggle between themes
- ⛶ **Fullscreen Support**: Resize or go fullscreen (F11)
- 📊 **Progress Tracking**: Real-time progress bar and status updates
- ⏹️ **Cancellable Operations**: Stop long calculations anytime
- 🛡️ **Input Validation**: Only accepts valid numbers
- 📈 **Smart Warnings**: Estimates calculation time for large numbers

## 🖥️ System Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- Minimum 4GB RAM (8GB+ recommended for large sequences)

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/fibonacci-generator.git
cd fibonacci-generator
```

2. **Run the application:**
```bash
python fibonacci_app.py
```

That's it! No additional dependencies required.

## 📝 Usage

### Generate Fibonacci Sequence
1. Enter the quantity of numbers you want (1-100,000)
2. Click "🚀 Generate"
3. Watch the real-time progress and results

### Find Specific Fibonacci Number
1. Enter the position you want to find (1-1,000,000)
2. Click "🔍 Find"
3. Get the result instantly with digit count

### Keyboard Shortcuts
- **F11**: Toggle fullscreen
- **Escape**: Exit fullscreen

## 🎨 Themes

Switch between Light and Dark modes using the theme toggle button in the top-right corner.

## 📊 Performance

| Numbers Generated | Estimated Time | RAM Usage |
|------------------|----------------|-----------|
| 1,000           | Few seconds    | <100MB    |
| 10,000          | 10-30 seconds  | ~500MB    |
| 50,000          | 1-3 minutes    | ~2GB      |
| 100,000         | 5-8 minutes    | ~5GB      |

## 🛠️ Technical Details

- **Algorithm**: Linear iteration O(n) for sequences
- **Architecture**: Producer-consumer pattern with threading
- **UI Framework**: Python Tkinter
- **Memory Management**: Batch processing for large datasets

## 🤝 Contributing

We welcome contributions! Here are ways you can help:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📖 Improve documentation

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Add comments for complex logic
- Test with both small and large numbers

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/fibonacci-generator/issues) page
2. Create a new issue with detailed information
3. Include your OS, Python version, and steps to reproduce

## 🌟 Acknowledgments

- Built with Python's powerful threading capabilities
- Inspired by the mathematical beauty of Fibonacci sequences
- Thanks to all contributors who help improve this project

## 📸 Screenshots

### Light Mode
*Coming soon - add screenshots of your app*

### Dark Mode  
*Coming soon - add screenshots of your app*

---

⭐ **Star this repository if you found it useful!** ⭐