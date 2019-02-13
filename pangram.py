import string
universal_set=string.ascii_lowercase
print("Enter sentence")
sentence=input().replace(" ","")
sub = set(universal_set)-set(sentence)
print((sorted(list(sub))))