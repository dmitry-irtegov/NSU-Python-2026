lines = [
    "apple- malum, pomum, popula",
    "fruit- baca, bacca, popum",
    "punishment- malum, multa"
]

latin_to_english = {}

for line in lines:
    if '-' not in line:
        continue

    # 分割英语单词和拉丁语翻译部分
    eng_word, lat_translations_str = line.split('-')
    eng_word = eng_word.strip()

    # 分割拉丁语单词 (可能有多个，用逗号分隔)
    lat_words = [w.strip() for w in lat_translations_str.split(',')]

    # 构建反向字典
    for lat in lat_words:
        if lat not in latin_to_english:
            latin_to_english[lat] = []
        latin_to_english[lat].append(eng_word)

# 排序并输出
# 1. 字典的键 (拉丁词) 需要按字母顺序排序
sorted_latin_keys = sorted(latin_to_english.keys())

for lat in sorted_latin_keys:
    # 2. 每个拉丁词对应的英语翻译列表也需要排序
    eng_translations = sorted(latin_to_english[lat])
    print(f"{lat}- {', '.join(eng_translations)}")