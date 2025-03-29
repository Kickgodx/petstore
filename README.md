# Petstore API pytest tests

This repository contains a set of tests for the Petstore API using pytest.

## Installation

1. Clone the repository
2. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Running the tests

To run the tests, use the following command:

```bash
pytest
```

## Parallel execution with pytest-xdist

To run the tests in parallel, use the following command:

```bash
pytest -n <number_of_workers>
```

## Allure report

Pytest generates an Allure report after running the tests. To view the report, use the following command:

```bash
allure serve allure-results
```

## Test cases

The test cases are located in the `tests` directory. Pull of the test cases are located in the file.

## Structure

The repository has the following structure:

- tests: Contains the test cases
- src: Contains the functions that are used in the tests (api, helpers, assertions, etc.)
- allure-results: Contains the Allure report results
- requirements.txt: Contains the required packages
- pytest.ini: Contains the pytest configuration
- README.md: Contains the repository description
- .gitignore: Contains the files and directories that are ignored by Git
- docker-compose.yml: Contains the Docker Compose configuration
- Dockerfile: Contains the Docker configuration

## Docker

To run the tests in a Docker container, use the following command:

```bash
docker-compose up
```

or

```bash
docker build -t petstore-api-tests .
docker run petstore-api-tests
```