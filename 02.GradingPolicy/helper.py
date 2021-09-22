import json


def to_json(object):
    jsonString = json.dumps(object.__dict__)
    jsonData = json.loads(jsonString)
    return jsonData


def is_none(value, whatIfNone):

    returnValue = value
    if (value == None):
        returnValue = whatIfNone
    return returnValue
