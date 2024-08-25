# zip function aggregates from one or more iterable

usernames=["cold-drinks", "peanut butter", "Idli Chutney"]          # this is a list
password=("drowssap", "abc123", "qwerty")                           # this is a tuple


users=dict(zip(usernames, password))                                      # two of them got paired together based on indexing

for key, value in users.items():
    print(key,":",value)

print("")

listNames=["firstname", "secnondname", "thirdname"]
listMonth=["February", "January", "December"]
listNations=("India", "England", "Sri Lanka")

userData=zip(listNames, listMonth, listNations)

for i in userData:
    print(i)

