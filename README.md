
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

* Result of an entire run of pipeline
&nbsp;
  <img src="screenshots/pipeline-result-terraform.png" width=600>
&nbsp;

* Entire pipeline after run
&nbsp;
  <img src="screenshots/EntirePipeline-successfulrun.png" width=600>
&nbsp;

* Result overview of integration tests with Postman
&nbsp;
  <img src="screenshots/PostmanTestreport-MetricsDataValidation.png" width=600>
&nbsp;

&nbsp;
  <img src="screenshots/PostmanTestreport-MetricsRegression.png" width=600>
&nbsp;

* detailed testcases postman in the detailed pipeline view (outputs)
&nbsp;
  <img src="screenshots/Postman-RegressionTest.png" width=600>
&nbsp;

* Results in the detailed pipeline view (outputs)
&nbsp;
  <img src="screenshots/Postman-publishedTestresults-.png" width=600>
&nbsp;


* UItests with selenium and python -- results
&nbsp;
  <img src="screenshots/UItests-results-selenium-Pipelineslogs.png" width=600>
&nbsp;


* Endurance and Stress tests with jmeter - successful run pipeline
&nbsp;
  <img src="screenshots/jmeter-standaloneTest-enduranceTest.png" width=600>
&nbsp;

* Jmeter testresults report
&nbsp;
  <img src="screenshots/2021-03-11 15_25_21-ApacheJMeterDashboard-endurancetest.png" width=600>
&nbsp;

&nbsp;
  <img src="screenshots/2021-03-11 15_26_26-ApacheJMeterDashboard-stresstest.png" width=600>
&nbsp;

&nbsp;
  <img src="screenshots/2021-03-11 15_27_48-ApacheJMeterDashboardStressTest-details.png" width=600>
&nbsp;


* The Alert email from Azure monitoring
&nbsp;
  <img src="screenshots/AzureMonitorAlertbyEmail.png" width=600>
&nbsp;

* The Monitor and the rule
&nbsp;
  <img src="screenshots/AzureMonitorMetrics.png" width=600>
&nbsp;

&nbsp;
  <img src="screenshots/AzureMonitorMetrics.png" width=600>
&nbsp;

* The rule
&nbsp;
  <img src="screenshots/AlertruleMicrosoftAzure.png" width=600>
&nbsp;


* The Alerts
&nbsp;
  <img src="screenshots/MicrosoftAzure-Alerts.png" width=600>
&nbsp;

*
