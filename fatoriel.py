# un  commentaire
def factoriel(n):
    """le factoriel"""
    if n <= 1:
        return 1
    else:
        return n *factoriel(n-1)
    
print(factoriel(100))
