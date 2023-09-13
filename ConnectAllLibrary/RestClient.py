#! /bin/python

import logging as log
import json

class RestClient:
    """
        Interface for the RestClient with api methods to be implemented by implementing classes
    """
    # The location of the config file from where to load the properties
    CONFIG_LOCATION = "ConnectAllConfig.json"

    # The type of authentication to be used for the rest api call
    REST_AUTH_TYPE = None

    def __init__(self):
        pass

    def doGet(self, resourceUrl):
        """
            Do a get request to the url
        """
        pass

    def doPost(self, resourceUrl, payload):
        """
            Do a post request to the url
        """
        pass    
    
    def loadConfig(self):
        """
            Load the configuration from the ConnectAllConfig.json file
        """
        with open(self.CONFIG_LOCATION) as json_file:
            data = json.load(json_file)
            return data
