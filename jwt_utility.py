#!/usr/bin/env python
import argparse
import jwt
import time
import uuid
from datetime import datetime


def generate_jwt(input_data, secret):
    """
    Generate a JWT with given input_data and secret.

    :param input_data: The data to include in the payload
    :param secret: The secret key to sign the JWT with
    :return: The generated JWT
    """
    iat = int(time.time())  # Current timestamp
    jti = str(uuid.uuid4())  # Unique cryptographic nonce

    # Create the payload with the specified claims
    payload = {
        "iat": iat,
        "jti": jti,
        "payload": {
            "data": input_data,
            "date": datetime.now().strftime("%Y-%m-%d"),
        },
    }

    # Generate and return the JWT
    return jwt.encode(payload, secret, algorithm="HS512")


def validate_jwt(jwt_token, secret):
    """
    Validate the given JWT using the provided secret.

    :param jwt_token: The JWT to validate
    :param secret: The secret key to validate the JWT with
    :return: The decoded JWT payload if valid, or an error message if invalid
    """
    try:
        # Decode and validate the JWT
        return jwt.decode(jwt_token, secret, algorithms=["HS512"])

    except jwt.InvalidTokenError as e:
        return str(e)


def main():
    parser = argparse.ArgumentParser(description="Generate and validate JWTs.")
    parser.add_argument("--data", type=str, help="Input data for JWT generation")
    parser.add_argument(
        "--secret",
        type=str,
        required=True,
        help="Secret key for JWT signing and validation",
    )
    parser.add_argument("--validate", type=str, help="JWT to validate")

    args = parser.parse_args()

    if args.data:
        jwt_token = generate_jwt(args.data, args.secret)
        print("Generated JWT:", jwt_token)

    if args.validate:
        validation_result = validate_jwt(args.validate, args.secret)
        print("Validation result:", validation_result)


if __name__ == "__main__":
    main()
