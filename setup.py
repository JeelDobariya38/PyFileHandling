from setuptools import setup

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

# Use the README.md file as the long description
long_description = read_file('README.md')

setup(
    name='pyfilehandling',
    version='2.0.0',
    description='A Python package for file manipulation operations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='JeelDobariya',
    author_email='dobariyaj34@gmail.com',
    url='https://github.com/JeelDobariya38/pyfilehandling',
    packages=['pyfilehandling'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords=['file handling','file manipulation','file operation']
    project_urls={
        'Bug Tracker': 'https://github.com/JeelDobariya38/pyfilehandling/issues',
        'Documentation': 'https://jeeldobariya38.github.io/pyfilehandling/',
        'Source Code': 'https://github.com/JeelDobariya38/pyfilehandling',
    },
    license='MIT',
)
