import math
import re
import statistics

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

def parse_link(markdown):
    """ Jan 14

    Given the string of a link in Markdown, return the equivalent HTML string.

    A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

    For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

    Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.
    """
    label = re.search(r"\[.*\]", markdown).group()[1:-1]
    link  = re.search(r"\(.*\)", markdown).group()[1:-1]
    return f"<a href=\"{link}\">{label}</a>"

def array_swap(arr: list) -> list:
    """ Jan 15
    
    Given an array with two values, return an array with the values swapped.

    For example, given ["A", "B"] return ["B", "A"].    
    """
    if len(arr) > 2: raise ValueError(
        f"Invalid Value, Received: {arr},\n\tExpected list of size 2, Received list of size {len(arr)}"
        )
    
    return [arr[1],arr[0]]

def is_integer_hypotenuse(a: int, b: int) -> bool:
    """ Jan 16
    
    Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.

    The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total (a2 + b2 = c2).


    """
    h = math.sqrt((a**2) + (b**2))

    return True if h == int(h) else False

def knight_moves(position: str) -> int:
    """ Jan 17

    Given the position of a knight on a chessboard, return the number of valid squares the knight can move to.

    Parameters
    ----------
    postion: str
        A position on a chess board in chess notation, e.g. "A8" or "H1"
    
    Returns
    -------
    int
        The number of valid moves for a knight located on that square. 

    Notes
    -----  
    A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:
    
    A8 	B8 	C8 	D8 	E8 	F8 	G8 	H8

    A7 	B7 	C7 	D7 	E7 	F7 	G7 	H7

    A6 	B6 	C6 	D6 	E6 	F6 	G6 	H6

    A5 	B5 	C5 	D5 	E5 	F5 	G5 	H5

    A4 	B4 	C4 	D4 	E4 	F4 	G4 	H4

    A3 	B3 	C3 	D3 	E3 	F3 	G3 	H3

    A2 	B2 	C2 	D2 	E2 	F2 	G2 	H2

    A1 	B1 	C1 	D1 	E1 	F1 	G1 	H1

    A knight moves in an "L" shape: two squares in one direction (horizontal or vertical), and one square in the perpendicular direction.

    This means a knight can move to up to eight possible positions, but fewer when near the edges of the board. For example, if a knight was at A1, it could only move to B3 or C2.

    """
    

    files, ranks = "ABCDEFGH", "87654321"
    move_indexes = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    moves = len(
        [
            (files.find(position[0]) + f, ranks.find(position[1]) + r)
            for r,f in move_indexes
            if (files.find(position[0]) + f in range(0,len(files)) and
                ranks.find(position[1]) + r in range(0,len(ranks)))
        ]
    )
    return moves

def gets_free_shipping(cart: list[str], minimum: float) -> bool:
    """ Jan 18
    
    Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.

    Parameters
    ----------
    cart: list[str]
        The list of items in the cart in string format.
    minimum: float
        the minimum cost for free shipping

    Returns
    -------
    bool
        Whether the cost of the cart is high enough for free shipping

    
    Notes
    -----

    The given array will contain items from the list below:
        Item 	Price
        "shirt" --- 34.25
        "jeans" --- 48.50
        "shoes" --- 75.00
        "hat" ----- 19.95
        "socks" --- 15.00
        "jacket" -- 109.95
    """

    item_costs = {
        "shirt" : 34.25,
        "jeans" : 48.50,
        "shoes" : 75.00,
        "hat"   : 19.95,
        "socks" : 15.00,
        "jacket": 109.95
    }
    total = 0
    for item in cart: total += item_costs.get(item, 0)
    return total > minimum

def compare_energy(calories_burned: int, watt_hours_used: int) -> str:
    """
    Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.

    Parameters
    ----------
    calories_burned: int
        Number of calories burned during workout
    watt_hours_used: int
        Number of watt hours used by electronic devices during workout. 

    Returns
    -------
    str:
        string refering to the higher value between calories burned and what hours used. Can also return "Equal".

    Notes
    -----
    To compare them, convert both values to joules using the following conversions:

    1 Calorie equals 4184 joules.

    1 watt-hour equals 3600 joules.

    Return:

    "Workout" if the workout used more energy.

    "Devices" if the device used more energy.

    "Equal" if both used the same amount of energy.
    """
    cals_in_J, watts_in_J = calories_burned * 4184, watt_hours_used * 3600
    return "Equal" if cals_in_J == watts_in_J else ("Workout" if cals_in_J > watts_in_J else "Devices")

def to_consonant_case(s):
    """ Jan 20

Given a string representing a variable name, convert it to consonant case using the following rules:


    Parameters
    ----------
    s: str
        The input string to convert to consonant case
    
        
    Returns
    -------
    str
        The string converted to consonant case

        
    Notes
    -----

    All consonants should be converted to uppercase.

    All vowels (a, e, i, o, u in any case) should be converted to lowercase.

    All hyphens (-) should be converted to underscores (_).

    """
    return ''.join([c.lower() if c in 'AEIOU' else ("_" if c in "-" else c) for c in s.upper()])

def parse_inline_code(markdown: str) -> str:
    """ Jan 21
    Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

    Parameters
    ----------
    markdown: str
        a string in markdown format

    Returns
    -------
    str
        an html string using the <code></code> tags instead of markdown ``s

    Notes
    -----
    
    Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

    Return the given string with all code blocks converted to HTML code tags.

    For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

    Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
    """
    openning_tag = True
    while markdown.count("`") > 1 or not openning_tag:
        markdown = markdown.replace(
            '`',
            "<code>" if openning_tag else "</code>",
            1
        )
        openning_tag = not openning_tag

    return markdown

def get_average_grade(scores: list[int]) -> str:
    """ jan 22
    
    Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following chart:

    Parameters
    ----------
    scores: list(int)

    Returns
    -------

    str
        The average letter grade of the scores.

    Notes
    -----

    Average Score	Letter Grade

    97-100	"A+"

    93-96	"A"

    90-92	"A-"

    87-89	"B+"

    83-86	"B"

    80-82	"B-"

    77-79	"C+"

    73–76	"C"

    70-72	"C-"

    67-69	"D+"

    63-66	"D"

    60–62	"D-"

    below 60	"F"

    Calculate the average by adding all scores in the array and dividing by the total number of scores.
    """ 
    grade_ranges = {
        "A+": (97, 100),
        "A":  (93, 97),
        "A-": (90, 92),
        "B+": (87, 89),
        "B":  (83, 86),
        "B-": (80, 82),
        "C+": (77, 79),
        "C":  (73, 76),
        "C-": (70, 72),
        "D+": (67, 69),
        "D":  (63, 66),
        "D-": (60, 62),
        "F":  (0, 59)
    }
    avg_grade = math.floor(statistics.mean(scores))
    if not 0 <= avg_grade <= 100: raise ValueError("Average of list outside grade range")

    for key, value in grade_ranges.items():
        low, high = value
        if low <= avg_grade <= high:
            return key

def is_valid_hex(s: str) -> bool:
    """jan 22
    
    Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

    Parameters
    ----------
    s: str
        A string possibly containing a hexidecimal value. 

    Returns
    
    Start with a #, and
    be followed by either 3 or 6 hexadecimal characters.
    Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).
    """
    return s[0] == "#" and len(s[1:]) in (3,6) and all([c.lower() in "0123456789abcdef" for c in s[1:]])

