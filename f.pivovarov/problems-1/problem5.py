import math
import unittest

def factorize(n):
    if n <= 1:
        return []
    
    factors = []
    
    if n % 2 == 0:
        count = 0
        while n % 2 == 0:
            count += 1
            n //= 2
        factors.append([2, count])
    
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                count += 1
                n //= divisor
            factors.append([divisor, count])
        divisor += 2
    
    if n > 1:
        factors.append([n, 1])
    
    return factors


class TestFactorize(unittest.TestCase):
    # Helper to check if factorization is correct
    def verify_factorization(self, n, factors):
        result = 1
        for prime, power in factors:
            result *= prime ** power
        return result == n

    ''' TEST '''
    def test_prime_number(self):
        self.assertEqual(factorize(2), [[2, 1]])
        self.assertEqual(factorize(3), [[3, 1]])
        self.assertEqual(factorize(17), [[17, 1]])
        self.assertEqual(factorize(97), [[97, 1]])
    
    def test_power_of_two(self):
        self.assertEqual(factorize(4), [[2, 2]])
        self.assertEqual(factorize(8), [[2, 3]])
        self.assertEqual(factorize(16), [[2, 4]])
        self.assertEqual(factorize(1024), [[2, 10]])
    
    def test_power_of_odd_prime(self):
        self.assertEqual(factorize(9), [[3, 2]])
        self.assertEqual(factorize(27), [[3, 3]])
        self.assertEqual(factorize(125), [[5, 3]])
        self.assertEqual(factorize(2401), [[7, 4]])
    
    def test_product_of_two_primes(self):
        self.assertEqual(factorize(6), [[2, 1], [3, 1]])
        self.assertEqual(factorize(15), [[3, 1], [5, 1]])
        self.assertEqual(factorize(77), [[7, 1], [11, 1]])
    
    def test_example_from_task(self):
        result = factorize(12)
        self.assertEqual(result, [[2, 2], [3, 1]])
        self.assertTrue(self.verify_factorization(12, result))
    
    def test_multiple_factors(self):
        result = factorize(60) 
        self.assertEqual(result, [[2, 2], [3, 1], [5, 1]])
        self.assertTrue(self.verify_factorization(60, result))
    
    def test_large_composite(self):
        n = 2 * 2 * 3 * 5 * 5 * 7 * 11 
        result = factorize(n)
        expected = [[2, 2], [3, 1], [5, 2], [7, 1], [11, 1]]
        self.assertEqual(result, expected)
        self.assertTrue(self.verify_factorization(n, result))
    
    # Negative scenarios
    def test_n_equals_1(self):
        self.assertEqual(factorize(1), [])
    
    def test_n_equals_0(self):
        self.assertEqual(factorize(0), [])
    
    def test_negative_number(self):
        self.assertEqual(factorize(-12), [])
    
    
    def test_verify_helper(self):
        self.assertTrue(self.verify_factorization(12, [[2, 2], [3, 1]]))
        self.assertTrue(self.verify_factorization(100, [[2, 2], [5, 2]]))
        self.assertFalse(self.verify_factorization(12, [[2, 1], [3, 1]]))
    
    def test_property_product_equals_n(self):
        test_numbers = [2, 6, 12, 30, 100, 2310, 10000]
        for n in test_numbers:
            with self.subTest(n=n):
                factors = factorize(n)
                self.assertTrue(self.verify_factorization(n, factors))
    
    def test_factors_are_prime(self):
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if x % i == 0:
                    return False
            return True
        
        for n in [12, 100, 2310, 9999]:
            with self.subTest(n=n):
                factors = factorize(n)
                for prime, _ in factors:
                    self.assertTrue(is_prime(prime))
    
    def test_factors_sorted(self):
        for n in [12, 60, 100, 2310]:
            with self.subTest(n=n):
                factors = factorize(n)
                primes = [p for p, _ in factors]
                self.assertEqual(primes, sorted(primes))


if __name__ == "__main__":
    unittest.main()