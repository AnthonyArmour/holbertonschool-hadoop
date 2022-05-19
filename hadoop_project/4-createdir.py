#!/usr/bin/python3.8
"""Module has function that creates driectories
in hadoop using snakebite"""


from snakebite.client import Client
  

def createdir(l):
    """Creates directories in hadoop"""
    client = Client('localhost', 9000)

    for p in client.mkdir(l, create_parent=True):
        print(p)


if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    createdir(l)
