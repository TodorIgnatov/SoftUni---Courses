needed_book = input()
counter = 0

while True:
    book = input()
    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    if book == needed_book:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1

