# -*- coding: utf-8 -*-
import json

def Find():
    print("ABCDF")

def FindOne(id):
   with open("database.json",encoding='utf8') as file:
    data = json.load(file)
    for i in data:
        if id == i["id"]:
           return i


