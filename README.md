# volvo-campaign
This is a project to test the Volvo Campaign on Car Safety

## Test Framework
The test framework is designed using Pytest & Selenium. 

The test framework is having the below parts:
1. **features** - This folder is having the feature files. Each feature file is designed for individual page and there are different scenario for testing each page sections.
2. **map** - The page map is used for saving the locators. Each file is created for individual pages/apps. There are different classes for each page sub section to differentiate between each other.
3. **steps** - The steps folder is having all the necessary files for executing the test cases. **common_actions** is having the reused components. **conftest** is having the set up and teardown files. **custom_waits** is having the resuable explicit wait components. **drivers** houses the declaration of remote webdriver instance. **page_map** is used for linking the page locator file(map) to the corresponding step implementation in features. **test_001_campaign.py** is having the pytest step implementation of the features.
4. **docker-compose.yml** - This file is used for listing and creating the docker services.
5. **Dockerfile** - The Dockerfile is used for creating a docker image with the project files and the pytest and selenium executables.
6. **requirements.txt** - This file is used for tracking all the required executables for executing the script.

## Test Execution
The test can be executed with few simple steps.
1. Download docker to the system in which execution is being done.
2. Clone the repository.
3. Open terminal and hit `docker-compose up`

## Parallel Execution
Parallel execution can be achieved using the `pytest -n=2`.
If the number of parallel executions has to be increased, we have to use increase the value of n.

## Reporting
The report is already created in the docker and pytest execution by using the command `pytest -v`.
The report can be even improved by using the following command `pytest --html=report.html`.

##Further Improvements
1. Visual regression can be implemented using `PhantomJS` library.