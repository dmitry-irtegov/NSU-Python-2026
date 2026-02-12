import unittest



def return_prime_list(n):
    return [
        i for i in range(2, n + 1)
        if all(i % j for j in range(2, int((i)**0.5) + 1))
    ]



class TestPrimes(unittest.TestCase):
   
    def test_primes(self):
        from sympy import isprime
        import random
        random.seed(42)
        num = random.randint(1, 1000000)
        ref_arr = [x for x in range(2, num + 1) if isprime(x)]
        my_arr = return_prime_list(num)
        self.assertEqual(my_arr, ref_arr)
        
if __name__ == "__main__":
    unittest.main()