dic = {'"': '&quot', '&': '&amp', '<': '&lt', '>': '&gt'}

def decorator(func):
    def wrapper(tag):
        func(tag)
        string = [x for x in tag]
        for x in range(len(string)):
            if string[x] in list(dic.keys()):
                string[x] = dic.get(string[x])
        return ''.join(string)
    return wrapper

@decorator
def show_string(string):
    return string

if __name__ == '__main__':
    value = input("Write your tag: ")
    print('Your escape HTML tag: ' + show_string(value))