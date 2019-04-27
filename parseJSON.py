import json

def getKeys(pars):
    keys = []
    for computer in pars['computers']:
        for key in computer.keys():
            keys.append(key.upper())
        break
    keys = ', '.join(map(str, keys))
    return keys

def getVals(pars):
    list = []
    for computer in pars['computers']:
        tmp = []
        for value in computer.values():
            tmp.append(value)
        list.append(tmp)
    return list

def getHeaders(pars):
    headers = []
    for computer in pars['computers']:
        for key in computer.keys():
            definition = key + ' VARCHAR(255)'
            headers.append(definition)
        break

    headers = ', '.join(map(str, headers))
    return headers


