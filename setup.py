from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import ws2812

setup(
    name = "ws2812",
    version = ws2812.__version__,
    url = 'https://github.com/cathalmccabe/ws2812',
    license = 'All rights reserved.',
    author = "Cathal McCabe",
    author_email = "cathal.mccabe@xilinx.com",
    packages = ['ws2812'],
    package_data = {
    '' : ['*.bit','*.tcl', '*. py'],
    },
    description = "PYNQ WS2812 controller overlay for PYNQ-Z1"
)