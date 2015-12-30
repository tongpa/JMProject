from distutils.core import setup

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys
 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(name='surveymodel',
      version='1.0',
      description="model of poll and survey",
      
      author="Tong",
      #package_dir={'' : 'src'},
      #package_dir={'survey': ''},
     #packages=['logsurvey'],
     packages=find_packages(exclude=['ez_setup']),
     package_dir={'surveymodel': 'surveymodel',
                  'surveyobject':'surveyobject'
                  },
      #py_modules=['logsurvey'],
      #packages=find_packages(exclude=['ez_setup']),
       
      include_package_data=True,
    
       
      zip_safe=True
      )