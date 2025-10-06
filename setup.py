from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="focus-cli",
    version="0.1.0",
    author="Ravindra Devrani",
    description="A simple CLI time tracker for focus sessions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/focus-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[
        "plyer>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "focus=focus_cli.cli:main",
        ],
    },
)
