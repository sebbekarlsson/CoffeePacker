from distutils.core import setup
import setuptools


setup(
    name='CoffeePacker',
    version='1.2',
    install_requires=[
        ''
    ],
    packages=[
        'coffeepacker'
    ],
    entry_points={
        "console_scripts": [
            "coffeepacker = coffeepacker.endpoints:pack",
        ]
    },
   )
