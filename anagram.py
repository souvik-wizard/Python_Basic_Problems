string1 = "Listen"
string2 = "Silent"

string1 = string1.lower()
string2 = string2.lower()

leng1=len(string1)
leng2=len(string2)


if( leng1 == leng2):
   
    sorting1=sorted(string1)
    sorting2=sorted(string2)

    if sorting1 == sorting2:
        print("They are anagram")
    else:
        print("They are not anagram")
else:
    print("Not matching")