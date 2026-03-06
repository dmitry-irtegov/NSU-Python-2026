from typing import List

def find_urls(text: str) -> List[str]:
    urls = []
    words = text.split()

    for word in words:
        while word and word[-1] in ",.!?;:":
            word = word[:-1]

        lower_word = word.lower()

        if lower_word.startswith("www.") or \
           lower_word.startswith("http://") or \
           lower_word.startswith("https://"):

            if lower_word.startswith("www."):
                rest = word[4:]
            elif lower_word.startswith("http://"):
                rest = word[7:]
            else:
                rest = word[8:]

            if rest and all(c.isalnum() or c in "-." for c in rest):
                urls.append(word)

    return urls