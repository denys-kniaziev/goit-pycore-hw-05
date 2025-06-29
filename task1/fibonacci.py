def caching_fibonacci():
    """
    Creates and returns a fibonacci function with caching capability.
    
    This function implements closure to maintain a cache dictionary
    that stores previously computed Fibonacci numbers for optimization.
    
    Returns:
        function: Inner fibonacci function that computes n-th Fibonacci number
    """
    # Create empty cache dictionary to store computed values
    cache = {}
    
    def fibonacci(n: int) -> int:
        """
        Computes the n-th Fibonacci number using recursion with caching.
        
        The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
        Where F(n) = F(n-1) + F(n-2) for n > 1
        
        Args:
            n (int): Position in Fibonacci sequence (0-indexed)
            
        Returns:
            int: The n-th Fibonacci number
        """
        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
            
        # Check if value is already in cache
        if n in cache:
            return cache[n]
        
        # Compute and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    # Return the inner function (closure)
    return fibonacci


# Example usage and testing
if __name__ == "__main__":
    # Get the fibonacci function
    fib = caching_fibonacci()
    
    # Test the function with example values
    print(f"fib(10) = {fib(10)}")  # Should output: 55
    print(f"fib(15) = {fib(15)}")  # Should output: 610
    
    # Additional tests to verify correctness
    print("\nTesting Fibonacci sequence:")
    for i in range(11):
        print(f"F({i}) = {fib(i)}")
    
    # Test performance benefit of caching
    print(f"\nLarge number test:")
    print(f"fib(30) = {fib(30)}")  # Should be fast due to caching
