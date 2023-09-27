# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in output, -V stands for more info metadata
# you can run specific file with py.text <filename>
# you can mark(tag) tests @pytest.mark.somke and then run with -m
# To skip the test case @pytest.mark.skip as skip
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases- conftest file to generalize
# fixtures and make it available to all text case
# datadriven and parametrization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


#@pytest.mark.smoke
#@pytest.mark.skip
#@pytest.mark.xfail
#def test_firstProgram():
#    print("Hello")


# pytest -s -v
# pytest -k File_Name -s -v
# pytest -k Function_name -s -v
# pytest -m pytest.mark.name -s -v


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield                                # used to run post
    print("I will executed last")

def test_fictureDemo(setup):
    print("i will execute steps in fixtureDemo method")
