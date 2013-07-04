'''
Created on Jul 14, 2012

@author: Michele Sama (m.sama@puzzledev.com)
'''

#!/usr/bin/env python

from distutils.core import setup

setup(name = 'django-uploadcleaner',
      version = '1.1',
      author = "Original: Michele Sama. Fork: Darie Petrov",
      author_email = "darie@cambriansoft.org",
      maintainer = "Darie Petrov",
      maintainer_email = "darie@cambriansoft.org",
      url = "",
      description = "",
      long_description = "",
      download_url = "",
      classifiers = [
                'Environment :: Web Environment',
                'Programming Language :: Python',
                ],
      platforms = [
                "Linux",
                ],
      license = "",
      packages = [
                'uploadcleaner',
                'uploadcleaner.management',
                'uploadcleaner.management.commands',
                'uploadcleaner.admin',
                ],
     )
