# Inspection REST API - Test Plan

* [Introduction](#introduction)
* [Objective and tasks](#objective-and-tasks)
* [Scope](#scope)
  * [In scope](#what-will-be-tested)
  * [Out of scope](#what-will-not-be-tested)
* [Entry criteria](#entry-criteria)
* [Exit criteria](#exit-criteria)
* [Environment](#environment)
  * [Hardware requirements](#hardware-requirements)
  * [Software requirements](#software-requirements)
* [Test cases](#test-cases)
* [Cross-functional impact](#cross-functional-impact)
* [Automation](#automation)
* [Code coverage](#code-coverage)
* [Unit testing cases and logs](#unit-testing-cases-and-logs)
* [Schedule](#schedule)
* [Risks/Assumptions](#risksassumptions)
* [Review comments/Approvals](#review-commentsapprovals)
* [Revision history](#revision-history)

## Introduction
Inspect api is designed to find potential sensitive information in the content. 

## Objective and tasks
### Objective
Main objective of this test plan is to describe the scenarios to be tested and elaborate test design
### Tasks
* prepare test scenarios
* design test data
* automate test case execution and test data generation
## Scope
### what will be tested
Functional aspects of following features will be validated as part of this testing
* generic field validations of API
* Max Size validations
* results based on inspect configuration
  * infoTypes
  * minLikelihood
  * limits
  * excludeInfoTypes
  * customInfoTypes
  * inspectRuleSet
* true positive, true negative validations for selected infoTypes

### what will not be tested
* performance / scale testing
## Environment
### Hardware requirements
To be updated
### Software requirements
To be updated

## Test cases
test combinations for validating InspectConfig

| Filter Based on infoTypes      |  Filter Based on minLikelihood | Filter Based on limits | maxFindingsPerItem | maxFindingsPerRequest | maxFindingsPerInfoType 
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
|Same as infoType in output|Same as minLikelihood in output|Less than output|More than output|Less than output|
|No filter|No filter|More than output|Less than output|More than output|
|other than the infoType in output|other than the minLikelihood in output|No filter|No filter|No filter|

test combinations for value:
value as string, value as table, value as byteItem (Different encodings)

test data:
| infoType  |  test data | expected results | Comments |
| ----------- | ----------- | ----------- | ----------- |
| CREDIT_CARD_NUMBER| Credit Card Type Credit Card Number American Express 371449635398431 Diners Club 30569309025904 Discover 6011111111111117 JCB 3530111333300000 MasterCard 5555555555554444 Visa 4111111111111111    |  True Positive  |
| CREDIT_CARD_NUMBER| Credit Card Type Credit Card Number American Express 3714-2963-5398-431 Diners Club 3056-9309-224904 Discover 6011-1111-1115-1117 JCB 3530111633300000 MasterCard 5555555565554444 Visa 4111111121111111   | True negative | failing Luhn algorithm |
| email id | laxman.eluri@gmail.com | True Positive   |
| email id | laxman e  this is @myhouse | True negative |   

## Recommended regression
## Cross-functional impact
## Automation
### test data generation automation
To cover the test combinations with minimal set of tests pair-wise test technique can be adopted  
for this purpose a wrapper to generate tests using [microsoft pict](#https://github.com/microsoft/pict) tool need to be developed
### test case automation
Above tests will be automated using python / pytest based API framework

## Code coverage
## Unit testing cases and logs
## Schedule
## Risks/Assumptions
*  
* 
## Review comments/Approvals
## Revision history

| Revision      |  Date | Author/s | Comments |
| ----------- | ----------- | ----------- | ----------- |
| v 0.1| 30-Aug-2021 | laxman eluri | draft |
| | | | |
