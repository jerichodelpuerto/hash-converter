# Project: Hash Converter

A simple command-line utility to generate a comprehensive set of hashes for any given text string. This script dynamically uses all algorithms from Python's `hashlib.algorithms_guaranteed` (MD5, SHA-1, SHA-256, SHA-3, BLAKE2, SHAKE, etc.).

---

## Features

* **Comprehensive:** Generates a complete list of all hashes guaranteed to be available in the `hashlib` module.
* **Smart Handling:** Automatically detects and correctly handles eXtensible-Output Functions (XOFs) like `shake_128` and `shake_256` by providing a default output length.
* **Simple Interface:** Runs interactively from the command line.
* **Lightweight:** A single script with no external dependencies (uses only built-in `hashlib` and `sys` modules).

---

## Requirements

* Python 3.x

---

## ⚙️ Installation

No installation is required. Simply save the script as `hash_converter.py`.

---

## 🚀 Usage

Run the script from your terminal using `python` or `python3`:

```bash
python hash_converter.py