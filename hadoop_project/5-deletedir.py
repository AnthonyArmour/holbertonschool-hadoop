#!/usr/bin/python3.8
"""Module has function that deletes driectories
in hadoop using snakebite"""


from snakebite.client import Client
  

def deletedir(l):
    """Deletes directories in hadoop"""
    l = sorted(l, reverse=True)
    client = Client('localhost', 9000)

    for p in client.delete(l, recurse=True):
        print(p)


if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    deletedir(l)
