# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:04:51 2021

@author: hugod
"""

import json as j
import matplotlib.pyplot as plt

course_string = '''
{
"course": 411,
"courseName": "Software in Telecommunications",
"releaseYear": 2021,
"courseActive": true,
"droppedStudents": null,
"date": 20210218,
"someData": [[11,2], [22, 4], [33, 1], [44,5]],
"scores": {"a":77, "b":46, "c":91}
}
'''

data = j.loads(course_string)
X = []
Y = []
for a in data["someData"]:
    X.append(a[0])
    Y.append(a[1])

plt.plot(X,Y, "r*")
