from testing import testFunc
def vowel_case(s):
    vowels="aAeEiIoOuU"
    s = [
        l.upper() if l.lower() in vowels else l.lower() 
        for l in s
    ]
    return ''.join(s)

# UNIT TESTS: vowel_case(s)
cases = [
"vowelcase",
"coding is fun",
"HELLO, world!",
"git cherry-pick",
"HEAD~1"
]
results = [
"vOwElcAsE",
"cOdIng Is fUn",
"hEllO, wOrld!",
"gIt chErry-pIck",
"hEAd~1"
]
testFunc(vowel_case, cases, results)

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

# UNIT TESTS: parse_unordered_list(markdown)
cases = [
    "- Item A\n- Item B",
    "-  JavaScript\n-  Python",
    "- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla",
    "- A-1\n- A-2\n- B-1"
]
results = [
    "<ul><li>Item A</li><li>Item B</li></ul>",
    "<ul><li>JavaScript</li><li>Python</li></ul>",
    "<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>",
    "<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>"
]
testFunc(parse_unordered_list, cases, results)

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

# UNIT TESTS: is_sorted(arr)     
cases = [
    [1,2,3,4,5],[10,8,6,4,2],[1,3,2,4,5],[3.14, 2.71, 1.61, 0.57],
    [12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9],[0.4, 0.5, 0.3]
]
results =[
    "Ascending","Descending","Not sorted","Descending",
    "Ascending","Not sorted"
]
testFunc(is_sorted, cases, results)