# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "file to execute various csv related operations"
"""
import csv

__all__ = [
    'readCSV',
    'downloadCSV',
]

def readCSV(_filename, _columnName):
    """
    functions to read csv file
    :param _filename: a given file with the extension csv
    :param _columnName: string name of the column to read
    :return: a list
    """
    _list = []
    with open(_filename, 'r') as csvFile:
        r = csv.DictReader(csvFile)
        for row in r:
            _list.append(row[_columnName])
    return _list

def downloadCSV():
    """
    functions to download csv file from database
    :return:
    """
    #TODO: query the data and write to a file
    #TODO: save the file to desktop with time
    pass