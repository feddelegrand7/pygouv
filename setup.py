from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(

    name='pygouv',
    version='0.0.8',
    url='https://github.com/feddelegrand7/pygouv',
    author='Mohamed El Fodil Ihaddaden',
    author_email='ihaddaden.fodeil@gmail.com',
    description='API wrapper for data.gouv.fr',
    py_modules=["pygouv"],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English"

    ],
    install_requires=[
        "pandas ~= 1.1",
        "requests ~= 2.25",
    ],

    extras_require={

        "dev": [
            "pytest >= 3.7",
        ]


    }

)
