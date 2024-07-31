# slicing in strings is created to make substrings

name="My Full Name"
substring1=name[0:5]                                        # this is equivalent to create a substring from index 0 to (5-1)

print(substring1)

# there is even a shorthand way for this
substringFromStart=name[:8]
substringToEnd=name[3:]

print("This is the substring from the start: "+substringFromStart)
print("This is the substring till the end: "+substringToEnd)

# added to this, the python language comes with a new feature
# the actual function goes like this:- name[start:end:step]
# so the step actually means counting one character, the next character chosen is adjacent or after skipping
# on base, the step is set to 1
# if someone writes 2 or 3, then we see that. Look below

string1="ALEXANDARA"
string2=string1[0:9:2]
print("The Actual String is "+string1+" and due to Function, we see this: "+string2)    

test1="LOLSIKEhello"
print(test1[3::2])

# and we can even RESVERSE a String directly using Indexing
normalName="THIS IS THE NORMAL NAME"
reversedName=normalName[::-1]                               # the -1 shows we are using reversing
print("After Reversing-we get:- "+reversedName)

# NOW, APART FROM INDEXING, THERE IS EVEN SLICING FUNCTION

websiteURL="https://google.com/god-of-war"
endingIndex=websiteURL.find('.')                            # we use this to get the end of web name
slicing=slice(8,endingIndex,1)                              # in short, it sets the easy bounds

webName=websiteURL[slicing]
print(webName)