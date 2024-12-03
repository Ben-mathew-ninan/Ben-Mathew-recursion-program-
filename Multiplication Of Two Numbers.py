def multiply_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply_numbers(n1,n2-1)
print(multiply_numbers(5,4))