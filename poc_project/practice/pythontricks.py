import my_module

print(my_module.external_func())
print(my_module._internal_func())
#_internal_func()
#
# class Test:
#     def __init__(self):
#         self.foo = 11
#         self._bar = 23
#
# t = Test()
# print(t.foo)
# t._bar


def greet(name, question):
    return f'Hello {name} ! How is {question}'


print(greet('Bob','going'))


def yell(text):
    return text.upper() + '!'


print(yell('hello'))

bark = yell
print(yell('woof'))

print(type(bark))

#functions can be stored in data structures
#
# funcs = [bark, str.lower, str.capitalize]
# print(funcs)

#Functions Can Be Passed to Other Functions
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

print(greet(bark))
#Python map() function
print(list(map(bark, ['hello', 'hey', 'hi'])))
