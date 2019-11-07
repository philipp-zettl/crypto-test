# crypto-test
tests the compatibility of changing from deprecated package `pycrypto` to `pycryptodome`

during this "test" we encrypt the string `"value"` using both packages in separate containers. Each container runs
the provided `script.py`, which generates 3 outputs:

1) encryption of `"value"`
2) decryption of encrypted `"value"`
3) decryption of a string generated (in a test run) from the other package
## setup
requires `docker` and `docker-compose`

## run

run the command

`docker-compose up [-d]`