import string
lower=string.ascii_lowercase
upper=string.ascii_uppercase
numbers=string.digits
special=string.punctuation
a=input()
def reverse_swap(a):
    result=''
    for i in a:
        if i in lower:
            result+=lower[-lower.find(i)-1]
        elif i in upper:
            result+=upper[-upper.find(i)-1]
        elif i in numbers:
            result+=numbers[-numbers.find(i)-1]
        elif i in special:
            result+=special[-special.find(i)-1]
        else:
            result+=i
    
    return result

print(reverse_swap(a))

