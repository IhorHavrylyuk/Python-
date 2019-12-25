def word_stat(words):
    word_map = {}
    for word in words:
        if word not in word_map:
            word_map[word] = 1
        else:
            word_map[word] += 1
    return word_map


def count_words(name):
    with open(name, 'r') as f:
        text = f.read()
        word_list = text.split()
        return len(word_list), word_stat(word_list)


def download_file(url, name):
    import urllib.request
    urllib.request.urlretrieve(url, name)


if __name__ == '__main__':
    _url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
    _path = 'D:/Labs/Python/text.txt'
    download_file(_url, _path)
    file_name = 'text.txt'
    length_file, words_stats = count_words(file_name)
    print('Кількість слів у текстовому файлі = {}'.format(length_file))
    print("Статистика слів:")
    for key, value in words_stats.items():
        print('{0} -- {1}'.format(key, value))