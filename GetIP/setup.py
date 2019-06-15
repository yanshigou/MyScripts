"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import os
from pathlib import Path

APP = ['mac_tk.py']
APP_NAME = "tk_nginx"
DATA_FILES = []
OPTIONS = {
    "bdist_base": os.path.join(str(Path(os.getcwd()).parent), 'build'),
    "dist_dir": os.path.join(str(Path(os.getcwd()).parent), 'dist'),
    'iconfile': 'mac_tk.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleVersion': "2.2.0",
        'CFBundleShortVersionString': "2.2.0",
        'NSHumanReadableCopyright': "Copyright © 2019, Yanshigou, All Rights Reserved"
    }

}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
