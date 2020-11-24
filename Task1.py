def user_words(function):
    print(function().split())

@user_words
def entered_string():
    return input('Print something:  ')



