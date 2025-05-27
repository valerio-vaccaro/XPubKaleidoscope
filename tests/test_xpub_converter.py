import unittest
from xpubkaleidoscope import convert_xpub

class TestXPubConverter(unittest.TestCase):
    def setUp(self):
        # Mainnet Single-Signature
        # BIP44 - Legacy addresses (P2PKH)
        self.xpub = "xpub6CUGRUonZSQ4TWtTMmzXdrXDtypWKiKrhko4egpiMZbpiaQL2jkwSB1icqYh2cfDfVxdx4df189oLKnC5fSwqPfgyP3hooxujYzAu3fDVmz"
        # BIP49 - Nested SegWit (P2WPKH in P2SH)
        self.ypub = "ypub6Ww3ibxVfGzLrAH1PNcjyAWenMTbbAosGNB6VvmSEgytSER9azLDWCxoJwW7Ke7icmizBMXrzBx9979FfaHxHcrArf3zbeJJJUZPf663zsP"
        # BIP84 - Native SegWit (P2WPKH)
        self.zpub = "zpub6rFR7y4Q2AijBEqTUquhVz398htDFrtymD9xYYfG1m4wAcvPhXNfE3EfH1r1ADqtfSdVCToUG868RvUUkgDKf31mGDtKsAYz2oz2AGutZYs"

        # Mainnet Multi-Signature
        # P2WSH in P2SH
        self.Ypub = "Ypub6kvjDSz8jKJnFHi47fB5BzAMVx3hZpnL1KYZWqNxkzgHVuZKJcUJVqBKMUzxDkFoGzqK7nPsQxVhG3QHYVxbx4CqxvtvKKzePJxGAKqKn8g"
        # Native P2WSH
        self.Zpub = "Zpub74VSfvfhAJc3DqhGEh6Fm8V6Z5CS8aKxF3ggqJfYmfNWK8dHFrG3XqvVy4BaY7qRMKCxrD5yBHBJqxHBTTN4tWpvPyJpRKYGK1QMxSE9MBc"

        # Testnet Single-Signature
        # Legacy (P2PKH or P2SH)
        self.tpub = "tpubD6NzVbkrYhZ4XgiXtGrdW5XDAPFCL9h7we1vwNCpn8tGbBcgfVYjXyhWo4E1xkh56hjod1RhGjxbaTLV3X4FyWuejifB9jusQ46QzG87VKp"
        # SegWit (P2WPKH in P2SH)
        self.upub = "upub5EFU65HtV5TeiKPSDcFRQkW2mHHBGd4GAb7CzE8koZ5JrT4JyDrGyDKRbwwvKUNHBKfQs7jZoXqcGUByXB7eGYwbfmkzxHZLxV8m6EXtcxX"
        # Native SegWit (P2WPKH)
        self.vpub = "vpub5SLqN2bLY4WeZF3kL4VqiWF1itbf3A6oRrp7TxiYsSiUGpkZhsG4EYj6dKojC7P3epCCxw4nXgTpkxSWpZuX8RdXXRdLtFqzaYzP6bEAg6p"

        # Testnet Multi-Signature
        # P2WSH in P2SH
        self.Upub = "Upub5QbFtXVVHg4AaUxHGrgGHPGNQDhEvSHqEfVXxhbsX3pTMwGUh3PvgGp8cVg8TrYvpHxvwmZuEBAxsHJSUBrV7HqAeDvGjpfaEQu3hAkkorw"
        # Native P2WSH
        self.Vpub = "Vpub5dEvVGKn7251zFq7jXvUmJRbFCk5WaQWwgpQiKpH3fVYkEp4MvXRQQNvpCM1Y6jk7rYYpBgqzgT1CatJxqrHMFRjkb7Kc5am9QY8tLf4UEJ"

    def test_mainnet_single_sig_conversions(self):
        """Test conversions between mainnet single-signature formats"""
        # xpub conversions
        self.assertEqual(convert_xpub(self.xpub, "ypub"), self.ypub)
        self.assertEqual(convert_xpub(self.xpub, "zpub"), self.zpub)

        # ypub conversions
        self.assertEqual(convert_xpub(self.ypub, "xpub"), self.xpub)
        self.assertEqual(convert_xpub(self.ypub, "zpub"), self.zpub)

        # zpub conversions
        self.assertEqual(convert_xpub(self.zpub, "xpub"), self.xpub)
        self.assertEqual(convert_xpub(self.zpub, "ypub"), self.ypub)

    def test_mainnet_multi_sig_conversions(self):
        """Test conversions between mainnet multi-signature formats"""
        self.assertEqual(convert_xpub(self.Ypub, "Zpub"), self.Zpub)
        self.assertEqual(convert_xpub(self.Zpub, "Ypub"), self.Ypub)

    def test_testnet_single_sig_conversions(self):
        """Test conversions between testnet single-signature formats"""
        # tpub conversions
        self.assertEqual(convert_xpub(self.tpub, "upub"), self.upub)
        self.assertEqual(convert_xpub(self.tpub, "vpub"), self.vpub)

        # upub conversions
        self.assertEqual(convert_xpub(self.upub, "tpub"), self.tpub)
        self.assertEqual(convert_xpub(self.upub, "vpub"), self.vpub)

        # vpub conversions
        self.assertEqual(convert_xpub(self.vpub, "tpub"), self.tpub)
        self.assertEqual(convert_xpub(self.vpub, "upub"), self.upub)

    def test_testnet_multi_sig_conversions(self):
        """Test conversions between testnet multi-signature formats"""
        self.assertEqual(convert_xpub(self.Upub, "Vpub"), self.Vpub)
        self.assertEqual(convert_xpub(self.Vpub, "Upub"), self.Upub)

    def test_network_validation(self):
        """Test that conversions between different networks raise errors"""
        with self.assertRaises(ValueError):
            convert_xpub(self.xpub, "tpub")
        with self.assertRaises(ValueError):
            convert_xpub(self.tpub, "xpub")
        with self.assertRaises(ValueError):
            convert_xpub(self.Ypub, "Vpub")
        with self.assertRaises(ValueError):
            convert_xpub(self.Upub, "Zpub")

    def test_invalid_input_format(self):
        """Test handling of invalid input format"""
        invalid_xpub = "invalid_xpub_string"
        with self.assertRaises(ValueError):
            convert_xpub(invalid_xpub, "ypub")

    def test_invalid_target_format(self):
        """Test handling of invalid target format"""
        with self.assertRaises(ValueError):
            convert_xpub(self.xpub, "invalid_format")

    def test_same_format_conversion(self):
        """Test conversion to same format returns identical key"""
        self.assertEqual(convert_xpub(self.xpub, "xpub"), self.xpub)
        self.assertEqual(convert_xpub(self.ypub, "ypub"), self.ypub)
        self.assertEqual(convert_xpub(self.zpub, "zpub"), self.zpub)
        self.assertEqual(convert_xpub(self.Ypub, "Ypub"), self.Ypub)
        self.assertEqual(convert_xpub(self.Zpub, "Zpub"), self.Zpub)
        self.assertEqual(convert_xpub(self.tpub, "tpub"), self.tpub)
        self.assertEqual(convert_xpub(self.upub, "upub"), self.upub)
        self.assertEqual(convert_xpub(self.vpub, "vpub"), self.vpub)
        self.assertEqual(convert_xpub(self.Upub, "Upub"), self.Upub)
        self.assertEqual(convert_xpub(self.Vpub, "Vpub"), self.Vpub)

    def test_none_input(self):
        """Test handling of None input"""
        with self.assertRaises(ValueError):
            convert_xpub(None, "ypub")

    def test_empty_string_input(self):
        """Test handling of empty string input"""
        with self.assertRaises(ValueError):
            convert_xpub("", "ypub")

if __name__ == '__main__':
    unittest.main() 