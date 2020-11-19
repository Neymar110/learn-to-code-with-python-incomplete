import doctest

Peter = 0
Paul = 0
Calleb = 0
Kira = 0

def apple_eating_competition(player, num):
    """ The First Argument Should Be the Player Name And The Second Argument Should Be The Number Of Apples Eaten

    >>> apple_eating_competition(Peter, 5)
    5
    
    """
    player += num
    return player

if __name__ == "__main__":
    doctest.testmod()