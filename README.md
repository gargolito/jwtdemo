# JWT example utility

Clone this repo and cd to jwt-utility directory. The utility has only been tested in Ubuntu Linux LTS 22.04 with python 3.9.9.

## Command Line Use:

I recommend that create a virtual environment using your preferred method.
Install dependencies:

```
pip install --no-cache -r requirements.txt
```

Ensure that the script is executable:

```
chmod u+x jwt_utility.py
```

Syntax:

```
usage: jwt_utility.py [-h] [--data DATA] --secret SECRET [--validate VALIDATE]

Generate and validate JWTs.

optional arguments:
  -h, --help           show this help message and exit
  --data DATA          Input data for JWT generation
  --secret SECRET      Secret key for JWT signing and validation
  --validate VALIDATE  JWT to validate
```

Example:

```
generate jwt:
./jwt_utility.py --data 'Give me a JWT of this test string.' --secret 128_char_hex_string

validate jwt:
./jwt_utility.py --validate "output of generated jwt" --secret 128_char_hex_string
```

## Run in docker as api:

- Build: `make build`
- Run: `make run`

### Test with curl

generate jwt:

```
curl -X POST -H "Content-Type: application/json" \
-d '{"data":"Give me a JWT of this test string."}' \
http://localhost:8080/generate-jwt
```

validate the generated jwt:

```
curl -X GET http://localhost:8080/validate-jwt/{JWT}
```

## Note on securely storing secret keys

Personally, I like neither hard-coded keys nor environment variables for key storage. I prefer to use a key store form which I can programmatically retrieve secrets. This can be achieved easily in linux with the [**pass**](https://www.passwordstore.org) package. In MacOS, they can be stored in the keychain. Keys can be retrieved from either with the [**keyring**](https://pypi.org/project/keyring). Another option is to use the cloud with solutions like [**AWS Secrets-Manager**](https://aws.amazon.com/secrets-manager).
