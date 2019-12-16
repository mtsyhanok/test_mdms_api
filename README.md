MDMS API Tests
==================
Instructions how to run tests on local machine.


## Requirements:
* Python 3.7.2+
* ChromeDriver (for web tests only)
* Git


## To run tests
1.  Clone repository with tests to local machine:

    ```
    git clone https://github.com/mtsyhanok/test_mdms_api.git
    ```

2. Open command line (Windows Command Prompt), go to test_mdms_api directory and run command:

    ```
    pip install -r .meta/packages
    ```

    This will install python libraries required by tests.

3. Specify path to ChromeDriver in settigs.py e.g.:

    ```
    WEBDRIVER_PATH = "D:/Chrome/chromedriver"
    ```

4. To start tests run command (from test_mdms_api directory):

    ```
    python run_tests.py
    ```


## Test results
* *Text format*

    Test results in text format will be published to *results.txt* in tests directory.


* *Graphic report*

    Tests store data for graphic report in directory */test_results*.
    To generate report you need to install 'allure command line' (https://docs.qameta.io/allure/#_commandline). Then open allure command line and run command:

    ```
    allure serve {path to test_results directory}
    ```
