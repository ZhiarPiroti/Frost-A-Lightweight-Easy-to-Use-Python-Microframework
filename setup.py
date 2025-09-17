from setuptools import setup, find_packages

setup(
    name="pythonfrost",
    version="0.1.1.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[], 
    author="Zhiar Piroti",
    author_email="zhiarsmp11@gmail.com",
    description="A lightweight Python microframework for building fast and simple web apps.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZhiarPiroti/Frost-A-Lightweight-Easy-to-Use-Python-Microframework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
