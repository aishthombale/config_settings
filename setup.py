import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="config_set",
    version="0.0.1",
    author="Aishwarya Thombale",
    author_email="aishwarya.thombale@gmail.com",
    description="A package to convert configuration file to flatdict and writing configuration files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=[
        "<configparser> >=<5.0.2>",
        "<flatdict> >=<4.0.1>",
        "<PyYAML> >=<5.4.1>",
        "<pytest> >=6.2.5>"],

    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8.6"
)