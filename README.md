# RobotFramework ConnectALL Library

## Description
ConnectALL [Robot Framework](http://www.robotframework.org) listner library that provides listeners for your robot tests to report back the execution result to your favorite test management tools using ValueOps ConnectALL a product of Broadcom ValueOps solution. 


## Installation

```
pip install git+https://github.com/connectall/robotframework-connectall-library.git
```

## Documentation

See library documentation on [GitHub](https://github.com/connectall/robotframework-connectall-library/tree/main/docs)

## Library Usage

1. Import ConnectAllLibrary

   ```robot
   *** Settings ***
   Library    ConnectAllLibrary    url=http:\\server    user=user@domain.com    api_key=key_here    project=My Project    plan=Test Plan    run_name=MyDailyRun    config={'OS':'Windows', 'Browser':'Chrome'}    prefix=C

   ```

2. Mark Robot Framework tests with tag containing test case ID. Case IDs are the ones that are unique correlation-id test management system. They looks like the follofing C# (e.g. T12345).


## Examples

### Single tag example

```robotframework
*** Test Cases ***
Test With Test Rail tag
    [Tags]    C1    dummy    owner-johndoe
    Log    Hello, world!
```

### Multiple tags example

```robotframework
*** Test Cases ***
Test With Test Rail tag
    [Tags]    C1    C2    C45233    dummy    owner-johndoe
    Log    Hello, world!
```

## Usage with CI systems

// TODO
