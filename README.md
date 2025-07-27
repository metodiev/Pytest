# Pytest
This repository demonstrates the use of Pytest for testing Python applications. It includes sample test cases, fixtures, test organization patterns, and custom configurations to provide a complete testing framework. Ideal for learning, practicing, or using as a template for other projects.

## Install Dependecies

- Navigate to the root folder of the project and run one of the below commands

```bash
pip3 install -r requirements.txt --break-system-packages

```

or 

```bash
pip install -r requirements.txt --break-system-packages

```

##  Examples

###  Basics
-  Basic assert
-  Parametrize
-  Skipping tests
-  Marking tests
-  Asserting exceptions

###  Fixtures
-  Simple fixture
-  Fixture with teardown
-  Yield fixtures
-  Scope (module, session)
-  Autouse fixtures

### Test Structure
-  conftest.py
-  Nested test directories
-  Using pytest.ini

###  Advanced Features
-  Custom markers
-  Monkeypatching
-  Mocking with unittest.mock
-  Pytest-Django / Pytest-Flask integration
-  Capturing stdout/stderr

###  Plugins
-  pytest-xdist (parallel tests)
-  pytest-cov (coverage)
-  pytest-html (HTML reports)
-  Writing a custom plugin


# Pytest Example Suite

This repository contains **100 example pytest scripts** designed to cover a wide range of pytest features and best practices, organized by topic from basics to advanced usage.

---

## Overview

These examples serve as a practical guide to mastering pytest, demonstrating everything from simple assertions to advanced plugin development and integration.

---

## Covered Topics

### Basics

- **Basic asserts:** Writing simple tests using assert.
- **Parametrization:** Using @pytest.mark.parametrize to run tests with multiple data sets.
- **Skipping tests:** Skipping tests conditionally or unconditionally with @pytest.mark.skip, skipif, and pytest.skip().
- **Marking tests:** Custom and built-in markers for categorizing and selecting tests.
- **Asserting exceptions:** Using pytest.raises to assert that exceptions are properly raised.
- **Fixtures:**
  - Simple fixtures for setup.
  - Fixtures with teardown using request.addfinalizer.
  - Yield fixtures for cleaner setup/teardown.
  - Fixtures with various scopes: function, module, session.
  - Autouse fixtures to apply fixtures automatically without explicit usage.

---

### Test Structure

- **conftest.py:** Sharing fixtures and hooks across test directories.
- **Nested test directories:** Organizing tests in subfolders and sharing configuration.
- **Using pytest.ini:** Configuring pytest via ini files for markers, addopts, and other settings.

---

### Advanced Features

- **Custom markers:** Defining and using custom markers to categorize tests.
- **Monkeypatching:** Temporarily modifying objects or environment variables in tests.
- **Mocking with unittest.mock:** Using mock to replace parts of the system under test.
- **Pytest-Django / Pytest-Flask integration:** Basic examples showing how to write tests in Django/Flask projects using pytest.
- **Capturing stdout/stderr:** Capturing and asserting console output with capfd and caplog.
- **Plugins:**
  - Usage of pytest-xdist for parallel test execution.
  - Usage of pytest-cov for measuring test coverage.
  - Usage of pytest-html  for generating HTML test reports.
- **Writing a custom plugin:** Minimal example showing how to write and register a custom pytest plugin.

---

## Usage

Run all tests with:

```bash
pytest -v


