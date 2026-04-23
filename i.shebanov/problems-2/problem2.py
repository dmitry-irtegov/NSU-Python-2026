from collections import defaultdict

def inverse_dictionary(dictionary):
    inversed_dictionary = defaultdict(list)
    for word in dictionary.keys():
        for translation in dictionary[word]:
            inversed_dictionary[translation].append(word)
    return dict(inversed_dictionary)

def convert_to_dict(text):
    dictionary = {}
    for line in text.splitlines():
        word, translations = line.split(' - ')
        dictionary[word] = translations.split(', ')
    return dictionary

def convert_to_text(dictionary):
    text = ''
    sorted_keys = sorted(dictionary.keys())
    for word in sorted_keys:
        translations = dictionary[word]
        text += f'{word} - {", ".join(translations)}\n'
    return text

def inverse_dictionary_files(source_dictionary_path, inverse_dictionary_path):
    with open(source_dictionary_path, 'r', encoding='utf-8') as f:
        dictionary = convert_to_dict(f.read())
    inversed_dictionary = inverse_dictionary(dictionary)
    with open(inverse_dictionary_path, 'w', encoding='utf-8') as f:
        f.write(convert_to_text(inversed_dictionary))

if __name__ == '__main__':
    from unittest import TestCase, main
    import tempfile
    import os

    class TestDictionaryFunctions(TestCase):

        def setUp(self):
            self.source_text = (
                "apple - malum, pomum, popula\n"
                "fruit - baca, bacca, popum\n"
                "punishment - malum, multa"
            )

            self.expected_inverse = {
                "baca": ["fruit"],
                "bacca": ["fruit"],
                "malum": ["apple", "punishment"],
                "multa": ["punishment"],
                "pomum": ["apple"],
                "popula": ["apple"],
                "popum": ["fruit"],
            }

        def test_convert_to_dict(self):
            d = convert_to_dict(self.source_text)

            self.assertEqual(d["apple"], ["malum", "pomum", "popula"])
            self.assertEqual(d["fruit"], ["baca", "bacca", "popum"])
            self.assertEqual(d["punishment"], ["malum", "multa"])

        def test_inverse_dictionary(self):
            d = convert_to_dict(self.source_text)
            inv = inverse_dictionary(d)

            self.assertEqual(inv, self.expected_inverse)

        def test_convert_to_text(self):
            text = convert_to_text(self.expected_inverse)

            expected_text = (
                "baca - fruit\n"
                "bacca - fruit\n"
                "malum - apple, punishment\n"
                "multa - punishment\n"
                "pomum - apple\n"
                "popula - apple\n"
                "popum - fruit\n"
            )

            self.assertEqual(text, expected_text)

        def test_full_cycle(self):
            d = convert_to_dict(self.source_text)
            inv = inverse_dictionary(d)
            text = convert_to_text(inv)

            d2 = convert_to_dict(text)
            self.assertEqual(inv, d2)

        def test_file_inversion(self):
            with tempfile.TemporaryDirectory() as tmpdir:
                src_path = os.path.join(tmpdir, "src.txt")
                dst_path = os.path.join(tmpdir, "dst.txt")

                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(self.source_text)

                inverse_dictionary_files(src_path, dst_path)

                with open(dst_path, "r", encoding="utf-8") as f:
                    result_text = f.read()

                expected_text = convert_to_text(self.expected_inverse)
                self.assertEqual(result_text, expected_text)
    main()
