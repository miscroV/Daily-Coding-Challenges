import pytest
from src.freecodecampjan import *

@pytest.mark.parametrize(
    "case, result",
    [
        ("vowelcase", "vOwElcAsE"),
        ("coding is fun","cOdIng Is fUn"),
        ("HELLO, world!","hEllO, wOrld!"),
        ("git cherry-pick","gIt chErry-pIck"),
        ("HEAD~1","hEAd~1")
    ]
)
def test_vowel_case(case, result):
    assert vowel_case(case) == result

@pytest.mark.parametrize(
    "case, result",
    [
        ("- Item A\n- Item B", 
         "<ul><li>Item A</li><li>Item B</li></ul>"),
        ("-  JavaScript\n-  Python",
         "<ul><li>JavaScript</li><li>Python</li></ul>"),
        ("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla",
         "<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>"),
        ("- A-1\n- A-2\n- B-1",
         "<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>"),
    ]
)
def test_parse_unordered_list(case, result):
    assert parse_unordered_list(case) == result

@pytest.mark.parametrize(
    "case, result",
    [
        ([1, 2, 3, 4, 5],"Ascending"),
        ([10, 8, 6, 4, 2],"Descending"),
        ([1, 3, 2, 4, 5],"Not sorted"),
        ([3.14, 2.71, 1.61, 0.57],"Descending"),
        ([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9],"Ascending"),
        ([0.4, 0.5, 0.3],"Not sorted")
    ]
)   
def test_is_sorted(case, result):
    assert is_sorted(case) == result

@pytest.mark.parametrize(
        "case, result",
    [
        (197, True),
        (23, False),
        (13, True),
        (89, False),
        (1193, True)
    ]
)   
def test_is_circular_prime(case, result):
    assert is_circular_prime(case) == result

@pytest.mark.parametrize(
    "case, result",  
    [
        ([["X", "X", "X"], 
          ["O", "O", "X"], 
          ["O", "X", "O"]],
          "X wins"),
        ([["X", "O", "X"], 
          ["X", "O", "X"], 
          ["O", "O", "X"]],
          "O wins"),
        ([["X", "O", "X"], 
          ["O", "X", "O"], 
          ["O", "X", "O"]],
          "Draw"),
        ([["X", "X", "O"],
          ["X", "O", "X"],
          ["O", "X", "X"]],
          "O wins"),
        ([["X", "O", "O"], 
          ["O", "X", "O"], 
          ["O", "X", "X"]],
          "X wins"),
        ([["O", "X", "X"], 
          ["X", "O", "O"], 
          ["X", "O", "X"]],
          "Draw")
    ]
)
def test_tic_tac_toe(case, result):
    assert tic_tac_toe(case) == result

@pytest.mark.parametrize(
    "case, result",
    [
        ((3,3) ,"Par"),
        ((4, 3),"Birdie"),
        ((3, 1),"Hole in one!"),
        ((5, 7),"Double bogey"),
        ((4, 5),"Bogey"),
        ((5, 3),"Eagle")
    ]
)
def test_golf_score(case, result):
    assert golf_score(*case) == result

@pytest.mark.parametrize(
    "case, result",
    [
        ((1,     "acres",    "corn"    ), 4046  ),
        ((2,     "hectares", "lettuce" ), 100000),
        ((20,    "acres",    "soybeans"), 161874),
        ((3.75,  "hectares", "tomatoes"), 150000),
        ((16.75, "acres",    "tomatoes"), 271139)
    ]
)
def test_get_number_of_plants(case, result):
    assert get_number_of_plants(*case) == result

@pytest.mark.parametrize(
    "case, result",
    [
        (1,"Odd"),
        (2,"Even"),
        (13,"Odd"),
        (196,"Even"),
        (123456789,"Odd")
    ]
)
def test_odd_or_even(case,result):
    assert odd_or_even(case) == result

@pytest.mark.parametrize(
    "case, result",
    [
        ("[freeCodeCamp](https://freecodecamp.org/)",
            '<a href="https://freecodecamp.org/">freeCodeCamp</a>'),
        ("[Donate to our charity.](https://www.freecodecamp.org/donate/)",
            '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>'),
        ("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)",
            '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>'),
    ]
)
def test_parse_link(case,result):
    assert parse_link(case) == result

@pytest.mark.parametrize(
    "case, result", 
    [
        (["A", "B"],["B", "A"]),
        ([25, 20],[20, 25]),
        ([True, False],[False, True]),
        (["1", 1],[1, "1"])
    ]
)
def test_array_swap(case,result):
    assert array_swap(case) == result