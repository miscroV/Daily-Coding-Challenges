import pytest
from src.jan import *

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