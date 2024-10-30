from setuptools import setup, find_packages

setup(
    name='ckanext-restrictaccess',
    version='0.1',
    description='CKAN extension to remove logout symbol and restrict access to specific routes',
    author='Your Name',
    author_email='your.email@example.com',
    license='AGPL',
    url='https://github.com/gislab-augsburg/ckanext-restrictaccess',
    packages=find_packages(include=['ckanext', 'ckanext.*']),
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        restrictaccess=ckanext.restrictaccess.plugin:RestrictAccessPlugin
    ''',
)
