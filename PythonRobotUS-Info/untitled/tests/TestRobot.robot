*** Settings ***
Documentation	Testing Robot features
...
...               The _data-driven_ style works well when you need to repeat
...               the same workflow multiple times.
...
Test Template	MathOp
Library  ../MathOpTest.py
*** Variables ***
${listVar}
${a}    3
${b}    02
${c}    5
*** Test Cases ***
AddOperation                                    10                                                  10
subtraction                                     10                                                  2

*** Keywords ***
#Testing
#	[Documentation]	Test used to understand Robot
#	${listVar}=     create list  ${a}   ${b}    ${c}
#	log many  Testing123    ${listVar}

MathOp
    [Arguments]    ${expression}    ${expected}
    Math Op Query   ${expression}
    Result validate    ${expected}
    ${listVar}=     create list  ${a}  ${b} ${c}
    log many  testingLogMany    ${listVar}}
    #${list1}=   create list  ${a}    ${b}   ${c}
    ${res}=     deleteFpcFromExistingGnf    "url123"    ${listVar}
    log many    jsonlog     ${res}


