from setuptools import setup

setup(
    name="proxy_chekcing",
    version="0.0.0",
    license="The MIT License",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    packages=["proxy_checking"],
    install_requires=[
        "setuptools ~= 58.0",
        "cython ~= 0.29.0",
        "certifi == 2021.5.30",
        "chardet == 4.0.0",
        "idna == 2.10",
        "PySocks == 1.7.1",
        "requests == 2.25.1",
        "urllib3 == 1.26.5",
        "httpx == 0.22.0",
    ],
    tests_require=["httmock>=1.2.5"],
    classifiers=[],
)
