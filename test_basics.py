import pytest

# mark set for each function

@pytest.mark.set1
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed"


@pytest.mark.set2
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"

@pytest.mark.set3
def test_file1_method3():
	x = "77"

	assert x == 77,'failed to identify integer'




