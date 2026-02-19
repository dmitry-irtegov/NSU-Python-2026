
class Vector:
    def __init__(self, n):
        self._length = n
        self._nums = [0] * n

    @classmethod
    def from_list(cls, numList):
        ret = cls(len(numList))
        ret._nums = numList.copy()
        return ret

    def __len__(self):
        return self._length

    def __setitem__(self, index, value):
        self._nums[index] = value

    def __getitem__(self, index):
        return self._nums[index]

    def __add__(self, other):
        ret = Vector(len(self))
        for i in range(len(self)):
            ret[i] = self[i] + other[i]
        return ret

    def __sub__(self, other):
        ret = Vector(len(self))
        for i in range(len(self)):
            ret[i] = self[i] - other[i]
        return ret

    def __mul__(self, scalar):
        ret = Vector(len(self))
        for i in range(len(self)):
            ret[i] = self[i] * scalar
        return ret

    def __rmul__(self, scalar):
        return self * scalar

    def __eq__(self, other):
        for i in range(len(self)):
            if self[i] != other[i]:
                return False

        return True

    def __str__(self):
        return "( " + ", ".join(str(x) for x in self._nums) + " )"

    def dot(self, other):
        ret = 0
        for i in range(len(self)):
            ret += self[i] * other[i]
        return ret

if __name__ == "__main__":
    line1 = input("Enter first vector (numbers separated by spaces): ").strip()
    if not line1:
        print("Error: empty input")
        exit(1)
    nums1 = list(map(int, line1.split()))
    v1 = Vector.from_list(nums1)

    line2 = input("Enter second vector (numbers separated by spaces): ").strip()
    if not line2:
        print("Error: empty input")
        exit(1)
    nums2 = list(map(int, line2.split()))
    v2 = Vector.from_list(nums2)

    print("\nAvailable operations:")
    print("  +    - addition of vectors")
    print("  -    - subtraction of vectors")
    print("  *    - multiplication by scalar (will require entering a number)")
    print("  dot  - dot product")
    print("  ==   - equality check")
    op = input("Choose operation: ").strip()

    try:
        if op == "+":
            result = v1 + v2
            print("Addition result:", result)

        elif op == "-":
            result = v1 - v2
            print("Subtraction result:", result)

        elif op == "*":
            scalar_str = input("Enter scalar: ").strip()
            if not scalar_str:
                print("Error: scalar not entered")
                exit(1)
            scalar = float(scalar_str)
            result = v1 * scalar
            print("Result of multiplication by scalar for first vector:", result)

            scalar = float(scalar_str)
            result = v2 * scalar
            print("Result of multiplication by scalar for second vector:", result)

        elif op == "dot":
            result = v1.dot(v2)
            print("Dot product:", result)

        elif op == "==":
            print("Vectors are equal?", v1 == v2)

        else:
            print("Unknown operation")

    except ValueError as e:
        print("Error:", e)