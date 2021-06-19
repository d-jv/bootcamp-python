import unittest


class MathDojo:

    def __init__(self) -> None:
        self.result = 0

    def add(self, num, *nums):
        try:
            num = int(num)
            map(int, nums)
        except ValueError: return None

        self.result += num
        for x in nums:
            self.result += x
        return self
    
    def subtract (self, num, *nums):
        self.result -= num
        for x in nums:
            self.result -= x
        return self
    
    def standardDeviation (self, num, *nums):
        squareDistance = 0
        numsList = [num]
        for i in nums:
            numsList.append(i)
        sumatoria = sum(numsList)
        avg = sumatoria / len(numsList)
        #falta por terminar



md = MathDojo()

hehe = md.add(2).add(1,5,1).subtract(3,2).result
print(hehe)

paProbar1 = MathDojo()
# Escriba el método add y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez
paProbarAdd = paProbar1.add(2).add(1,2,3).add(1,2).result
print(paProbarAdd)

paProbar2 = MathDojo()
# Escriba el método de subtract y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez
paProbarSubtract = paProbar2.add(10).subtract(1,1).subtract(3,1).subtract(5,4,3,2).result
print(paProbarSubtract)	

# --------------------------- TESTING ---------------------------------------
class MathDojoTesting(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def testCero(self):
        dojo = MathDojo()
        self.assertEqual(dojo.result, 0)

    def tearDown(self) -> None:
        return super().tearDown()

# if __name__ == '__main__':
#     unittest.main()