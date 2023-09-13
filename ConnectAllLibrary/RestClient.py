#! /bin/python

import logging as log
import json
import configparser

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
            # convert data to dictionary
            return data
        
    def loadConfigProperties(self, configFile):
        """
            Load the configuration from the configFile
        """
        # load config from file using configparser 
        config = configparser.ConfigParser()
        config.read(configFile)
        # convert config to dictionary
        self.config_dict = {s:dict(config.items(s)) for s in config.sections()}
        return self.config_dict
    
    def connectAllApiKey(self):
        """
            Get the ConnectALL API Key from the config
        """
        return self.config['core']['apikey']
    
    def automationName(self):
        """
            Get the Automation Name from the config
        """
        return self.config['automation']['name']

