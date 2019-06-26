#!/usr/bin/python

import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def do_readme(link, fd):
    rep = requests.get(link)
    if rep.status_code == 200:
        soup = BeautifulSoup(rep.text, "html.parser")
        print ("%s" % soup, end = "")

def loop_url(link, fd):
    rep = requests.get(link)
    if rep.status_code != 200:
        print ("error occured on '%s'" % link)
        return (-1)
    fd.write(link + "\n")
    soup = BeautifulSoup(rep.text, "html.parser")
    for a in soup.findAll("a"):
        result = a["href"]
        if ".." in result:
            continue
        elif "README" in result:
            do_readme(link + result, fd)
        final = link + "/" + result
        loop_url(final, fd)


def main():
    fd = open("result.log", "w")
    linked = "http://192.168.43.34/.hidden"
    loop_url(linked, fd)
    fd.close

if __name__ == "__main__":
    main()
