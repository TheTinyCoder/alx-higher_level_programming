#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""


from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
