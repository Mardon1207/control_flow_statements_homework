def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    x=0 
    y=0
    if a<0:
        x=x+1
    if b<0:
        x=x+1
    if c<0:
        x=x+1
    if a>0:
        y=y+1
    if b>0:
        y=y+1
    if c>0:
        y=y+1
    if x<y:
        l=str("there are a lot of positive numbers")
    if x>y:
        l=str("there are a lot of negative numbers")
    return l
a=int(input())
b=int(input())
c=int(input())
print(main(a,b,c))   