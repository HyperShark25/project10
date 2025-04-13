#    newString = [i.upper() if not i.upper() else i.lower() for i in s]
#    newString = ''.join(newString)
#    print(newString)

def is_spongecase(text):
    letterIndex = 0
    for i in text:
        if i.isalpha():
            if letterIndex % 2 == 0 and not i.isupper():
                print(True)
            else:
                print(True)
        else:
            letterIndex += 1
    print(True)

is_spongecase("HeLlo WoRlD!")
