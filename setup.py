from setuptools import setup

setup(
    name='evixtract',
    version='1.0.0',
    py_modules=['evixtract'],
    entry_points={
        'console_scripts': [
            'evixtract=evixtract:main',
        ],
    },
    author='Waqas Ahmad',
    description='A tool for data acquisition and imaging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/WaqasWikky/evixtract',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
