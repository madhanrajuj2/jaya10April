*** Settings ***
Library                     RequestsLibrary
Library                     Collections
Library                     XML  use_lxml=True
Force Tags                  REST


*** Variables ***
${SERVICE_ROOT}  http://ip.jsontest.com/
${SERVICE_NAME}  testing

*** Keywords ***
json_property_should_equal
    [Arguments]  ${json}  ${property}  ${value_expected}
    ${value_found} =    Get From Dictionary  ${json}  ${property}
    #"Get from dictionary" is a Robot collection function --https://bulkan.github.io/robotframework-requests/#Get%20Request
    ${error_message} =  Catenate  SEPARATOR=  Expected value for property "  ${property}  " was "  ${value_expected}  " but found "  ${value_found}  "
    #http://robotframework.org/robotframework/latest/libraries/BuiltIn.html#Catenate
    Should Be Equal As Strings  ${value_found}  ${value_expected}  ${error_message}    values=false

*** Test Cases ***
Example REST JSON
    [Documentation]  Testing functionality of Robot
  Create session  ${SERVICE_NAME}  ${SERVICE_ROOT}
  #https://bulkan.github.io/robotframework-requests/#Get%20Request  --- info on "Create session"
  #info on "Create session" https://github.com/bulkan/robotframework-requests     --require or else we will get "testing" is not defined
  ${headers}=  Create Dictionary  Content-Type=application/json  Accept=application/json
  ${result}=  Get Request  ${SERVICE_NAME}  ${SERVICE_ROOT}  headers=${headers}
  Should Be Equal  ${result.status_code}  ${200}
  Log  ${result.content}
  ${json}=    To Json    ${result.content}
  #log many  loggingJson   ${json}
  ${pp}=  To Json  ${result.content}  pretty_print=True
  Log  ${pp}
  json_property_should_equal  ${json}  ip  2605:6000:8b48:c000:943a:63d7:48b1:2fea