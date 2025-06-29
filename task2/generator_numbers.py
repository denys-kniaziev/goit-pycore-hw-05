import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float]:
    """
    Generator function that analyzes text and yields all real numbers found.
    
    Numbers are considered valid if they are clearly separated by spaces
    on both sides and represent real numbers (including integers and floats).
    
    Args:
        text (str): Input text to analyze for numbers
        
    Yields:
        float: Real numbers found in the text
    """
    # Regular expression pattern to match real numbers
    # \b ensures word boundaries (numbers separated by spaces)
    # \d+ matches one or more digits
    # (?:\.\d+)? optionally matches decimal part
    pattern = r'\b\d+(?:\.\d+)?\b'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Yield each number as float
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable) -> float:
    """
    Calculates the total sum of all numbers in the text using a generator function.
    
    Args:
        text (str): Input text containing numbers
        func (Callable): Generator function to extract numbers from text
        
    Returns:
        float: Total sum of all numbers found in the text
    """
    # Use the generator function to get all numbers and sum them
    total = sum(func(text))
    return total


# Example usage and testing
if __name__ == "__main__":
    # Test with different text examples
    test_cases = [
        "Price: 15.99 and discount 5.50, total: 10.49",
        "No numbers in this text!",
        "Simple integers: 100 200 300",
        "Mixed: 1.5 and 2 and 3.14159"
    ]
    
    print("\nTesting with different text examples:")
    for i, text in enumerate(test_cases, 1):
        numbers = list(generator_numbers(text))
        result = sum_profit(text, generator_numbers)
        print(f"Test {i}: (text: '{text}')")
        print(f"Numbers found: {numbers}")
        print(f"Total profit: {result}:")
