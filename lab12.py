import sys, os
import hashlib
from threading import Thread
PATHS_FOR_THREAD = 100


def get_all_paths(_path):
    files_list = []
    for dir_path, dir_names, file_names in os.walk(folder_path):
        for _file_name in file_names:
            files_list.append(dir_path + '/' + _file_name)
    return files_list


def hashfile(path, block_size=1024):
    """
        рахуємо MD5 hash файлу по заданому path
        :return HEX digits of file
    """
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
    all_paths = get_all_paths(folder_path)
    count_paths = len(all_paths)
    threads = []
    start_path_num = 0
    end_path_num = PATHS_FOR_THREAD
    while True:
        if end_path_num > count_paths:
            end_path_num = count_paths

        thread = Thread(target=thread_work, args=(all_paths, start_path_num, end_path_num, dups))
        threads.append(thread)
        thread.start()

        start_path_num = end_path_num
        end_path_num += PATHS_FOR_THREAD
        if start_path_num == count_paths:
            break
    for thread in threads:
        thread.join()
    return dups


def thread_work(all_paths, start_path_num, end_path_num, dups):
    for i in range(start_path_num, end_path_num):
        file_hash = hashfile(all_paths[i])
        if file_hash in dups:
            dups[file_hash].append(all_paths[i])
        else:
            dups[file_hash] = [all_paths[i]]


def print_result(_dict):
    results = list(filter(lambda x: len(x) > 1, _dict.values()))
    if len(results) > 0:
        print('Duplicates found')
        for res in results:
            print(res)
    else:
        print('None duplicates')


if __name__ == '__main__':
    # C:\Users\Ihor\Desktop
    folder_path = input("Enter folder path > ")
    duplicates = find_duplicates(folder_path)
    print_result(duplicates)