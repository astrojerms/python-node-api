import requests

def get_all_xfer_info(options, sslverify, username, pw, host):
    return requests.get(_url(host,'/ops/transfers'), verify=sslverify, params=options, auth=(username, pw))

def get_xfer_info(options, transferid, sslverify, username, pw, host):
    return requests.get(_url(host,'/ops/transfers/' + transferid), verify=sslverify, params=options, auth=(username, pw))

# requires activity_bandwidth_logging to be enabled on transfer server
def get_bandwidth_usage(options, sslverify, username, pw, host):
    return requests.get(_url(host,'/ops/transfers/bandwidth'), verify=sslverify, params=options, auth=(username, pw))

def cancel_transfer(options, transferid, sslverify, username, pw, host):
    return requests.request("CANCEL", _url(host,'/ops/transfers/' + transferid), verify=sslverify, params=options, auth=(username, pw))

def _url(host, path):
    return 'https://' + host + ':9092' + path
