*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Login After Successful Registration
    Set Username  zzz
    Set Password  zzzzz123
    Set Password confirmation  zzzzz123
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Logout User
    Logout Should Succeed
    Set Username  zzz
    Set Password  zzzzz123
    Login User
    Login Should Succeed

Login After Failed Registration
    Set Username  zzz
    Set Password  zzzzz123
    Set Password confirmation  zzzzz1234
    Submit Credentials
    Register Should Fail With Message  Password doesn't match
    Go To Login Page
    Set Username  zzz
    Set Password  zzzzz123
    Login User
    Login Should Fail With Message  Invalid username or password

Register With Valid Username And Password
    Set Username  zzz
    Set Password  zzzzz123
    Set Password confirmation  zzzzz123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  zz
    Set Password  zzzzz123
    Set Password confirmation  zzzzz123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  zzz
    Set Password  zzzzz12
    Set Password confirmation  zzzzz12
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters

Register With Valid Username And Invalid Password
    Set Username  zzz
    Set Password  zzzzzzzz
    Set Password confirmation  zzzzzzzz
    Submit Credentials
    Register Should Fail With Message  Password can't consist of characters only

Register With Nonmatching Password And Password Confirmation
    Set Username  zzz
    Set Password  zzzzz123
    Set Password confirmation  zzzzz1234
    Submit Credentials
    Register Should Fail With Message  Password doesn't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  zzzzz123
    Set Password confirmation  zzzzz123
    Submit Credentials
    Register Should Fail With Message  Username not available, choose another one

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Logout Should Succeed
    Login Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Login User
    Click Button  Login

Logout User
    Click Button  Logout

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}