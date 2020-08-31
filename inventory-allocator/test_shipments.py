from shipments import main

# Order can be shipped using one warehouse
def test_case1():
    testInput = '{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]'
    assert main(testInput) == '[{ owd: { apple: 1 } }]'

# Order can be shipped using multiple warehouses
def test_case2():
    testInput = '{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]'
    assert main(testInput) == '[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]'
    '''
    I actually think a more appropriate output would be 
        '[{ owd: { apple: 5 }}, { dm: { apple: 5 } }]' 
    since warehouse 'owd' appears before warehouse 'dm' in the input...
    '''

# Order cannot be shipped because there is not enough inventory v1
def test_case3():
    testInput = '{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]'
    assert main(testInput) == '[]'

# Order cannot be shipped because there is not enough inventory v2
def test_case4():
    testInput = '{ apple: 2 }, [{ name: owd, inventory: { apple: 1 } }]'
    assert main(testInput) == '[]'

def test_case5():
    testInput = '{ apple: 10 }, [{ name: case5a, inventory: { apple: 5 } }, { name: case5b, inventory: { apple: 6 } }]'
    assert main(testInput) == '[{ case5a: { apple: 5 } }, { case5b: { apple: 5 } }]'

def test_case6():
    testInput = '{ apple: 10 }, [{ name: case6a, inventory: { apple: 11 } }, { name: case6b, inventory: { apple: 2 } }]'
    assert main(testInput) == '[{ case6a: { apple: 10 } }]'

def test_case7():
    testInput = '{ apple: 5, banana: 5, orange: 5 }, [{ name: case7a, inventory: { apple: 5, banana: 5 } }, { name: case7b, inventory: { apple: 5, orange: 5 } }, { name: case7c, inventory: { apple: 1, banana: 2, orange: 3, dragonfruit: 4 } }]'
    assert main(testInput) == '[{ case7a: { apple: 5 } }, { case7a: { banana: 5 } }, { case7b: { orange: 5 } }]'

def test_case8():
    testInput = '{ apple: 1, banana: 2, carrot: 3, strawberries: 4, oatmeal: 5, peanut butter: 6 }, [{ name: case8a, inventory: { apple: 2 } }, { name: case8b, inventory: { banana: 1 } }, { name: case8c, inventory: { carrot: 3 } }, { name: case8d, inventory: { strawberries: 4 } }, { name: case8e, inventory: { oatmeal: 5 } }, { name: case8f, inventory: { peanut butter: 6 } }]'
    assert main(testInput) == '[]'
