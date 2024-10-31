import price_info

def test_total_cost_shopping(capsys):
    # Run the function and capture the print output
    price_info.total_cost_shopping()
    captured = capsys.readouterr()
    output = captured.out.strip()
    
    # Calculate the expected total manually
    expected_total = sum(
        price_info.price_list[fruit] * price_info.quantity_list.get(fruit, 0)
        for fruit in price_info.price_list
    )
    
    # Print expected and actual output for debugging
    print(f"Expected output: total cost = {expected_total}")
    print(f"Actual output: {output}")

    # Check if the output matches the expected total cost
    assert output == f"total cost = {expected_total}", f"Expected {expected_total}, but got {output}"

def test_cost_of_fruits(capsys):
    # Test cost_of_fruits for a specific fruit (e.g., apple with quantity 10)
    fruit = 'apple'
    quantity = 10
    price_info.cost_of_fruits(fruit, quantity)
    captured = capsys.readouterr()
    output = captured.out.strip()

    # Calculate the expected cost for this case
    expected_cost = price_info.price_list[fruit] * quantity
    expected_output = f"cost of {quantity} {fruit} = {expected_cost}"

    # Print expected and actual output for debugging
    print(f"Expected output: {expected_output}")
    print(f"Actual output: {output}")

    # Check if the output matches the expected cost
    assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"
