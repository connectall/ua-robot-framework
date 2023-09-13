# Robot framework listener to read the test results and send it to ConnectALL
# Uses the TestResult datastructure to hold the test status

# Path: connectall-robotframework-listener/RobotListener.py
import requests

class RobotListener:
    """
        RobotListener class to read the test results and send it to ConnectALL
    """
    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password
        self.session = requests.Session()

    # a method to capture the end of test execution
    def end_test(self,name,attrs):
        # Capture the dynamic attributes like test name, status, message
        test_name = attrs['longname']
        test_status = attrs['status']
        test_message = attrs['message']
        # Create a TestResult object
        self.test_result = TestResult(test_name,test_status,test_message)


class TestResult:
    """
        TestResult datastructure to hold the test status
    """
    def __init__(self,name,status,message):
        self.name = name
        self.status = status
        self.message = message