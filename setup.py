import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spongetext",  # Replace with your own username
    version="1.0.0",
    author="j wizzle",
    author_email="info@hossel.net",
    description="Creates text with randomly capitalized letters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jwizzle/spongetext",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
