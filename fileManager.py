from datetime import datetime


def readFromFile(file_name):
    f_descriptor = open(file_name, 'r')
    data = f_descriptor.read()
    f_descriptor.close()
    return data


def writeInFile(file_name, data):
    f_descriptor = open(file_name, 'w')
    f_descriptor.write(data)
    f_descriptor.close()


def getTimeFromFile(file_name, date_format):
    return datetime.strptime(readFromFile(file_name), date_format)

