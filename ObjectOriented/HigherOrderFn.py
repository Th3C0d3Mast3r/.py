def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text=func("The Word")
    print(text)

hello(loud)

# this was in short- in hellow we passed the function loud.
# the loud() in hello function went like- text=func("The Word")
# thus, it passed string="The Word" to the upper function, which returned all caps of that string
# and we printed that

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))


'''THUS, HIGH ORDER FUNCTIONS ARE SOMETHING THAT ACCEPT FUNCTION AS PARAMETERS, OR RETURN FUNCTIONS'''
