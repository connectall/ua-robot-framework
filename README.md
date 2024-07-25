# ua-robot-framework

## Description
ConnectALL [Robot Framework](http://www.robotframework.org) listner library that provides listeners for your robot tests to report back the execution result to your favorite test management tools using ValueOps ConnectALL a product of Broadcom ValueOps solution. 


## Installation

```
pip install git+https://github.com/connectall/robotframework-connectall-library.git
```

## Documentation

See library documentation on [GitHub](https://github.com/connectall/robotframework-connectall-library/tree/main/README.md)

## Usage

### Setup

1. Create a robot test case with the following tags that will be used as dynamic paraters 
* caseId - testcaseId in the test management system
* type - denotes the type of testcase valid values `['Functional','Regression','Performance','Acceptance']`
* name - testcase name custom name other than the original name
* description - details about the testcase

   ```robot
    *** Test Case ***
    Test Case 1
        [Tags]    caseId=T12345     type=Functional     name="Test Case 1"    description="Test case 1 long description"     
        Should Be Equal    RobotShould Be EqualShould Be EqualShould Be Equal    framework
   ```

2. Create a `config.toml` configuration file for ConnectALL settings
    ```robot
    # config.toml - ConnectALL Configuration settings

    [core]
    # ConnectALL POST Record endpoint ex: http://localhost:8090
    url = http://post-service.connectall.broadcom.com
    username = admin
    password = welcome
    apiKey = abcdefgh-1234-5678-90123-ijklmnopqrst

    [automation]
    name = RobotRally
    ```


### Execution

To report the results of the your robot tests back to your test management system execute the tests using `ConnectAllListener`

```sh
$ robot --listener ConnectAllListener:configFile=config.toml test/FirstSuite.robot
```
