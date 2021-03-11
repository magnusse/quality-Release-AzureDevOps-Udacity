
# quality-Release-AzureDevOps-Udacity

## project 3 for the Azure devops nanodegree

This project consists of:
* terraform infrastructure declaration including
 * Service App to host a small web application (fakerestapi)
 * virtual machine (Linux) for hosting a UI tests
* automatedtesting suite for the following TestReports
 * UI test with selenium on python
 * postman integration test
 * jmeter stress and endurance tests

The project is orchestrated by an Azure Devops pipeline YAML file which contructs the interfaces, deploys the software and the tests and finally runs all tests. Please finde screenshots of all relevant infos and results in the screenshot folder.
