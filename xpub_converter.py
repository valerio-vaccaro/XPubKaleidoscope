#!/usr/bin/env python3

import sys
import argparse
import base58
import hashlib
import binascii
import hmac

# Version bytes for different formats with their corresponding BIP32 paths and address types
VERSION_BYTES = {
    # Mainnet Single-Signature
    'xpub': {
        'bytes': b'\x04\x88\xb2\x1e',
        'path': "m/44'/0'/0'",
        'address_type': 'P2PKH or P2SH',
        'network': 'mainnet'
    },
    'ypub': {
        'bytes': b'\x04\x9d\x7c\xb2',
        'path': "m/49'/0'/0'",
        'address_type': 'P2WPKH in P2SH',
        'network': 'mainnet'
    },
    'zpub': {
        'bytes': b'\x04\xb2\x47\x46',
        'path': "m/84'/0'/0'",
        'address_type': 'P2WPKH',
        'network': 'mainnet'
    },
    # Mainnet Multi-Signature
    'Ypub': {
        'bytes': b'\x02\x95\xb4\x3f',
        'path': "Custom",
        'address_type': 'Multi-signature P2WSH in P2SH',
        'network': 'mainnet'
    },
    'Zpub': {
        'bytes': b'\x02\xaa\x7e\xd3',
        'path': "Custom",
        'address_type': 'Multi-signature P2WSH',
        'network': 'mainnet'
    },
    # Testnet Single-Signature
    'tpub': {
        'bytes': b'\x04\x35\x87\xcf',
        'path': "m/44'/1'/0'",
        'address_type': 'P2PKH or P2SH',
        'network': 'testnet'
    },
    'upub': {
        'bytes': b'\x04\x4a\x52\x62',
        'path': "m/49'/1'/0'",
        'address_type': 'P2WPKH in P2SH',
        'network': 'testnet'
    },
    'vpub': {
        'bytes': b'\x04\x5f\x1c\xf6',
        'path': "m/84'/1'/0'",
        'address_type': 'P2WPKH',
        'network': 'testnet'
    },
    # Testnet Multi-Signature
    'Upub': {
        'bytes': b'\x02\x42\x89\xef',
        'path': "Custom",
        'address_type': 'Multi-signature P2WSH in P2SH',
        'network': 'testnet'
    },
    'Vpub': {
        'bytes': b'\x02\x57\x54\x83',
        'path': "Custom",
        'address_type': 'Multi-signature P2WSH',
        'network': 'testnet'
    }
}

FORMATS = list(VERSION_BYTES.keys())

# Add color constants
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'  # Added for fingerprint
    CYAN = '\033[96m'  # Added for descriptor
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Add icons for different attributes
ICONS = {
    'key': '🔑',
    'network': {
        'mainnet': '🌐',
        'testnet': '🧪'
    },
    'type': '📦',
    'path': '🔗',
    'input': '📥',
    'output': '📤',
    'error': '❌',
    'success': '✅',
    'fingerprint': '🔍',
    'descriptor': '📝'
}

