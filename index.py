# # 1 задание
# def greet_people(a, b , c, d):
#     print("hello" + a)
#     print("hello" + b)
#     print("hello" + c)
#     print("hello" + d)

# greet_people("1", "2", "3", "4")
    
       



# 2 задание 
# def count_animals(animals):
#      return sum(animals)

# animals = [True, False, True, True, False, False]
# print(count_animals(animals))  



# # 3 задание
# def check_numbers(numbers):
#     for number in numbers:
#         if number %2 == 0:
#             print(f"{number} - четное")
#         else:
#             print(f"{number} - нечетное")

# numbers_list = [1, 2, 3, 4, 5, 6]
# check_numbers(numbers_list)

# 4 задание 
# def square_numbers(numbers):
#     return [number ** 2 for number in numbers]

# numbers_list = [1, 2, 3, 4,]
# newnumbers_list = square_numbers(numbers_list)
# print(newnumbers_list)  
# 5 задание
# def calculate_score(answers):
#     return sum(answers)


# examen_answers = [True, False, True, True, False,]
# ball = calculate_score(examen_answers)
# print(ball) 

















# my_str = "hello"

# x1 = my_str + "!"
# x2 = f"{my_str}!"
 
# print(len(x1))



# print(X2)
# print(x2.upper())
# print(x2.lower())
# x8 = x2.split()
# print(x8)
# print('--'.join(x8))


# text = 'apple'

# print(text.replace())


# if text.startswith('hel'):
#     print("+")

# if text.endswith("png"):
#     print("-")


# x1 = "hello my friend!"

# # str[start:end:step]

# print(x1[0:5])

# x1 = "Hello my world!"
# print(x1[5:8])


# my_list = ["hi", 10, True, 10, "hello"]
# print(my_list[2])
# print(my_list[0:2])

# my_list.append(20)
# print(my_list)

# my_list.remove(10)
# print(my_list)

# my_list.insert(2, 35)
# print(my_list)

# my_list.pop(2)
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list.extend([1, 2 ,"hi", 10, 20, 1, 1])
# print(my_list.index("hi"))

# my_list.reverse()
# print(my_list)

# print(my_list.count(1))

# my_dict = {"mom": "07804085890899", "friends": "02020202020"}

# print(my_dict.keys())

# print(my_dict.values())

# print(my_dict.items())

# for key, value in my_dict.items():
#     print(f"Ключ: {key,} значение: {value}")








# user_products = ['apple', 'milk', 'banana']

# for i in range(len(user_products) -1):
#     print(user_products[i], user_products[+ 1])



# import random

# print(random.randint(0, 10))



# import turtle

# t = turtle.Turtle()
# for _ in range(9):
#     t.forward(70)
#     t.right(50)

# turtle.done()


# matrix = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9], [1, 3, 4, 5, 7, 1]]

# # matrix[1]
# count = 0

# for row in matrix:
#     print(row)
#     for item in row:
#         if item == 1:
#             count += 1

# print(count)

# y = 11 #Глобальная перем5енная
# x = 9
# x = 7

# def my_function():
#     x = 10
#     print(y)
#     print(x)

# my_function()









x = 15

def outer_fun():
    x = 10

    def inner_fun():
        x = 5
        print(x)

    inner_fun()

outer_fun()




