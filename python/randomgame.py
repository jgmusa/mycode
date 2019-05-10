#!/usr/bin/python3

import requests

MYAPI = "https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new"

def main():

    results = requests.get(MYAPI)
    # print("Read = ", results)
    if "1" in results.text:
        print("You Won!!!")
    else:
        print("You lost!")

main()
