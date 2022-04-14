from setuptools import setup, find_packages

package_name = 'robomaster_s1_driver'

setup(
    name=package_name,
    version='0.0.0',
    package_dir = {
        '': 'robomaster_s1_driver'
    },
    install_requires=[
        'setuptools',
        'python-can',
    ]
)