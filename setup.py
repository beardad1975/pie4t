import setuptools

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pie4t",
    version="0.0.2",
    author="Wen-Hung, Chang",
    author_email="beardad1975@nmes.tyc.edu.tw",
    description="Physics Impulse Engine wrapper for Teenagers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beardad1975/pie4t",
    #packages=setuptools.find_packages(),
    packages=['pie4t'],
    install_requires = ['pyglet==1.4.1', 'pymunk==5.5.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: Chinese (Traditional)",
    ],
)