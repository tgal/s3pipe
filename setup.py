from distutils.core import setup

setup(
  name = 's3pipe',
  version = '1.0',
  author = 'Tobias Galitzien',
  author_email = 'tg@trusttheadmin.de',
  url = 'https://github.com/tgal/s3pipe',
  description = 'Command line tool to upload data to Amazon S3 via a pipe',
  scripts = ['s3pipe'],
)
