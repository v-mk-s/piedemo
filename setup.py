import platform
from setuptools import setup
from setuptools import find_packages


with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name='piedemo',
    version='1.0.3',
    python_requires=f'>=3.6,<3.9',
    description='PyTorch based Web Demo app',
    url='https://github.com/PieDataLabs/piedemo',
    author='George Kasparyants',
    author_email='gg@piedata.ai',
    license='',
    packages=find_packages(include=['piedemo', 'piedemo.*']),
    install_requires=requirements,
    zip_safe=True,
    include_package_data=True,
    exclude_package_data={'': ['tests']},
    platforms=[platform.platform()],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6"
    ],
    scripts=["scripts/piedemo"]
)
