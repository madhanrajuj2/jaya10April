*** Settings ***
Documentation    Suite description
Library  InterView1.py
*** Variables ***
*** Test Cases ***
Test suit -Validate 1 - 10
    [Documentation]  Validating InterView1.py by supplying values to check Fizz or Buzz is displayed1
    [Tags]  InterView.py validate1
    validating_given_values  10     Buzz
    validating_given_values  6      Fizz
    validating_given_values  1      Fizz

Test suit 2 - Validate 11 - 20
    [Documentation]  Validating InterView1.py by supplying values to check Fizz or Buzz is displayed2
    [Tags]  InterView.py validate2
    validating_given_values  15  FizzBuzz
    validating_given_values  20  Buzz
    validating_given_values  12  Fizz

Test suit 3 - validate 21 - 100
    [Documentation]  Validating InterView1.py by supplying values to check Fizz or Buzz is displayed3
    [Tags]  InterView.py validate3
    validating_given_values  21  Fizz
    validating_given_values  100  Buzz
    validating_given_values  30    Fizz

*** Keywords ***
validating_given_values
    [Arguments]  ${valueToValidate}     ${strDisplay}
    ${gen_Values}=  numEval     ${valueToValidate}
    should contain      ${gen_Values}   ${strDisplay}

