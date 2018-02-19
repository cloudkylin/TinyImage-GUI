import json
from urllib import request, parse, error
import re
import socket
import tinify

def loadkey():
    try:
        fo = open("config.json", "r")
        conf = json.loads(fo.read())
        fo.close()
    except:
        raise Exception("Can't find your config.")
    try:
        key = conf['key']
    except:
        raise Exception("Can't find KEY!")
    if len(key) != 32:
        raise Exception("Can't find true KEY!")
    return key


def inputkey(key):
    if len(key) != 32:
        raise Exception("Please enter true API-Key!")
    try:
        validate(key)
    except tinify.Error as e:
        raise e
    try:
        fo = open("config.json", "w+")
        conf = fo.read()
    except:
        raise Exception("Can't write config! Please check your permission.")
    try:
        conf = json.loads(conf)
    except:
        conf = {}
    conf['key'] = str(key)
    fo.write(json.dumps(conf))
    fo.close()
    return True


def registerkey(name, mail):
    if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', mail) is None:
        raise Exception("Wrong e-mail address!")
    timeout = 20
    url = 'https://tinypng.com/web/subscription'
    header = {
        'Host': 'tinypng.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'application/json',
        'Referer': 'https://tinypng.com/developers',
        'content-type': 'application/json',
        'Connection': 'keep-alive'
    }
    data = {
        "fullName": name,
        "mail": mail
    }
    data = json.dumps(data).encode('utf-8')
    try:
        socket.setdefaulttimeout(timeout)
        req = request.Request(url, headers=header, data=data)
        req = request.urlopen(req)
    except error.HTTPError as e:
        msg = json.loads(e.read())
        raise Exception(msg['message'])
    except error.URLError as e:
        raise e
    return True


def validate(key):
    try:
        tinify.key = key
        tinify.validate()
    except tinify.Error as e:
        raise Exception(e)