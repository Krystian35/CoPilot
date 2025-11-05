import pytest
from function import add, is_even, reverse_string

def test_add():
    # Test positive numbers
    assert add(2, 3) == 5
    assert add(0, 5) == 5
    assert add(10, 20) == 30
    
    # Test with negative numbers
    assert add(-1, 1) == 0
    assert add(-5, -3) == -8
    
    # Test large numbers
    assert add(999999, 1) == 1000000
    assert add(-999999, -1) == -1000000

def test_add_edge_cases():
    # Test with None values
    with pytest.raises(TypeError):
        add(None, 5)
    with pytest.raises(TypeError):
        add(5, None)
    with pytest.raises(TypeError):
        add(None, None)
    
    # Test with non-numeric types
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add([], {})

def test_is_even():
    # Test even numbers
    assert is_even(2) == True
    assert is_even(0) == True
    assert is_even(100) == True
    
    # Test odd numbers
    assert is_even(1) == False
    assert is_even(-1) == False
    assert is_even(99) == False
    
    # Test large numbers
    assert is_even(1000000) == True
    assert is_even(999999) == False

def test_is_even_edge_cases():
    # Test with None value
    with pytest.raises(TypeError):
        is_even(None)
    
    # Test with non-numeric types
    with pytest.raises(TypeError):
        is_even("2")
    with pytest.raises(TypeError):
        is_even([])
    
    # Test with float numbers
    with pytest.raises(TypeError):
        is_even(2.5)

def test_reverse_string():
    # Test basic strings
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    
    # Test empty string
    assert reverse_string("") == ""
    
    # Test single character
    assert reverse_string("a") == "a"
    
    # Test palindrome
    assert reverse_string("radar") == "radar"
    
    # Test with spaces
    assert reverse_string("hello world") == "dlrow olleh"
    
    # Test with special characters
    assert reverse_string("!@#$%") == "%$#@!"
    assert reverse_string("123") == "321"

def test_reverse_string_edge_cases():
    # Test with None value
    with pytest.raises(TypeError):
        reverse_string(None)
    
    # Test with non-string types
    with pytest.raises(TypeError):
        reverse_string(123)
    with pytest.raises(TypeError):
        reverse_string([1, 2, 3])
    
    # Test with very long string
    long_string = "a" * 10000
    assert reverse_string(long_string) == long_string[::-1]
    
    # Test with unicode characters
    assert reverse_string("héllo") == "olléh"
    assert reverse_string("🌟✨") == "✨🌟"