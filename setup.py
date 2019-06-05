import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scaffold",
    python_requires='>3.6',
    version="0.0.1dev",
    author="Swag mcSwaggerson",
    author_email="swag.mcswaggerson@nirovision.com",
    description="Template repo to show tox and pytest friendship",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    test_suite="tests",
    install_requires=[]
)
