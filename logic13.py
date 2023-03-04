def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    c=a//10
    b=a%10
    return((c+b)%2==0)
x=main(12)
print(x)

