##Setup
The service uses the python HTTP Server library AIOHTTP.
Please make sure to install aiohttp python package via `pip install aiohttp`.

When you run `python Shortly.py`, it will start a server in address and port 127.0.0.1:15001.
Both the host address and port can be easily changed in the beginning of the file Shortly.py.

## Encode
### Input

For encoding your url, go to `127.0.0.1:15001/encode/<url_to_be_shortened>`,
where `url_to_be_shortened` is the URL you want to shorten.

#### Example:
###### Desired URL to be shortened: 
www.google.com
###### Go to: 
http://127.0.0.1:15001/encode/www.google.com

### Output
The output will be a json with the following format:

`{"shortened_url": "DOMAIN/short_url_suffix"}`

where the DOMAIN can be easily changed in the beginning of the file Shortly.py, and "short_url_suffix" 
is a suffix that uniquely identifies the original URL. The default DOMAIN is "http://short.est/".

## Decode
### Input
For decoding a shortened url into the original URL, go to `127.0.0.1:15001/decode/<short_url_suffix>`,
where `short_url_suffix` is the suffix of the shortened URL.

#### Example:
###### Shortened URL:
http://short.est/short_url_suffix
###### Go to: 
http://127.0.0.1:15001/decode/short_url_suffix

### Output
The output will be a json with the following format:

`{"original_url": "www.myoriginalurl.com"}`

If the given short_url_suffix was not returned by the server for a previously encoded URL, the server will return an
HTTP Error 400 (Bad Request).

## Unit Tests

In order to run the unit tests contained in the file `UnitTests.py`, just run `python UnitTests.py`.
