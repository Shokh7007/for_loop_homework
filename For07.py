def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    a=0
    x=list(range(N))
    for i in x:
        if i%2==1:
            a=a+i
    return a
print(main(12))