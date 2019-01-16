def is_uppercase(x):
    words = x.split("_")
    for word in words:
        if word == word.upper():
            print(True)
        else:
            print(False)



