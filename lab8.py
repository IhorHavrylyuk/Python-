import sys, os
import hashlib


def hashfile(path, block_size=1024):
    _file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = _file.read(block_size)
    while len(buf) > 0:
        hasher.update(buf)
        buf = _file.read(block_size)
    _file.close()
    return hasher.hexdigest()


def find_duplicates(folder_path):
    dups = {}
    for dirpath, dirnames, filenames in os.walk(folder_path):
        print(f'Scanning the {folder_path}')

        for filename in filenames:
            path = os.path.join(dirpath, filename)
            file_hash = hashfile(path)
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups


def print_result(_dict):
    results = list(filter(lambda x: len(x) > 1, _dict.values()))
    if len(results) > 0:
        print('Duplicates found')
        for res in results:
            print(res)


if __name__ == '__main__':
    folder_path = input("Enter folder path > ")
    duplicates = find_duplicates(folder_path)
    print_result(duplicates)