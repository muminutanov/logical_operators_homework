def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    c=a//100
    b=a//10
    d=a%10
    return((c+b+d)%2==1)
x=main(123)
print(x)