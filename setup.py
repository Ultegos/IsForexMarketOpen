from setuptools import setup, find_packages

setup(name='ForexMarketGUI',version='0.1',packages=find_packages(),install_requires=['tkinter==0.1.0'],entry_points={'console_scripts': ['forex-market-gui=ForexMarketGUI.forex_market_gui:main']})
