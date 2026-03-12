import unittest

def clip_sequence(seq, a, b):
    result = []
    
    for x in seq:
        if x < a:
            result.append(a)
        elif x > b:
            result.append(b)
        else:
            result.append(x)

    return result


class TestClipSequence(unittest.TestCase):

    def test_no_clipping_needed(self):
        self.assertEqual(
            clip_sequence([3, 4, 5], 1, 10),
            [3, 4, 5]
        )

    def test_clip_lower_bound(self):
        self.assertEqual(
            clip_sequence([1, 5, 10], 4, 15),
            [4, 5, 10]
        )

    def test_clip_upper_bound(self):
        self.assertEqual(
            clip_sequence([1, 5, 20], 0, 15),
            [1, 5, 15]
        )

    def test_clip_both_sides(self):
        self.assertEqual(
            clip_sequence([-5, 0, 10, 25], 0, 20),
            [0, 0, 10, 20]
        )

    def test_empty_list(self):
        self.assertEqual(
            clip_sequence([], 0, 10),
            []
        )

    def test_all_values_outside(self):
        self.assertEqual(
            clip_sequence([-10, 50], 0, 20),
            [0, 20]
        )


if __name__ == "__main__":
    unittest.main()