
#Ternary Conditionals
condition = True

if condition:
    x= 1
else:
    x = 0

x =1 if condition else 0

print(x)
#Underscore Placehders
num1= 10_000_000_000
num2 = 100_000_000
total = num1+num2
print(total)
#Context Managers


with open('input.txt', 'r') as f:
    file_content = f.read()
words = file_content.split(' ')
print(words)
words_count = len(words)
print(words_count)



