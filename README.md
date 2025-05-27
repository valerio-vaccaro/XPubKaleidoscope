# 🔄 XPubKaleidoscope
A Python utility for converting Bitcoin Extended Public Keys between different formats (xpub, ypub, zpub, tpub, etc.).

## 📝 Overview
XPubKaleidoscope allows you to easily convert Bitcoin extended public keys between various formats. This is particularly useful when working with different wallet types and Bitcoin address formats. Each key's fingerprint is calculated and displayed to help verify key integrity across conversions.

### ✨ Supported formats:

#### 🌐 Mainnet Single-Signature
- `xpub` - Legacy Bitcoin addresses (P2PKH or P2SH) - Path: m/44'/0'/0'
- `ypub` - SegWit addresses (P2WPKH in P2SH) - Path: m/49'/0'/0'
- `zpub` - Native SegWit addresses (P2WPKH) - Path: m/84'/0'/0'

#### 🌐 Mainnet Multi-Signature
- `Ypub` - Multi-signature P2WSH in P2SH - Path: Custom
- `Zpub` - Multi-signature P2WSH - Path: Custom

#### 🧪 Testnet Single-Signature
- `tpub` - Legacy Bitcoin addresses (P2PKH or P2SH) - Path: m/44'/1'/0'
- `upub` - SegWit addresses (P2WPKH in P2SH) - Path: m/49'/1'/0'
- `vpub` - Native SegWit addresses (P2WPKH) - Path: m/84'/1'/0'

#### 🧪 Testnet Multi-Signature
- `Upub` - Multi-signature P2WSH in P2SH - Path: Custom
- `Vpub` - Multi-signature P2WSH - Path: Custom

## 🚀 Setup & Installation

### 📦 Using pip (Recommended)
```bash
pip install xpubkaleidoscope
```

### 🛠️ From Source
1. Clone the repository:
```bash
git clone https://github.com/valerio-vaccaro/XPubKaleidoscope.git
cd XPubKaleidoscope
```

2. Set up a virtual environment:
```bash
python3 -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

pip install -r requirements.txt
```

To deactivate the virtual environment when you're done:
```bash
deactivate
```

## 🛠️ Usage

