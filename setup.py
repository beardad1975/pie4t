import setuptools

# with open("README.md", "r",encoding="utf8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="pie4t",
    version="0.0.4",
    author="Wen-Hung, Chang 張文宏",
    author_email="beardad1975@nmes.tyc.edu.tw",
    description="Physics Impulse Engine wrapper for Teenagers",
    long_description="Physics Impulse Engine wrapper for Teenagers",
    long_description_content_type="text/markdown",
    url="https://github.com/beardad1975/pie4t",
    #packages=setuptools.find_packages(),
    platforms=["Windows"],
    python_requires=">=3.5",
    packages=['pie4t','物理模組'],
    install_requires = ['arcade==2.4a10', 'pymunk==5.6.0', 'pyperclip==1.8.0'],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: Microsoft :: Windows",
            #"Operating System :: MacOS",
            #"Operating System :: POSIX :: Linux",
            "Natural Language :: Chinese (Traditional)",
        ],
)