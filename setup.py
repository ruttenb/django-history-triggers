from setuptools import setup, find_packages
import history

setup(
    name='django-history',
    version=history.__version__,
    description='Management command and middleware for Django history triggers.',
    author='Dan Watson',
    author_email='watsond@imsweb.com',
    url='http://imsweb.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)