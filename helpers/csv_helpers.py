# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "library to execute various csv related operations"
"""
import csv


def readCSV(_filename):
    """
    functions to read csv file
    :param _filename: a given file with the extension csv
    :return: a list
    """
    _list = []
    with open(_filename, 'rb') as csvFile:
        r = csv.reader(csvFile, delimiter=' ')
        for row in r:
            _list.append(row)
    return _list

def downloadCSV():
    """
    functions to download csv file from database
    :return:
    """
    pass


with open('eggs.csv', 'rb') as csvfile:
    r = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in r:
    print ', '.join(row)