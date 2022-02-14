import base64
import requests

def get_token():
    #  fetch a new token
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    # encode consumer key and secret
    consumer_key = "SElUWzbMYVGboeFAXq2UuHGFQnrXgVKM"
    consumer_secret = "iJ4LlSt6JIuHulg8"
    encode_secret = encodeClientCredentials()
    print("ENCODED", encode_secret)
    return Response("here")


def encodeClientCredentials():
    consumer_key = "SElUWzbMYVGboeFAXq2UuHGFQnrXgVKM"
    consumer_key_bytes =consumer_key.encode("utf8")
    consumer_secret = "iJ4LlSt6JIuHulg8"
    return base64.b64encode(consumer_key_bytes)
