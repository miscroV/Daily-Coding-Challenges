# from testing import testFunc
def vowel_case(s):
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

def parse_unordered_list(markdown):
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

def is_sorted(arr):
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
