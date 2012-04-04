# s3pipe

Command line tool to upload data to Amazon S3 via a pipe

## Usage with tar

upload:

`tar c /my/files | gpg -c --passphrase verysecret | s3pipe -b my-bucket -k filename.tar.gpg`

and download:

`s3pipe -b my-bucket -k filename.tar.gpg -d | gpg -d --passphrase verysecret | tar x`
