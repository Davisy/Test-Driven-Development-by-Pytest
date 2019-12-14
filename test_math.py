import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5,"Test failed"

def test_square():
   num = 7
   assert 7*7 == 40,"Test failed, 7*7 != 40"

def test_equality():
   assert 10 == 11, "Test failed they are not equal"