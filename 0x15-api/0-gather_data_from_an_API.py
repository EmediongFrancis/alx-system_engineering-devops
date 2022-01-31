#!/usr/bin/python3

'''
    Gathers data from an API.
'''

import requests as req
from sys import argv as arg


def getData():
    '''
        Gets data from an API.
    '''
    ListOfUsers = req.get('https://jsonplaceholder.typicode.com/users').json()
    ListOfTodos = req.get('https://jsonplaceholder.typicode.com/todos').json()
    TOTAL_NUMBER_OF = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for user in ListOfUsers:
        if user.get('id') == int(arg[1]):
            EMPLOYEE_NAME = user.get('name')
            break
    for todo in ListOfTodos:
        if todo.get('userId') == int(arg[1]):
            TOTAL_NUMBER_OF += 1
            if todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF))

    for task in TASK_TITLE:
        print(f'\t{task}')


if __name__ == '__main__':
    getData()
