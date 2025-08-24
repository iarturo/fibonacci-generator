# 🤝 Contributing to Fibonacci Generator

Thank you for considering contributing to the Fibonacci Generator! This guide will help you get started.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## 📜 Code of Conduct

This project follows a simple code of conduct:
- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Focus on what is best for the community

## 🛠️ How Can I Contribute?

### 🐛 Reporting Bugs
- Use the GitHub issue tracker
- Include your OS, Python version, and detailed steps to reproduce
- Add screenshots if applicable

### 💡 Suggesting Features
- Check if the feature has already been suggested
- Explain the use case and benefits
- Be open to discussion and alternatives

### 🔧 Code Contributions
- Bug fixes
- Feature implementations
- Performance improvements
- Documentation updates
- UI/UX enhancements

### 📖 Documentation
- Fix typos or unclear explanations
- Add examples or tutorials
- Improve README or code comments

## 🏗️ Development Setup

1. **Fork the repository**
   - Click "Fork" on the GitHub page
   - Clone your fork locally

2. **Set up your environment**
   ```bash
   git clone https://github.com/yourusername/fibonacci-generator.git
   cd fibonacci-generator
   ```

3. **Create a branch for your work**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

4. **Test your changes**
   - Test with small numbers (1-100)
   - Test with medium numbers (1,000-10,000)
   - Test both light and dark modes
   - Test fullscreen functionality
   - Test the stop button with long calculations

## 📝 Coding Guidelines

### Python Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and reasonably sized

### Comments
- Explain complex algorithms or logic
- Use inline comments sparingly
- Update comments when changing code

### Threading
- Be careful with thread safety
- Use the existing queue system for UI updates
- Test thoroughly with different scenarios

### UI/UX
- Maintain consistency with existing design
- Ensure features work in both light and dark mode
- Test responsiveness with different window sizes

## 🔄 Pull Request Process

1. **Before submitting:**
   - Test your changes thoroughly
   - Update documentation if needed
   - Make sure your code follows the style guidelines
   - Write clear commit messages

2. **Creating the PR:**
   - Use a descriptive title
   - Explain what changes you made and why
   - Reference any related issues
   - Add screenshots for UI changes

3. **After submitting:**
   - Respond to feedback promptly
   - Make requested changes
   - Keep the discussion constructive

## 🐛 Reporting Issues

### Bug Reports
Include this information:
- **Description**: Clear description of the problem
- **Steps to reproduce**: Numbered steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens  
- **Environment**: OS, Python version, hardware specs
- **Screenshots**: If applicable

### Feature Requests
Include this information:
- **Problem**: What problem does this solve?
- **Solution**: Describe your proposed solution
- **Alternatives**: Any alternative solutions considered
- **Additional context**: Screenshots, examples, etc.

## 💡 Ideas for Contributions

### Easy (Good for beginners)
- Fix typos in documentation
- Add input validation improvements
- Improve error messages
- Add keyboard shortcuts
- Enhance the UI with better spacing or colors

### Medium
- Add export functionality (save results to file)
- Implement different Fibonacci variations
- Add more themes
- Improve performance for large numbers
- Add unit tests

### Advanced
- Implement matrix exponentiation for faster calculation
- Add visualization (graphs/charts)
- Create a web version
- Add mathematical analysis features
- Implement distributed computing for very large numbers

## 🏷️ Labels We Use

- `bug`: Something isn't working
- `enhancement`: New feature or improvement
- `good first issue`: Good for newcomers
- `help wanted`: We need help with this
- `documentation`: Related to docs
- `performance`: Performance related
- `ui/ux`: User interface/experience

## 🎉 Recognition

Contributors will be:
- Listed in the project contributors
- Mentioned in release notes for significant contributions
- Given credit in the documentation

## ❓ Questions?

If you have questions about contributing:
- Open a discussion on GitHub
- Create an issue with the "question" label
- Check existing issues and discussions

---

**Happy coding! 🚀**