def double_sha256(data):
    """Perform double SHA256 hash."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def verify_checksum(decoded):
    """Verify the checksum of a decoded extended public key."""
    if len(decoded) != 82:
        return False
    data, checksum = decoded[:-4], decoded[-4:]
    return double_sha256(data)[:4] == checksum

def get_format_info(fmt):
    """Get detailed information about a format."""
    info = VERSION_BYTES[fmt]
    return {
        'format': fmt,
        'path': info['path'],
        'type': info['address_type'],
        'network': info['network'],
    }

def calculate_fingerprint(xpub):
    """Calculate the fingerprint (first 4 bytes of hash160) of the key."""
    try:
        decoded = base58.b58decode(xpub)
        # Extract the public key part (33 bytes) starting from byte 45
        pubkey = decoded[45:78]
        # Calculate RIPEMD160(SHA256(pubkey))
        sha256_hash = hashlib.sha256(pubkey).digest()
        ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
        # Take first 4 bytes as fingerprint
        fingerprint = ripemd160_hash[:4].hex().upper()
        return fingerprint
    except Exception:
        return "Unable to calculate fingerprint"

def convert_to_xpub(key):
    """Convert any format back to xpub for descriptor."""
    try:
        current_format = identify_format(key)
        if current_format == 'xpub':
            return key
        return convert_xpub(key, 'xpub')
    except Exception:
        return key  # Return original key if conversion fails

def get_descriptors(fmt, key, fingerprint, path):
    """Get external and internal descriptors based on format."""
    base_descriptors = {
        'xpub': {
            'external': 'pkh([{fingerprint}/{path}]{key}/0/*)',
            'internal': 'pkh([{fingerprint}/{path}]{key}/1/*)'
        },
        'ypub': {
            'external': 'sh(wpkh([{fingerprint}/{path}]{key}/0/*))',
            'internal': 'sh(wpkh([{fingerprint}/{path}]{key}/1/*))'
        },
        'zpub': {
            'external': 'wpkh([{fingerprint}/{path}]{key}/0/*)',
            'internal': 'wpkh([{fingerprint}/{path}]{key}/1/*)'
        },
        'Ypub': {
            'external': 'sh(wsh(multi(k,[{fingerprint}/{path}]{key}/0/*,...)))',
            'internal': 'sh(wsh(multi(k,[{fingerprint}/{path}]{key}/1/*,...)))'
        },
        'Zpub': {
            'external': 'wsh(multi(k,[{fingerprint}/{path}]{key}/0/*,...))',
            'internal': 'wsh(multi(k,[{fingerprint}/{path}]{key}/1/*,...))'
        },
        'tpub': {
            'external': 'pkh([{fingerprint}/{path}]{key}/0/*)',
            'internal': 'pkh([{fingerprint}/{path}]{key}/1/*)'
        },
        'upub': {
            'external': 'sh(wpkh([{fingerprint}/{path}]{key}/0/*))',
            'internal': 'sh(wpkh([{fingerprint}/{path}]{key}/1/*))'
        },
        'vpub': {
            'external': 'wpkh([{fingerprint}/{path}]{key}/0/*)',
            'internal': 'wpkh([{fingerprint}/{path}]{key}/1/*)'
        },
        'Upub': {
            'external': 'sh(wsh(multi(k,[{fingerprint}/{path}]{key}/0/*,...)))',
            'internal': 'sh(wsh(multi(k,[{fingerprint}/{path}]{key}/1/*,...)))'
        },
        'Vpub': {
            'external': 'wsh(multi(k,[{fingerprint}/{path}]{key}/0/*,...))',
            'internal': 'wsh(multi(k,[{fingerprint}/{path}]{key}/1/*,...))'
        }
    }
    
    descriptors = base_descriptors[fmt]
    return {
        'external': descriptors['external'].format(
            key=key,
            fingerprint=fingerprint,
            path=path
        ),
        'internal': descriptors['internal'].format(
            key=key,
            fingerprint=fingerprint,
            path=path
        )
    }

def print_key_info(fmt, key=None):
    """Print formatted key information with colors and icons."""
    info = get_format_info(fmt)
    network_icon = ICONS['network'][info['network']]
    
    print(f"\n{Colors.BOLD}{info['format']}:{Colors.ENDC}")
    print(f"  {network_icon} Network: {Colors.BLUE}{info['network'].upper()}{Colors.ENDC}")
    print(f"  {ICONS['type']} Type: {Colors.GREEN}{info['type']}{Colors.ENDC}")
    print(f"  {ICONS['path']} Derivation Path: {Colors.YELLOW}{info['path']}{Colors.ENDC}")
    if key:
        print(f"  {ICONS['key']} Key: {Colors.BOLD}{key}{Colors.ENDC}")
        fingerprint = calculate_fingerprint(key)
        print(f"  {ICONS['fingerprint']} Fingerprint: {Colors.PURPLE}{fingerprint}{Colors.ENDC}")
        xpub_key = convert_to_xpub(key)
        
        # Get descriptors
        descriptors = get_descriptors(
            fmt,
            xpub_key,
            fingerprint,
            info['path'].lstrip('m/')
        )
        
        # Print descriptors
        print(f"  {ICONS['descriptor']} Descriptors:")
        print(f"    External (Receive): {Colors.CYAN}{descriptors['external']}{Colors.ENDC}")
        print(f"    Internal (Change): {Colors.CYAN}{descriptors['internal']}{Colors.ENDC}")

def identify_format(xpub):
    """Identify the format of an extended public key."""
    try:
        decoded = base58.b58decode(xpub)
        if not verify_checksum(decoded):
            return "Invalid checksum"
            
        version = decoded[:4]
        for fmt, info in VERSION_BYTES.items():
            if version == info['bytes']:
                return fmt
        return "Unknown format"
    except Exception:
        return "Invalid key"

def convert_xpub(xpub, target_format):
    """Convert xpub to target format."""
    if target_format not in VERSION_BYTES:
        raise ValueError(f"Unsupported target format: {target_format}")
    
    try:
        # Decode the original key
        decoded = base58.b58decode(xpub)
        
        # Verify checksum
        if not verify_checksum(decoded):
            raise ValueError("Invalid checksum")
        
        # Verify length
        if len(decoded) != 82:
            raise ValueError("Invalid key length")
        
        # Extract key data without version bytes and checksum
        key_data = decoded[4:-4]
        
        # Create new key with target version
        new_key_data = VERSION_BYTES[target_format]['bytes'] + key_data
        
        # Calculate new checksum
        new_checksum = double_sha256(new_key_data)[:4]
        
        # Combine everything
        final_key = new_key_data + new_checksum
        
        # Encode back to base58
        return base58.b58encode(final_key).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Conversion failed: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Convert between extended public key formats')
    parser.add_argument('key', help='The extended public key to convert')
    parser.add_argument('-t', '--to', choices=FORMATS, help='Target format to convert to')
    parser.add_argument('-i', '--identify', action='store_true', help='Only identify the format')
    parser.add_argument('-a', '--all', action='store_true', help='Convert to all supported formats')
    
    args = parser.parse_args()
    
    try:
        current_format = identify_format(args.key)
        
        if current_format == "Invalid key":
            print(f"{ICONS['error']} {Colors.RED}Error: Invalid extended public key{Colors.ENDC}")
            sys.exit(1)
        
        if current_format == "Unknown format":
            print(f"{ICONS['error']} {Colors.RED}Error: Unknown key format{Colors.ENDC}")
            sys.exit(1)
            
        print(f"\n{ICONS['input']} Input key:")
        print_key_info(current_format, args.key)
        
        if args.identify:
            sys.exit(0)
            
        if args.all:
            print(f"\n{ICONS['output']} Converting to all formats:")
            for fmt in FORMATS:
                if fmt != current_format:
                    try:
                        converted = convert_xpub(args.key, fmt)
                        print_key_info(fmt, converted)
                    except ValueError as e:
                        print(f"\n{ICONS['error']} {fmt}: {Colors.RED}Conversion failed{Colors.ENDC}")
        elif args.to:
            if args.to == current_format:
                print(f"\n{ICONS['error']} Input and target formats are the same")
            else:
                converted = convert_xpub(args.key, args.to)
                print(f"\n{ICONS['output']} Converted key:")
                print_key_info(args.to, converted)
        
    except Exception as e:
        print(f"{ICONS['error']} {Colors.RED}Error: {str(e)}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()