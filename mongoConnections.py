# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Mongo Database connection and handling usage file"
"""
from flask_pymongo import PyMongo

def FireUpMongo(app_name):
    return PyMongo(app_name)

def getMainCollections(object):
    return object.db.main

def addData(mainCollections):
    mainCollections.insert({ "job1": {
                                "id": 1,
                                "postLink": "https://facebook.com",
                                "Likers":{
                                    "Name":[],
                                    "profileLink":[],
                                    "like":[]
                                },
                                "Commenters": {
                                    "Name":[],
                                    "profileLink":[],
                                    "like":[]
                                },
                                "dateStamp": "22/03/2018"
                            }
    }
    )
