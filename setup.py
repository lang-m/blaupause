import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='blaupause',
    version='0.1',
    description=('Example package used as a template for setting up '
                 'Python packages/repositories.'),
    # these two lines allow using markdown README
    long_description=long_description,
    long_description_content_type='text/markdown',
    # url='https://ubermag.github.io',
    author='Martin Lang and Marijan Beg',
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=['pytest>=6.0.0'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Education',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Natural Language :: English',
                 'Operating System :: MacOS',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: Unix',
                 'Programming Language :: Python :: 3 :: Only',
                 ]
)
