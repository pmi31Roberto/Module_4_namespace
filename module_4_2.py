def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    return inner_function()


# inner_function() не работает
test_function()
