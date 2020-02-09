import requests

def get_xfer_info(options, sslverify, username, pw, host):
    return requests.get(_url(host,'/ops/transfers'), verify=sslverify, params=options, auth=(username, pw))

def get_bandwidth_usage(options, sslverify, username, pw, host):


def _url(host, path):
    return 'https://' + host + ':9092' + path
