import lab2.bmi as bmi

def test_underweight():
    assert bmi.calculate_bmi(1.7, 50) == -1  

def test_normal_weight():
    assert bmi.calculate_bmi(1.7, 65) == 0  

def test_overweight():
    assert bmi.calculate_bmi(1.7, 80) == 1 