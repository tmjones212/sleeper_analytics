from setuptools import setup, find_packages

setup(
    name="sleeper_analytics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="TJ",
    author_email="your.email@example.com",
    description="A package for Sleeper fantasy football analytics and DraftKings API integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sleeper_analytics",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)