"""
XPubKaleidoscope - A Python utility for converting Bitcoin Extended Public Keys
"""

__version__ = "0.1.0"
from .xpub_converter import convert_xpub, main

__all__ = ["convert_xpub", "main"]