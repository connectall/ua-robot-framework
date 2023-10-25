import datetime
import logging as log
# from robot.api import logger as log
from ConnectAllListener import ConnectAllListener
from ConnectAllListener import TestResult as Result

def test_parseTagAttributes():
    connectAllListener = ConnectAllListener("connectallConfig.toml")
    tags = ["caseId=T12345", "setId=TS45678", "type=Fuctional", "description=Test case 1 long description", "name=Test Case 1"]
    attributes = connectAllListener.parseTagAttributes(tags)
    assert attributes['caseId'] == "T12345"
    assert attributes['type'] == "Fuctional"
    assert attributes['name'] == "Test Case 1"
    assert attributes['description'] == "Test case 1 long description"

def test_postTestResult():
    connectAllListener = ConnectAllListener("connectallConfig.toml")
    result = Result("Test Case 1", "setId=TS45678", "PASS", "Test Case 1 passed", testCaseId="T12345", testCaseType="Functional", testCaseDescription="Test case 1 long description")
    response = connectAllListener.postTestResult(result)
    log.info (f"Response: {str(response.json())}")
    assert response.status_code == 201

def test_dateFormatting():
    currentTime = 1528797322
    _date = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%dT%H:%M:%SZ')
    log.info( f"Current date: {str(_date)}")
    log.info( f"Current date: {str(currentTime)}")
    assert _date.startswith("2018-06-12")
