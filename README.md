## s3pipe

Command line tool to upload data to Amazon S3 via a pipe

### Usage in tar

create a wrapper script `mytarfilter`:

`#!/bin/bash
gpg -c --passphrase verysecret | /path/to/s3pipe -b my-bucket -k filename.tar.gpg`

then use tar:

`tar c --use-compress-program=/path/to/mytarfilter /my/files`
