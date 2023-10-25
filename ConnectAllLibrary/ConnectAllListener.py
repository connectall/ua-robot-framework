# Robot framework listener to read the test results and send it to ConnectALL
# Uses the TestResult datastructure to hold the test status

# Path: connectall-robotframework-listener/RobotListener.py
import re
import datetime
from BasicAuthRestClient import BasicAuthRestClient
from typing import Any, Dict, List, Optional
from robot.api import logger as log

TESTCASE_ID_TAG = 'caseId'
TESTSET_ID_TAG = 'setId'
TESTCASE_NAME_TAG = 'name'
TESTCASE_TYPE_TAG = 'type'
TESTCASE_DESCRIPTION_TAG = 'description'
CONNECTALL_DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

class ConnectAllListener:
    """
        ConnectAllRobotListener class to read the test results and send it to ConnectALL
    """
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self,configFile = "connectallConfig.toml"):
        self.configFile = configFile
        self.client = BasicAuthRestClient(configFile)
        
    # a method to capture the end of test execution
    def end_test(self,name,attrs):
        # Capture the dynamic attributes like test name, status, message
        log.info(f"attrs: {str(attrs)}")
        test_id = attrs['id']
        test_name = attrs['longname']
        test_status = attrs['status']
        test_message = attrs['message']
        # Parse the tags to get the dynamic attributes
        dynamic_attributes = self.parseTagAttributes(attrs['tags'])
        caseid = dynamic_attributes[TESTCASE_ID_TAG]
        setid = dynamic_attributes[TESTSET_ID_TAG]
        type = dynamic_attributes[TESTCASE_TYPE_TAG]
        description = dynamic_attributes[TESTCASE_DESCRIPTION_TAG]

        # Create a TestResult object
        test_result = TestResult(test_id,test_name,test_status,test_message,testCaseId=caseid,testSetId=setid,testCaseType=type,testCaseDescription=description)
        self.postTestResult(test_result)

    # a method to post the test result to ConnectALL
    def postTestResult(self,testResult):
        """
            Post the test result to ConnectALL
        """
        apiKey = self.client.connectAllApiKey()
        automationname = self.client.automationName()
        # Set the api key and automation name in the url
        _connectallPostRecordResource = f"/connectall/api/2/postRecord?apikey={apiKey}&appLinkName={automationname}"
        # _postRecordEndpoing = self.client.formattedResourceUrl(_connectallPostRecordResource)
        
        # Create a payload
        payload = self.createPayload(result=testResult)
        log.info(f"Post record endpoint: {_connectallPostRecordResource} with paylod {payload}")

        # Post the payload to ConnectALL
        response = self.client.doPost(_connectallPostRecordResource, payload)
        log.info(f"Request failed with status code: {response.status_code}" )

        # Check if the request was successful (200 status code)
        if response!= None and response.status_code == 201:
            data = response.json()
            log.info(f"Response data: {str(data)}" )
        else:
            log.error(f"Request failed with status code: {response.status_code} with {str(response.json())}" )
        # return the response object back to the caller
        return response
    
    @staticmethod
    def createPayload(result):
        """
            Convert the test result to a json payload
        """
        payload = {
            "fields": {
                "id": result.uniqueId,
                "runStatus": result.runStatus,
                "runDate": result.runDate,
                "message": result.message,
                "testCaseName": result.name,
                "testCaseId": result.testCaseId,
                "testSetId": result.testSetId,
                "testCaseType": result.testCaseType,
                "testCaseDescription": result.testCaseDescription
            }
        }
        return payload
    
    @staticmethod
    def parseTagAttributes(tags: List[str]) -> Dict[str, Optional[str]]:
        """ Get dynamic attributes from robot framework's tags.

        *Args:* \n
            _tags_ - list of tags.

        *Returns:* \n
            Dict with attributes.
        """
        attributes = dict()
        matchers = [TESTCASE_ID_TAG, TESTCASE_NAME_TAG, TESTCASE_TYPE_TAG, TESTCASE_DESCRIPTION_TAG]
        for matcher in matchers:
            for tag in tags:
                match = re.match(matcher, tag)
                if match:
                    split_tag = tag.split('=')
                    tag_value = split_tag[1]
                    attributes[matcher] = tag_value
                    break
                else:
                    attributes[matcher] = None
        return attributes
    
class TestResult:
    """
        TestResult datastructure to hold the test status
    """
    def __init__(self,id,name,status,message,testCaseId=None,testSetId=None,testCaseType=None,testCaseDescription=None):
        self.id = id
        self.name = name
        self.runStatus = status
        self.message = message
        self.testCaseId = testCaseId
        self.testSetId = testSetId
        self.testCaseType = testCaseType
        self.testCaseDescription = testCaseDescription
        self.runDateInMillis = datetime.datetime.now()
        # create a unique id and set it to id field
        self.uniqueId = self.createUniqueId()
        # set the run date
        self.runDate = self.createRunDate()
    
    def createUniqueId(self):
        """
            Create a unique id for the test result as a concatenation of test case id and current timestamp
        """
        return f"{self.id}_{self.testCaseId}_{str(self.runDateInMillis.timestamp())}"
    
    def createRunDate(self):
        """
            Formats the runDate to yyyy-MM-dd'T'HH:mm:ss.SSS
        """
        # format the runDate to yyyy-MM-dd'T'HH:mm:ss.SSS
        return self.runDateInMillis.strftime(CONNECTALL_DATE_FORMAT)
    