### 📚 As a Python Package
```python
from xpubkaleidoscope import XPubConverter

# Initialize converter
converter = XPubConverter()

# Convert xpub to different format
result = converter.convert("your_xpub_key_here", target_format="zpub")

# Get key information
info = converter.identify("your_xpub_key_here")

# Convert to all formats
all_formats = converter.convert_all("your_xpub_key_here")
```

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
  🔗 Derivation Path: m/44'/0'/0'
  🔑 Key: xpub6CUGRUo...
  🔍 Fingerprint: A1B2C3D4
  📝 Descriptors:
    External (Receive): pkh([A1B2C3D4/44'/0'/0']xpub6CUGRUo.../0/*)
    Internal (Change): pkh([A1B2C3D4/44'/0'/0']xpub6CUGRUo.../1/*) 
```

#### Convert to specific format:
```bash
xpubkaleidoscope "your_xpub_key_here" -t zpub
```
Output example:
```
📥 Input key:
xpub:
  🌐 Network: MAINNET
  📦 Type: P2PKH or P2SH
  🔗 Derivation Path: m/44'/0'/0'
  🔑 Key: xpub6CUGRUo...
  🔍 Fingerprint: A1B2C3D4

📤 Converted key:
zpub:
  🌐 Network: MAINNET
  📦 Type: P2WPKH
  🔗 Derivation Path: m/84'/0'/0'
  🔑 Key: zpub6rFR7y4...
  🔍 Fingerprint: A1B2C3D4
```

#### Convert to all supported formats:
```bash
xpubkaleidoscope "your_xpub_key_here" -a
```
Output example:
```
📥 Input key:
xpub:
  🌐 Network: MAINNET
  📦 Type: P2PKH or P2SH
  🔗 Derivation Path: m/44'/0'/0'
  🔑 Key: xpub6CUGRUo...
  🔍 Fingerprint: A1B2C3D4

📤 Converting to all formats:

ypub:
  🌐 Network: MAINNET
  📦 Type: P2WPKH in P2SH
  🔗 Derivation Path: m/49'/0'/0'
  🔑 Key: ypub6Wq3G6n...
  🔍 Fingerprint: A1B2C3D4

zpub:
  🌐 Network: MAINNET
  📦 Type: P2WPKH
  🔗 Derivation Path: m/84'/0'/0'
  🔑 Key: zpub6rFR7y4...
  🔍 Fingerprint: A1B2C3D4
```

#### Show help:
```bash
xpubkaleidoscope -h

usage: xpubkaleidoscope [-h] [-t {xpub,ypub,zpub,Ypub,Zpub,tpub,upub,vpub,Upub,Vpub}] [-i] [-a] key

Convert between extended public key formats

positional arguments:
  key                   The extended public key to convert

options:
  -h, --help            show this help message and exit
  -t {xpub,ypub,zpub,Ypub,Zpub,tpub,upub,vpub,Upub,Vpub}, --to {xpub,ypub,zpub,Ypub,Zpub,tpub,upub,vpub,Upub,Vpub}
                        Target format to convert to
  -i, --identify        Only identify the format
  -a, --all             Convert to all supported formats
```

## ✨ Features
- 🔄 Convert between all major extended public key formats
- ✅ Validation of input keys
- 🌐 Support for both mainnet and testnet
- 💻 Simple command-line interface with colored output
- 🔌 Support for single-signature and multi-signature formats
- 🔍 Key fingerprint verification across conversions
- 📝 Output descriptors for wallet configuration

### 🔍 About Fingerprints
The fingerprint is a 4-byte identifier calculated from the public key using RIPEMD160(SHA256(pubkey)). It remains constant across different format conversions of the same key, helping to verify that the conversion was successful. The fingerprint is displayed in hexadecimal format (e.g., A1B2C3D4).

### 📝 About Descriptors
Output descriptors are a way to precisely describe how to derive addresses from keys. Each format has two descriptors: one for receiving addresses (external, 0/*) and one for change addresses (internal, 1/*). All descriptors use xpub format for consistency with Bitcoin Core:

#### Single-Signature Descriptors
- xpub/tpub:
  - External: `pkh([fingerprint/44'/0'/0']xpub.../0/*)`
  - Internal: `pkh([fingerprint/44'/0'/0']xpub.../1/*)`
- ypub/upub:
  - External: `sh(wpkh([fingerprint/49'/0'/0']xpub.../0/*))`
  - Internal: `sh(wpkh([fingerprint/49'/0'/0']xpub.../1/*))`
- zpub/vpub:
  - External: `wpkh([fingerprint/84'/0'/0']xpub.../0/*)`
  - Internal: `wpkh([fingerprint/84'/0'/0']xpub.../1/*)`

Example output:
```
zpub:
  🌐 Network: MAINNET
  📦 Type: P2WPKH
  🔗 Derivation Path: m/84'/0'/0'
  🔑 Key: zpub6rFR7y4...
  🔍 Fingerprint: A1B2C3D4
  📝 Descriptors:
    External (Receive): wpkh([A1B2C3D4/84'/0'/0']xpub6CUGRUo.../0/*)
    Internal (Change): wpkh([A1B2C3D4/84'/0'/0']xpub6CUGRUo.../1/*)
```

#### Multi-Signature Descriptors (Partial)
- Ypub/Upub:
  - External: `sh(wsh(multi(k,[fingerprint/path]xpub.../0/*,...)))`
  - Internal: `sh(wsh(multi(k,[fingerprint/path]xpub.../1/*,...)))`
- Zpub/Vpub:
  - External: `wsh(multi(k,[fingerprint/path]xpub.../0/*,...))`
  - Internal: `wsh(multi(k,[fingerprint/path]xpub.../1/*,...))`

Example multi-signature output:
```
Zpub:
  🌐 Network: MAINNET
  📦 Type: Multi-signature P2WSH
  🔗 Derivation Path: Custom
  🔑 Key: Zpub6rFR7y4...
  🔍 Fingerprint: A1B2C3D4
  📝 Descriptors:
    External (Receive): wsh(multi(k,[A1B2C3D4/Custom]xpub6CUGRUo.../0/*,...))
    Internal (Change): wsh(multi(k,[A1B2C3D4/Custom]xpub6CUGRUo.../1/*,...))
```

Note: 
- All keys in descriptors are shown in xpub format for compatibility with Bitcoin Core and other wallet software
- External (0/*) is used for receiving addresses
- Internal (1/*) is used for change addresses
- The asterisk (*) represents the address index

### 🔗 About Derivation Paths
All single-signature formats include a hardened subaccount index (0') in their derivation paths. This follows the BIP44 standard and its derivatives:
- Purpose: Hardened (e.g., 44', 49', 84')
- Coin type: 0' for mainnet, 1' for testnet
- Account: 0' (hardened subaccount)
- Change and address index: Handled by the descriptor's wildcard (*)

Multi-signature formats use custom derivation paths that should be specified according to your wallet configuration.

Example multi-signature output:
```
Zpub:
  🌐 Network: MAINNET
  📦 Type: Multi-signature P2WSH
  🔗 Derivation Path: Custom
  🔑 Key: Zpub6rFR7y4...
  🔍 Fingerprint: A1B2C3D4
  📝 Descriptors:
    External (Receive): wsh(multi(k,[A1B2C3D4/Custom]Zpub6rFR7y4.../0/*,...))
    Internal (Change): wsh(multi(k,[A1B2C3D4/Custom]Zpub6rFR7y4.../1/*,...))
```

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer
Always verify the output addresses and fingerprints before using them for real transactions. Incorrect conversions could lead to loss of funds.