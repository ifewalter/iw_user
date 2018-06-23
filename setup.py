from setuptools import setup, find_packages

setup(
    name = "iw_user",
    version = "0.1",
    author="Ife Walter",
    author_email="ifewalter@gmail.com",
    include_package_data=True,
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        
    ],
    dependency_links=[
    ]

)


