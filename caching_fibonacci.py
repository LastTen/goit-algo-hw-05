def caching_fibonacci():
    """
    This function returns a memoized fibonacci function that caches the results of previous calls to improve performance.

    Returns:
        A function that takes an integer n and returns the nth Fibonacci number.
    """
    cache = {}

    def fibonacci(n: int):
        """
        This function calculates the nth Fibonacci number using dynamic programming.

        Args:
            n (int): The index of the Fibonacci number to calculate.

        Returns:
            int: The nth Fibonacci number.
        """
        if n in cache:
            return cache[n]
        if n <= 0:
            return 0
        if n == 1:
            return 1

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fibonacci = caching_fibonacci()
    print(fibonacci(50))
