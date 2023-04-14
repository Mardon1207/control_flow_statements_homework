def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a//10!=0 and a//10<=9 and a%2==0:
        l=str("two-digit even number")
    if a//10!=0 and a//10<=9 and a%2==1:
        l=str("two-digit odd number")
    if a//100!=0 and a//100<=9 and a%2==0:
        l=str("three-digit even number")
    if a//100!=0 and a//100<=9 and a%2==1:
        l=str("three-digit odd number")
    return l
a=int(input())
print(main(a))