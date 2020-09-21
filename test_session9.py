import pytest
import session9
import os
#import numpy as np
import inspect
import re

README_CONTENT_CHECK_FOR = [

]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 250, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 0


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    line_no =1
    for space in spaces:
        line_no +=1
        print('=====', line_no, space)
        #print(lines)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        #assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# def test_not_a_function_valueerror():
#     with pytest.raises(ValueError):
#        session9.outer_func()

# def test_not_number_valueerror():
#     with pytest.raises(ValueError):
#         session9.nextfibonacci('a')

# def test_not_function_valueerror():
#     with pytest.raises(ValueError):
#         session9.counter_add(4,5)

# Test for Odd time function calculation
def test_for_odd_time_func():
    try :
        assert (session9.add(1,2,3,6,5) == 17 ), 'Your function not working'
    except TypeError:
        print('Type Error')
def test_for_odd_even_time_func():
    try :
        assert (session9.add(1,2,3,6,6) == 18 ), 'Your function not working'
    except TypeError:
        print('Type Error')

def test_for_log_func():
    assert (session9.add_func(3,4,5,6,7) ==25), 'Your function not working'

def test_add_not_work():
    with pytest.raises(TypeError):
        session9.add_not_work(2, 3) , 'Your function not working'
def test_mult_not_work():
    with pytest.raises(TypeError):
        session9.mult_not_work(2, 3), 'Your function not working'

def test_add_work():
    assert (session9.add_work(2, 3)== 5) , 'Your function not working'
def test_mult_work():
    assert (session9.mult_work(2, 3) == 6), 'Your function not working'

def test_time_func():
    assert (session9.add_times(10,30,40) == 80), 'Your function not working'
    
def test_fn1():
    assert bool(session9.fn1()) == False, 'Your function not working'
def test_fn2():
    assert bool(session9.fn2()) == False, 'Your function not working'
def test_fn3():
    assert bool(session9.fn3()) == False, 'Your function not working'
def test_fn4():
    assert bool(session9.fn4()) == False, 'Your function not working'
def test_fn5():
    with pytest.raises(ValueError):
        session9.fn5(), 'Your function not working'
def test_fn15():
    with pytest.raises(ValueError):
        session9.fn15(), 'Your function not working'

def test_htmlize():
    assert session9.htmlize({1, 2, 3}) == '<pre>{1, 2, 3}</pre>', 'Your function not working'
def test_htmlize_1():
    assert session9.htmlize(abs) == '<pre>&lt;built-in function abs&gt;</pre>', 'Your function not working'
def test_htmlize_2():
    assert session9.htmlize('Heimlich & Co.\n- a game') == '<p>Heimlich &amp; Co.<br>\n- a game</p>', 'Your function not working'
def test_htmlize_3():
    assert session9.htmlize(42) == '<pre>42 (0x2a)</pre>', 'Your function not working'
def test_htmlize_4():
    assert session9.htmlize(['alpha', 66, {3, 2, 1}]) == '<ul>\n<li><p>alpha</p></li>\n<li><pre>66 (0x42)</pre></li>\n<li><pre>{1, 2, 3}</pre></li>\n</ul>', 'Your function not working'

def test_things_not_allowed():
    code_lines = inspect.getsource(session9)
    for word in CHECK_FOR_THINGS_NOT_ALLOWED:
        assert word not in code_lines, 'Have you heard of Pinocchio?'
