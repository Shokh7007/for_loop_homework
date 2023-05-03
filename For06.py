def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    x=list(range(A,B))
    s=0
    for i in x:
        s=s+i
    return s
print(main(3,6))