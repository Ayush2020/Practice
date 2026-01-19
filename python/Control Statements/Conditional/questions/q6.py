# wap to check thst the given program language is present in the give list  of prog language

lang = input("Enter your language: ")
collection = input("Enter the language collection:")


if lang.lower() in collection.lower():
    print(lang, "it is programming language")


