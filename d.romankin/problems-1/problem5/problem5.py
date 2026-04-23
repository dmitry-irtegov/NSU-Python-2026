import unittest


def factorize(n):
    """function of factorizing an integer:
    n : int - number to factorize
    """
    factors = []
    d = 2    
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                count += 1
                n //= d
            factors.append([d, count])
        d += 1
    
    if n > 1:
        factors.append([n, 1])
        
    return factors

class TestFactorize(unittest.TestCase):

    
    def test_factorize(self):
        
        nums = [678457, 79544, 478950, 737546, 900767, 469155, 738339, 244601, 366582, 190183, 465267, 892834, 815467, 43090, 402577, 560646, 441282, 93548, 513032, 610784, 957823, 710612, 502248, 877551, 244342, 143465, 830814, 729395, 992384, 17692, 744825, 920013, 693281, 223079, 815566, 459351, 747512, 290803, 909403, 728747, 493778, 201467, 435087, 344257, 460753, 580408, 446865, 746967, 248392, 658033, 
                494720, 518380, 805331, 924622, 211531, 967003, 605004, 373422, 380679, 377614, 
                901739, 913276, 188201, 401883, 287437, 27692, 140950, 780099, 440843, 703529, 
                942308, 180755, 319362, 823443, 745675, 630003, 925586, 6646, 623483, 113641, 4958, 
                440281, 288887, 207238, 115325, 370688, 549471, 961610, 938496, 528306, 475338, 159992,
                961599, 150199, 910261, 79715, 195268, 834987, 803795, 723185]
        res_nums = []
        prods = []
        prod = 1
        for num in nums:
            res_nums.append(factorize(num))
        
        for res_num in res_nums:
            for j in res_num:
                prod *= (j[0]**j[1])
            prods.append(prod)
            prod = 1
        
        
        
        self.assertEqual(prods, nums)
        self.assertEqual(factorize(-1488), [])
        self.assertEqual(factorize(0), [])
    
    def test_negate(self):
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
        facts = [factorize(x) for x in negs]
        res = [[]] * len(negs)
        self.assertEqual(res, facts) 

    def test_primes(self):
        from sympy import isprime
        num = 100000
        primes_list = [x for x in range(2, num + 1) if isprime(x)]
        facts = [factorize(x) for x in primes_list]
        for i in range (len(primes_list)):
            self.assertEqual([[primes_list[i], 1]], facts[i])
            self.assertEqual(len(factorize(primes_list[i])), 1)
    
    def test_nulls(self):
        n = 1000000
        nulls = [0] * n
        facts = [factorize(x) for x in nulls]
        res = [[]] * n
        self.assertEqual(facts, res)

if __name__ == "__main__":
    unittest.main()