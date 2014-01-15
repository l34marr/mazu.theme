from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='mazu.theme',
      version=version,
      description="MaZu Theme Package",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='TsungWei Hu',
      author_email='marr.tw@gmail.com',
      url='http://github.com/l34marr/mazu.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mazu'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
