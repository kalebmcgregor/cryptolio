from distutils.core import setup


install_requires = [
    'pyyaml==3.12',
    'requests==2.18.4'
]

setup(
    name='cryptolio',
    version='1.0.0',
    packages=['cryptolio'],
    url='',
    license='GPL-3.0',
    author='Kaleb McGregor',
    author_email='',
    description='Command line tool to check your crypto coin roi and profit'
)
