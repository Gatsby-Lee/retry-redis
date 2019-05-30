from setuptools import setup, find_packages

requires = [
    'redis',
    'tenacity',
]

tests_require = [
    'pytest',  # includes virtualenv
]

setup(
    name='retry-redis',
    version='1.0',
    description='Redis Client with retry decoration.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    author='Gatsby Lee',
    url='https://github.com/Gatsby-Lee/retry-redis',
    keywords='redis retry gatsby',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'testing': tests_require,
    },
)
