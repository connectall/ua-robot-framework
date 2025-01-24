#! /bin/python

import logging as log
import requests
import json
import os

from RestClient import RestClient

class BasicAuthRestClient(RestClient):

    def __init__(self,configFile = None) -> None:
        """
            Init function for the RestClient, will load the configuration from the ConnectAllConfig.txt file
        """
        self.REST_AUTH_TYPE = "Basic"
        self.configFile = configFile
        # if configFile is not None then call loadConfigProperties else call loadConfig
        if configFile is not None:
            self.config = self.loadConfigProperties(configFile)
        else:
            self.config = self.loadConfig()
        self.url = self.config['core']['url']
        self.username = self.config['core']['username']
        self.password = self.config['core']['password']
        self.apiKey = self.config['core']['apikey']
                
    def formattedResourceUrl(self, resourceUrl):
        """
            Format the resource url with the url from the config
            by trimming the base url to remove the trailing slash and adding the resource url with a leading slash
        """
        if self.url.endswith('/'):
            self.url = self.url[:-1]
        if not resourceUrl.startswith('/'):
            resourceUrl = '/' + resourceUrl

        log.debug("Formatted url: " + self.url + resourceUrl)
        return self.url + resourceUrl

    def doGet(self, resourceUrl):
        """
            Do a get request to the url
        """
        # Create a session object and set the basic authentication
        session = requests.Session()
        session.auth = (self.username, self.password)
        try:
            # Make a GET request to the API endpoint
            response = session.get(self.formattedResourceUrl(resourceUrl))
            log.info(f"Request failed with status code: {response}" )

            # Check if the request was successful (200 status code)
            if response!= None and response.status_code == 200:
                data = response.json()
                # Do something with the response data
            else:
                log.error(f"Request failed with status code: {response.status_code}" )
            # return the response object back to the caller
            return response
        except Exception as e:
            log.error(e)
            raise e
        
    def doPost(self, resourceUrl, payload):
        """
            Do a post request to the url
        """
        log.debug(f"Posting Payload: {str(payload)} to {resourceUrl}" )
        
        # Create a session object and set the basic authentication
        session = requests.Session()
        session.auth = (self.username, self.password)
        try:
            # Make a POST request to the API endpoint
            response = session.post(self.formattedResourceUrl(resourceUrl), json=payload)

            # Check if the request was successful (200 status code)
            if response.status_code == 200:
                data = response.json()
                log.debug(f"Response data: {str(data)}" )
                return data
            else:
                log.error(f"Request failed with status code: {response.status_code}" )
            
            # return the response back to the caller
            return response
        except Exception as e:
            log.error(e)
            raise e
        
    def __str__(self) -> str:
        return super().__str__()+"\n"+str(self.REST_AUTH_TYPE)
        
    
# check if name is main and execute a get call
if __name__ == '__main__':
    print(os.getcwd())
    restClient = BasicAuthRestClient()
    print(restClient)
