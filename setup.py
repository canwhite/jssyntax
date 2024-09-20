from setuptools import setup, find_packages

setup(
    name="jssyntax",
    version="0.2.5",
    description="Write python using js syntax",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Zack Qiao",
    author_email="dangbai752716886@gmail.com",
    url="https://github.com/canwhite/jssyntax",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
