from setuptools import setup,find_packages

setup(
    name='tasklogger',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    tasklogger=cli:cli
    '''
)