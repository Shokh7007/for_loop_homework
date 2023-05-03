def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s=[]
    for i in range(n):
        s.append(str(i))
    x=','.join(s)
    return x
print(main(5))