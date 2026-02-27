from setuptools import setup, find_packages

setup(
    name="simple-safe-write",
    version="1.0.0",
    description="Simple atomic file writes (write-then-rename)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="raccoonette",
    url="https://github.com/MopicMP/simple-safe-write",
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
)
