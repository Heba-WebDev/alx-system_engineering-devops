#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    """ Gather data from an API """
    # Fetching the user data and getting the name
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    req = requests.get(url)
    name = req.json().get('name')
    # Fetching the todos
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    req = requests.get(url)
    todos = req.json()
    len = len(todos)
    completed = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks ({}/{})".format(
        name, completed, len))
    for task in completed:
        print("\t {}".format(task.get('title')))
