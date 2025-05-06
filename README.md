# Caesar's Cipher 🔐

Welcome to **Caesar's Cipher**, a Python-based encryption tool that transforms your plain text into secure, jumbled code! 🕵️‍♀️✨

## 🔍 What It Does

This program takes any paragraph you type and encrypts it using two values:
- `k_value`: Shifts each letter by a certain number of places (classic Caesar style).
- `m_value`: Multiplies the numeric value of each character before shifting — adding an extra layer of confusion for codebreakers.

Punctuation and symbols like `?`, `!`, etc. are **not encrypted**, but they still appear correctly in the final output!

## 🛠️ Installation

No installation needed! This runs on any Python editor or IDE.

**Requirements:**
- Python 3.x  
(No additional libraries are needed.)

## 🚀 How to Use

1. Open your terminal or editor of choice (VS Code, PyCharm, Replit, etc.).
2. Run the Python file:
   ```bash
   python caesars_cipher.py
   ```
3. Type in your paragraph when prompted.
4. Enter a `k_value` (an integer shift amount).
5. Enter an `m_value` (an integer multiplier to scramble things up).

Sit back and watch your text transform into a secret message! 💬➡️🧠➡️🗝️

## 💡 Example

```text
Enter your message: I love sandwiches!
Enter a k_value: 5
Enter an m_value: 3

Encrypted message: X jqjt qydzoamtrp!
```

## 🌟 Features

- Accepts letters, punctuation, and symbols.
- Adds a multiplier to classic Caesar Cipher for extra strength.
- Runs in any Python environment.
- Great for beginner cryptography practice.

## 🤝 Contributing

Pull requests are welcome! If you have ideas for improvements (like adding decryption or making it GUI-based), go for it!
