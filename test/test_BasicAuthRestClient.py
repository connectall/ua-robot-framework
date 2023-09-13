import pytest 
import sys
import os
import logging as log
from ConnectAllLibrary.BasicAuthRestClient import BasicAuthRestClient

CONNECTALL_MYSELF_RESOURCE = "/rest/api/myself"
CONNECTALL_CREATE_CONNECTION_RESOURCE = "/rest/api/template/connection"

def test_loadConfig():
    client = BasicAuthRestClient()
    config = client.loadConfig()
    assert config['core']['url'] == "http://10.253.137.224:8080/ConnectAll"

def test_loadConfigProperties():
    client = BasicAuthRestClient()
    config = client.loadConfigProperties("connectallConfig.toml")
    assert config['core']['url'] == "http://localhost:8080/ConnectALL"

def test_formattedResourceUrl():
    client = BasicAuthRestClient()
    formattedUrl = client.formattedResourceUrl(CONNECTALL_MYSELF_RESOURCE)
    assert formattedUrl == "http://10.253.137.224:8080/ConnectAll/rest/api/myself"

def test_doGet():
    client = BasicAuthRestClient()
    response = client.doGet(CONNECTALL_MYSELF_RESOURCE)
    log.error(f"Respnose : {str(response.json())}")
    assert response.status_code == 200

def test_doPost():
    client = BasicAuthRestClient()
    _connection = mockConnection()
    response = client.doPost(CONNECTALL_CREATE_CONNECTION_RESOURCE, _connection)
    data = response.json()
    log.error(f"Respnose : {str(data)}")
    assert response.status_code == 400

def mockConnection():
    data = {}
    return data