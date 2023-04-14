def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==0:
        l=str("positive even number")
    if a>0 and a%2==1:
        l=str("positive odd number")
    if a<0 and a%2==0:
        l=str("negative even number")
    if a<0 and a%2==1:
        l=str("negative odd number")
    if a==0:
        l=str("the number is zero")
    
    return l
a=int(input())
print(main(a))