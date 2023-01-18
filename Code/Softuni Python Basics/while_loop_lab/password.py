username = input()
password = input()

# data = input()
#
# while data != password:
#     data = input()
#
# print(f"Welcome {username}!")

while True:
    data = input()
    if data == password:
        print(f"Welcome {username}!")
        break