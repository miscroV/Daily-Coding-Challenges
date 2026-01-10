import math

def vowel_case(s: str) -> str:
    """ Jan-6
    
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
    """ Jan-7 

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
    """ Jan-8
    
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
    """Jan-9

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

def tic_tac_toe(board):
    if len(board) != len([i for i in zip(*board)]): return "Bad Board"

    views =  [board[i] for i in range(0,len(board))]                # horizontal wins
    views += [[i for i in zip(*board)]]                             # vertical wins
    views += [[board[i][i] for i in range(0,len(board))]]           # Diagonal 1
    views += [[board[i][k] for i,k  in 
               zip(range(0,len(board)),range(len(board)-1,-1,-1))]] # Diagonal 2
    
    wins   = [view[0] if all(cell == view[0] for cell in view) 
              else None for view in views]
    winner = [win for win in wins if win is not None][0]

    return f"{winner} wins" if winner != None else "Draw"

print(
    tic_tac_toe(
        [["X", "X", "X", "X"], 
         ["O", "O", "X", "O"], 
         ["O", "X", "O", "O"],
         ["O", "O", "X", "O"]]
    )
)