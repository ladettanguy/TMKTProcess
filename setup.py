from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
readme = (this_directory / "README.md").read_text()


setup(
    name='TMKTProcess',
    license='Apache 2.0',
    version='',
    author="Tanguy Ladet",
    maintainer="Tanguy Ladet",
    maintainer_email='sti2dlab.ladettanguy@gmail.com',
    author_email='sti2dlab.ladettanguy@gmail.com',
    packages=find_packages(include=['tmktprocess.*']),
    url='https://github.com/ladettanguy/TMKTProcess',
    download_url='https://github.com/ladettanguy/TMKTProcess.git',
    keywords=
    [
        'Thread',
        'Process',
        'Multi-process',
        "Multi-thread",
        "threading",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
    description="Easyfull multithreading package manager.",
    long_description=readme,
    long_description_content_type='text/markdown',
    zip_safe=False,
)
