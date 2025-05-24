# 🔄 XPubKaleidoscope
A Python utility for converting Bitcoin Extended Public Keys between different formats (xpub, ypub, zpub, tpub, etc.).

## 📝 Overview
XPubKaleidoscope allows you to easily convert Bitcoin extended public keys between various formats. This is particularly useful when working with different wallet types and Bitcoin address formats.

### ✨ Supported formats:

#### 🌐 Mainnet Single-Signature
- `xpub` - Legacy Bitcoin addresses (P2PKH or P2SH) - Path: m/44'/0'
- `ypub` - SegWit addresses (P2WPKH in P2SH) - Path: m/49'/0'
- `zpub` - Native SegWit addresses (P2WPKH) - Path: m/84'/0'

#### 🌐 Mainnet Multi-Signature
- `Ypub` - Multi-signature P2WSH in P2SH
- `Zpub` - Multi-signature P2WSH

#### 🧪 Testnet Single-Signature
- `tpub` - Legacy Bitcoin addresses (P2PKH or P2SH) - Path: m/44'/1'
- `upub` - SegWit addresses (P2WPKH in P2SH) - Path: m/49'/1'
- `vpub` - Native SegWit addresses (P2WPKH) - Path: m/84'/1'

#### 🧪 Testnet Multi-Signature
- `Upub` - Multi-signature P2WSH in P2SH
- `Vpub` - Multi-signature P2WSH

## 🚀 Setup

### 📋 Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/XPubKaleidoscope.git
cd XPubKaleidoscope
```

2. Set up a virtual environment:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

To deactivate the virtual environment when you're done:
```bash
deactivate
```

## 🛠️ Usage

### 🖥️ Command Line Interface

#### Identify format:
```bash
python xpub_converter.py "your_xpub_key_here" -i
```
Output example:
```
📥 Input key:
xpub:
  🌐 Network: MAINNET
  📦 Type: P2PKH or P2SH
  🔗 Derivation Path: m/44'/0'
  🔑 Key: xpub6CUGRUo...
```

#### Convert to specific format:
```bash
python xpub_converter.py "your_xpub_key_here" -t zpub
```
Output example:
```
📥 Input key:
xpub:
  🌐 Network: MAINNET
  📦 Type: P2PKH or P2SH
  🔗 Derivation Path: m/44'/0'
  🔑 Key: xpub6CUGRUo...

📤 Converted key:
zpub:
  🌐 Network: MAINNET
  📦 Type: P2WPKH
  🔗 Derivation Path: m/84'/0'
  🔑 Key: zpub6rFR7y4...
```

#### Convert to all supported formats:
```bash
python xpub_converter.py "your_xpub_key_here" -a
```

#### Show help:
```bash
python xpub_converter.py -h
```

## ✨ Features
- 🔄 Convert between all major extended public key formats
- ✅ Validation of input keys
- 🌐 Support for both mainnet and testnet
- 💻 Simple command-line interface with colored output
- 🔌 Support for single-signature and multi-signature formats

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer
Always verify the output addresses before using them for real transactions. Incorrect conversions could lead to loss of funds.