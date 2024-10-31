import pytest
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept, employee_data

def test_get_employees_by_age_range():
    # Test normal case
    result = get_employees_by_age_range(25, 35)
    assert len(result) == 4
    assert all(25 < emp["age"] < 35 for emp in result)
    
    # Test empty range
    result = get_employees_by_age_range(0, 20)
    assert len(result) == 0
    
    # Test boundary case
    result = get_employees_by_age_range(22, 24)
    assert len(result) == 1
    assert result[0]["name"] == "Mary"

def test_calculate_average_salary():
    # Calculate expected average
    expected_average = sum(emp["salary"] for emp in employee_data) / len(employee_data)
    
    # Test actual function
    result = calculate_average_salary()
    assert result == expected_average
    assert result == 60166.67  # Based on the given data (rounded to 2 decimal places)

def test_get_employees_by_dept():
    # Test Marketing department
    marketing_employees = get_employees_by_dept("Marketing")
    assert len(marketing_employees) == 2
    assert all(emp["department"] == "Marketing" for emp in marketing_employees)
    
    # Test Engineering department
    engineering_employees = get_employees_by_dept("Engineering")
    assert len(engineering_employees) == 2
    assert all(emp["department"] == "Engineering" for emp in engineering_employees)
    
    # Test case insensitive
    sales_employees = get_employees_by_dept("sales")
    assert len(sales_employees) == 2
    assert all(emp["department"].lower() == "sales" for emp in sales_employees)
    
    # Test non-existent department
    non_existent = get_employees_by_dept("HR")
    assert len(non_existent) == 0