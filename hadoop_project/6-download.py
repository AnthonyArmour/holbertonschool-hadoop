#!/usr/bin/python3.8
"""Module has function that downloads
hdfs file to local tmp directory"""


from snakebite.client import Client
  

def download(l):
    """Downloads file from hdfs to /tmp"""
    l = sorted(l, reverse=True)
    client = Client('localhost', 9000)

    for p in client.copyToLocal(l, "/tmp"):
        print(p)


if __name__ == "__main__":
    l = ["/holbies/input/lao.txt"]
    download(l)
    lao =  open("/tmp/lao.txt", "r")
    print(lao.read())
    lao.close()
