from setuptools import setup
import cpp2python

setup(
    name='cpp2python',
    version='1.0',
    description='Helps to convert C/C++ sources to C/C++ -like Python sources.',
    long_description=cpp2python.help,
    url='https://github.com/XShacker-XingyiHackerSubAccount/Cpp2Python3-bug/tree/main/V1',
    author='Xingyi Sun',
    author_email='XShacker2023@hotmail.com',
    license='Apache License',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='cpp python',

    scripts=['cpp2python.py']
)
