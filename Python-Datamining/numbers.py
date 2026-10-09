# Bai 1
# with open('number.txt', 'r') as file:
#     content = file.readline()
# number_as_strings = content.split(',')
# print('Cac so trong file: ', number_as_strings)
# numbers = map(int, number_as_strings)
# total = sum(numbers)
# print('Tong cac so:', total)

#Bai 2
with open('number2.txt', 'r') as file:
    content = file.readline()
    number_as_strings = content.split(',')
    numbers = list(map(int, number_as_strings))

    max_number = max(numbers)
    min_number = min(numbers)

with open('output.txt', 'w') as file:
    file.write(f"So lon nhat: {max_number}\n")
    file.write(f"So nho nhat: {min_number}\n")
print("Da ghi ket qua vao file output.txt")