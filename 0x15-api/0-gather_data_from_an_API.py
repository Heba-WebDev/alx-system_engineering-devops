#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    """ Gather data from an API """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    req = requests.get(url)
    name = req.json().get('name')
    completed = 0
    notCompleted = 0
    itemsUrl = "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1])
    data = requests.get(itemsUrl).json()
    if data is not None:
        for item in data:
            if item.get("completed") is True:
                completed = completed + 1
            else:
                notCompleted = notCompleted + 1
    print("Employee {} is done with tasks ({}/{})".format(name,
                        completed, notCompleted))
    for item in data:
        if item.get("completed") is True:
            print("\t {}".format(item.get('title')))
