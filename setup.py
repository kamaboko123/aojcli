from setuptools import setup, find_packages

requires = ["requests", "texttable"]

setup(
    name='aojcli',
    version='0.1',
    description='AOJ submit tool',
    url='https://github.com/kamaboko123/aojcli',
    author='kamaboko123',
    author_email='6112062+kamaboko123@users.noreply.github.com',
    license='LGPL',
    packages=['aojcli'],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    scripts=['bin/aojcli']
)

