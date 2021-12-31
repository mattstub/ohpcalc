import setuptools

setuptools.setup(
    name='ohpcalc',
    version='1.0.0',
    author='Matt Stubenhofer',
    author_email='matt.stubenhofer@gmail.com',
    description='Tool used to calculate and round overhead and profit for invoices',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'ohpcalc = ohpcalc.ohpcalc:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
