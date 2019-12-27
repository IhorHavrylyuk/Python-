from urllib.request import urlopen, Request
from threading import Thread
# 'https://png2jpg.com/images/png2jpg/icon.png'
CHUNK = 500


def create_request(url, start, end):
    _request = Request(url)
    _request.add_header('Range', f'bytes={str(start)}-{str(end)}')
    return _request


def fill_file(end, response):
    with open(file_name, 'ab') as _file:
        _file.seek(end, 0)  # 0 - з початку файлу
        _file.write(bytearray(response.read()))


def thread_work(url, start, end, file_name):
    """задавати range скачування можна у header об'єкту Request"""
    response = urlopen(create_request(url, start, end))
    fill_file(end, response)


def download(url, download_size, file_name):
    """кожен потік закачує CHUNK=500 байт"""
    threads_count = 0
    start_bytes_board = 0
    end_bytes_board = CHUNK
    while True:
        if end_bytes_board > download_size:
            end_bytes_board = download_size

        thread = Thread(target=thread_work, args=(url, start_bytes_board, end_bytes_board, file_name))

        thread.start()
        threads_count += 1
        thread.join()

        start_bytes_board = end_bytes_board
        end_bytes_board += CHUNK
        if start_bytes_board == download_size:
            break

    print(f'{threads_count} threads are working!')


if __name__ == '__main__':
    _url = input('Enter file url > ')
    file_name = input('Enter file name > ')
    file_info = dict(urlopen(_url).info())
    file_size = int(file_info['Content-Length'])
    download(_url, file_size, file_name)