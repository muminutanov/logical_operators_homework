def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    return(a<b and b<c) or (a>b and b>c)
x=main(a=3,b=4,c=5)
print(x)