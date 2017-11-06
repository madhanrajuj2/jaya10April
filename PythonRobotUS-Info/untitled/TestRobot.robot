*** Settings ***
Documentation	Testing Robot features
....
....		The _data-driven_ style works well when you need to repeat
....		the same workflow multiple times.
....
Test Template	Testing

*** Variables ***
${listVar}
${a}    3
${b}    02
${c}    5
*** Test Cases ***

*** Keywords ***
Testing
	[Documentation]	Test used to understand Robot
	${listVar}=     create list  ${a}   ${b}    ${c}
	log many  Testing123    ${listVar}