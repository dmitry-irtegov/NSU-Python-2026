import os
import random
import tempfile
from collections import defaultdict
from unittest import TestCase, main


def invert_text(text):
    inv = defaultdict(list)

    for line in text.splitlines():
        if not line or " - " not in line:
            continue

        eng, lats = line.split(" - ", 1)
        for lat in lats.split(", "):
            inv[lat].append(eng)

    result_lines = []
    for lat, engs in sorted(inv.items()):
        sorted_engs = sorted(set(engs))
        result_lines.append(f"{lat} - {', '.join(sorted_engs)}")

    return "\n".join(result_lines) + "\n"


def process_file(src_path, dst_path):
    with open(src_path, "r", encoding="utf-8") as f:
        result = invert_text(f.read())

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(result)


class TestDict(TestCase):
    def setUp(self):
        self.src = (
            "apple - malum, pomum, popula\n"
            "fruit - baca, bacca, popum\n"
            "punishment - malum, multa"
        )
        self.exp = (
            "baca - fruit\n"
            "bacca - fruit\n"
            "malum - apple, punishment\n"
            "multa - punishment\n"
            "pomum - apple\n"
            "popula - apple\n"
            "popum - fruit\n"
        )

    def test_inv(self):
        self.assertEqual(invert_text(self.src), self.exp)

    def test_io(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            s_path = os.path.join(tmpdir, "src.txt")
            d_path = os.path.join(tmpdir, "dst.txt")

            with open(s_path, "w", encoding="utf-8") as f:
                f.write(self.src)

            process_file(s_path, d_path)

            with open(d_path, "r", encoding="utf-8") as f:
                self.assertEqual(f.read(), self.exp)

    def test_rand(self):
        random.seed(42)
        engs = [f"e_{i}" for i in range(5)]
        lats = [f"l_{i}" for i in range(5)]
        text = "\n".join(f"{e} - {', '.join(random.sample(lats, 2))}" for e in engs)

        res = invert_text(text)
        self.assertTrue(len(res) > 0)

        keys = [line.split(" - ")[0] for line in res.splitlines()]
        self.assertEqual(keys, sorted(keys))


if __name__ == "__main__":
    main()
