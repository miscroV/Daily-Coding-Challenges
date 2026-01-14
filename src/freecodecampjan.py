import math

def vowel_case(s: str) -> str:
    """ Jan 6
    
    Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

    Vowels are "a", "e", "i", "o", and "u" in any case.
    Non-alphabetical characters should remain unchanged.
    """
    vowels="aAeEiIoOuU"
    s = [
        l.upper() if l.lower() in vowels else l.lower() 
        for l in s
    ]
    return ''.join(s)

def parse_unordered_list(markdown: str) -> str:
    """ Jan 7 

    Given the string of a valid unordered list in Markdown, return the equivalent HTML string.

    An unordered list consists of one or more list items. A valid list item appears on its own line and:

    Starts with a dash ("-"), followed by
    At least one space, and then
    The list item text.
    The list is given as a single string with new lines separated by the newline character ("\n"). Do not include the newline characters in the item text.

    Wrap each list item in HTML li tags, and the whole list of items in ul tags.

    For example, given "- Item A\n- Item B", return "<ul><li>Item A</li><li>Item B</li></ul>".
    """
    items = markdown.split("\n")
    items = [item[2:].strip() for item in items]
    html="<ul>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ul>"
    return html

def is_sorted(arr: list) -> str:
    """ Jan 8
    
    Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

    If the given array is:

    In ascending order (lowest to highest), return "Ascending".
    In descending order (highest to lowest), return "Descending".
    Not sorted in ascending or descending order, return "Not sorted".
    """
    is_acc = True
    is_des = True
    for i in range(1, len(arr)):
        if not (arr[i] > arr[i-1]): is_acc = False
        if not (arr[i] < arr[i-1]): is_des = False

    if is_acc:
        return "Ascending"
    elif is_des:
        return "Descending"
    else:
        return "Not sorted"

def is_circular_prime(n: int) -> bool:
    """Jan 9

    Given an integer, determine if it is a circular prime.

    A circular prime is an integer where all rotations of its digits are themselves prime.

    For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.
    """
    # get circulars:
    circulars = []
    temp = str(n)
    for i in range(0,len(temp)):
        temp = f"{temp[1:]}{temp[:1]}"
        circulars.append(int(temp))
    print(circulars)

    # get all prime
    is_c_prime = True
    for n in circulars:
        for i in range(2,int(math.sqrt(n))):
            if (n % i) == 0:
                is_c_prime = False 
    return is_c_prime

def tic_tac_toe(board: list[list]) -> str:
    """ Jan 10
    
    Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

    Each element in the given matrix is either an "X" or "O".

    A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

    Return:

    "X wins" if player X has three in a row.
    "O wins" if player O has three in a row.
    "Draw" if no player has three in a row.

    """
    # Checks for if board is proportional
    if len(board) != len([i for i in zip(*board)]): return "Bad Board"

    views: list = [board[i] for i in range(0,len(board))]           # horizontal wins
    views += [list(i) for i in zip(*board)]                         # vertical wins
    views += [[board[i][i] for i in range(0,len(board))]]           # Diagonal 1
    views += [[board[i][k] for i,k  in 
               zip(range(0,len(board)),range(len(board)-1,-1,-1))]] # Diagonal 2
    
    winner: str = None
    for view in views:
        if all(cell == view[0] for cell in view):
            winner = view[0]
            break;

    return f"{winner} wins" if winner != None else "Draw"

def golf_score(par: int, strokes: int) -> str:
    """ Jan 11
    
    Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

    Return:

    "Hole in one!" if it took one stroke.
    "Eagle" if it took two strokes less than par.
    "Birdie" if it took one stroke less than par.
    "Par" if it took the same number of strokes as par.
    "Bogey" if it took one stroke more than par.
    "Double bogey" if took two strokes more than par.

    """

    if strokes == 1:
        return "Hole in one!"
    
    compare = par - strokes

    match compare:
        case  2: return "Eagle"
        case  1: return "Birdie"
        case  0: return "Par"
        case -1: return "Bogey"
        case -2: return "Double bogey"
        case  _: return ""

def get_number_of_plants(field_size: float, unit: str, crop: str) -> int:
    """ Jan 12
    
    Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

    1 acre equals 4046.86 square meters.
    1 hectare equals 10,000 square meters.
    Here's a list of crops that will be given as input and how much space a single plant takes:

    Crop	Space per plant
    "corn"	1 square meter
    "wheat"	0.1 square meters
    "soybeans"	0.5 square meters
    "tomatoes"	0.25 square meters
    "lettuce"	0.2 square meters
    Return the number of plants that fit in the field, rounded down to the nearest whole plant.
    """
    match unit:
        case "acres": sqrMeters = 4046.86
        case "hectares": sqrMeters = 10000
        case _: raise ValueError(f"Invalid unit, Received: {unit}\n\tPermitted Values: (\"acres\"|\"hectares\")")

    if not (isinstance(sqrMeters, float) or isinstance(sqrMeters, int)):
        raise ValueError(f"Invalid field_size, Received:{field_size}\n\tExpected type float or int.")
    sqrMeters *= field_size

    match crop:
        case "corn"    : sqrMeterPerPlant = 1
        case "wheat"   : sqrMeterPerPlant = 0.1
        case "soybeans": sqrMeterPerPlant = 0.5
        case "tomatoes": sqrMeterPerPlant = 0.25
        case "lettuce" : sqrMeterPerPlant = 0.2
        case _: raise ValueError(f"Invalid crop, Received:{crop}\n\tPermitted Values: (\"corn\"|\"wheat\"|\"soybeans\"|\"tomatoes\"|\"lettuce\")")

        
    return int(sqrMeters/sqrMeterPerPlant)

def odd_or_even(n: int) -> str:
    """ Jan 13

    Given a positive integer, return "Odd" if it's an odd number, and "Even" is it's even.
    """

    # Enforce Requirements
    if not isinstance(n, int): raise TypeError(f"Invalid Value, Received: {n}\n\tExpected int, got {type(n).__name__}")
    if not (n > 0): raise ValueError(f"Invalid Value, Received: {n}\n\tValue must be a postiveinteger")

    # check value of last bit is 1, if 1 return odd else even
    return "Odd" if n & 1 else "Even"

import re

def parse_link(markdown):
    label = re.search(r"\[.*\]", markdown).group()
    link  = re.search(r"\(.*\)", markdown).group()
    print(label)
    print(link)
    return (label, link)

print(parse_link("[freeCodeCamp](https://freecodecamp.org/)"))