import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="HalleyEncrypt",
    version="0.1.0",
    author="Raxabi",
    author_email="originalraxabi@gmail.com",
    maintainer_email="originalraxabi@gmail.com",
    description="A starter encrypt package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Raxabi/HalleyEncrypt",
    project_urls={
        "Bug Tracker": "https://github.com/Raxabi/HalleyEncrypt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="HalleyCrypt"),
    python_requires=">=3.6",
)