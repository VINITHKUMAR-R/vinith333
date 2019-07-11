x=input()
a=["a","e","i","o","u"]

if(x>= 'a'and x<= 'z'):
    if x in a:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
