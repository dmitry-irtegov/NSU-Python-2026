import unittest



def return_prime_list(n):
    """function that returns a list of prime numbers up to n"""
    return [
        i for i in range(2, n + 1)
        if all(i % j for j in range(2, int((i)**0.5) + 1))
    ]



class TestPrimes(unittest.TestCase):
   
    def test_primes(self):
        from sympy import isprime
        
        num = 1000000
        ref_arr = [x for x in range(2, num + 1) if isprime(x)]
        my_arr = return_prime_list(num)
        self.assertEqual(my_arr, ref_arr)
        self.assertEqual([], return_prime_list(0))
        self.assertEqual([], return_prime_list(-1488))
    
    def test_zeroes(self):
        n = 1000000
        zeroes = [0] * n
        res = [return_prime_list(x) for x in zeroes]
        emptys = [[]] * n

        self.assertEqual(res, emptys)

    def test_negates(self):
        negs = [-706614, -670420, -856740, -761179, -540022, -568648, -156115, -263282, -200923, -902497, 
                -44755, -598547, -201436, -469687, -453211, -297816, -435355, -502952, -785052, 
                -960991, -136099, -15214, -805953, -498533, -697190, -344820, -903704, -851007, 
                -339012, -502856, -979863, -199784, -471248, -289058, -819794, -347162, -700990, 
                -412233, -444014, -402524, -836288, -996213, -48473, -236386, -863927, -156429,
                -548212, -864082, -366530, -901634, -357015, -937879, -271322, -317060, -145555,
                -907249, -602242, -246112, -544063, -89926, -225428, -533723, -421895, -101267, -191558, 
                -542907, -329007, -835553, -897520, -437468, -981969, -303312, -145651, -752910, -850667,
                -655797, -570557, -495522, -554968, -900456, -740348, -161229, -386195, -354641, -894813,
                -519831, -871041, -172233, -999198, -769244, -511180, -712103, -678087, -612811, -816924, -28322, -137431, -280181, -127214,
                -609199]
        res = [return_prime_list(x) for x in negs]
        emptys = [[]] * len(negs)
        self.assertEqual(emptys, res)

    
        
if __name__ == "__main__":
    unittest.main()