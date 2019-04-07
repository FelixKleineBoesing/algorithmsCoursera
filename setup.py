from setuptools import setup
from setuptools import find_packages


setup(name='algorithms',
      version='0.1.1',
      description='algorithms that were implemented during algorithms specialization on coursera',
      url='https://github.com/FelixKleineBoesing/algorithmsCoursera',
      author='Felix Kleine Bösing',
      license='WDL',
      packages=find_packages(),
      install_requires=['numpy'],
      include_package_data=True,
      zip_safe=False)