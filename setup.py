from setuptools import setup


setup(
    name='InputTest',
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'Pytest',
        ],
    entry_points='''
        [console_scripts]
        cli=cli:cli
    ''',
)
