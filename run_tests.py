import os
import pytest
import sys

if __name__ == '__main__':
    print('Tests are running. Please, wait.\nResults will be published to results.txt')
    sys.stdout = open('results.txt', 'w')

    PYTEST_PARAMS = os.getenv('PYTEST_PARAMS')
    PATH_TO_TESTS = 'tests/'
    PATH_TO_PYTEST_OUTPUT = 'test_results'

    pytest.main(args=['-v', '-s',
                      PATH_TO_TESTS,
                      '--alluredir=' + PATH_TO_PYTEST_OUTPUT,
                      '-m={}'.format(PYTEST_PARAMS if PYTEST_PARAMS else '')])
    sys.stdout.close()
    sys.stdout = sys.__stdout__
