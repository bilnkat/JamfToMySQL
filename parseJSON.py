import json

def getKeys(req):
    keys = []
    parsed = json.loads(req.content)
    for computer in parsed['computers']:
        for key in computer.keys():
            keys.append(key)
        break
    keys = ', '.join(map(str, keys))
    return keys

def getVals(req):
    parsed = json.loads(req.content)
    list = []
    for computer in parsed['computers']:
        tmp = []
        for value in computer.values():
            tmp.append(value)
        list.append(tmp)
    return list

def getHeaders(req,):
    headers = []
    parsed = json.loads(req.content)
    for computer in parsed['computers']:
        for key in computer.keys():
            definition = key + ' VARCHAR(255)'
            headers.append(definition)
        break

    headers = ', '.join(map(str, headers))
    return headers


