# 📦 Publishing XPubKaleidoscope to PyPI

## 📁 Package Structure
```
XPubKaleidoscope/
├── LICENSE
├── MANIFEST.in
├── README.md
├── PACKAGE.md
├── pyproject.toml
├── setup.cfg
├── src/
│   └── xpubkaleidoscope/
│       ├── __init__.py
│       ├── xpub_converter.py
│       └── utils/
│           └── __init__.py
└── tests/
    ├── __init__.py
    └── test_xpub_converter.py
```

## 📝 Required Files

### pyproject.toml
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"
```

### setup.cfg
```ini
[metadata]
name = xpubkaleidoscope
version = 0.1.0
author = Valerio Vaccaro
author_email = your.email@example.com
description = A Python utility for converting Bitcoin Extended Public Keys between different formats
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/valerio-vaccaro/XPubKaleidoscope
project_urls =
    Bug Tracker = https://github.com/valerio-vaccaro/XPubKaleidoscope/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    Topic :: Software Development :: Libraries :: Python Modules
    Topic :: Security :: Cryptography

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6
install_requires =
    # Add your dependencies here

[options.packages.find]
where = src
```

### MANIFEST.in
```
include LICENSE
include README.md
include requirements.txt
```

## 📋 Publishing Steps

1. **Set up your PyPI account**
   ```bash
   # Install twine
   pip install twine
   ```

2. **Create a PyPI account**
   - Go to https://pypi.org/account/register/
   - Create an account and verify your email
   - Enable two-factor authentication (recommended)

3. **Create a TestPyPI account**
   - Go to https://test.pypi.org/account/register/
   - Create an account for testing

4. **Build the package**
   ```bash
   # Install build tools
   pip install build

   # Build the package
   python -m build
   ```
   This will create both wheel (.whl) and source (.tar.gz) distributions in the `dist/` directory.

5. **Test your package locally**
   ```bash
   # Create a new virtual environment
   python -m venv test_env
   source test_env/bin/activate  # On Windows: test_env\Scripts\activate

   # Install the package locally
   pip install dist/xpubkaleidoscope-0.1.0.tar.gz

   # Test the installation
   python -c "import xpubkaleidoscope; print(xpubkaleidoscope.__version__)"
   ```

6. **Upload to TestPyPI first**
   ```bash
   # Upload to TestPyPI
   python -m twine upload --repository testpypi dist/*
   ```

7. **Test the TestPyPI installation**
   ```bash
   # Create a new virtual environment
   python -m venv test_env_pypi
   source test_env_pypi/bin/activate  # On Windows: test_env_pypi\Scripts\activate

   # Install from TestPyPI
   pip install --index-url https://test.pypi.org/simple/ xpubkaleidoscope
   ```

8. **Upload to PyPI**
   ```bash
   # Upload to PyPI
   python -m twine upload dist/*
   ```

## 🔄 Updating the Package

1. **Update version number**
   - Update the version in `setup.cfg`

2. **Clean previous builds**
   ```bash
   rm -rf build/ dist/ *.egg-info/
   ```

3. **Rebuild and upload**
   ```bash
   # Build new distributions
   python -m build

   # Upload to PyPI
   python -m twine upload dist/*
   ```

## 📝 Best Practices

1. **Version numbering**
   - Follow semantic versioning (MAJOR.MINOR.PATCH)
   - Example: 1.0.0, 1.0.1, 1.1.0

2. **Git tags**
   ```bash
   git tag -a v0.1.0 -m "First release"
   git push origin v0.1.0
   ```

3. **Documentation**
   - Keep README.md updated
   - Include examples
   - Document all public functions

4. **Testing**
   - Write comprehensive tests
   - Test on multiple Python versions
   - Use GitHub Actions for CI/CD

## ⚠️ Common Issues

1. **Package name already taken**
   - Check availability on PyPI before choosing a name
   - Use `pip search packagename` or check PyPI website

2. **Upload errors**
   - Ensure unique version numbers
   - Check file permissions
   - Verify PyPI credentials

3. **Installation issues**
   - Verify dependencies in setup.cfg
   - Test in clean virtual environment
   - Check Python version compatibility

## 🔗 Useful Resources

- [PyPI documentation](https://pypi.org/help/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Twine documentation](https://twine.readthedocs.io/)
- [Setup.cfg documentation](https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html)