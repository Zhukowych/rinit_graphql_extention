from distutils.core import setup
setup(
  name = 'rinit_graphql_extention', 
  packages = ['rinit_graphql_extention'],
  version = '0.1',     
  license='gpl-3.0',   
  description = 'packet to make work with graphql more comfortabke', 
  author = 'Max Zhuk',
  author_email = 'mzmzhuk@gmail.com',
  url = 'https://github.com/Zhukowych/',
  download_url = 'https://github.com/Zhukowych/rinit_graphql_extention/v_01.tar.gz',    # I explain this later on
  keywords = ['rinit_graphql_extention'], 
  install_requires=[          
          'django',
          'graphene',
		  'graphql'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',        
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: gpl-3.0 License',  
    'Programming Language :: Python :: 3.8',
  ],
)
