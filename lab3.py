def add_tag(tag=""):
    def decorator(func):
        def wrapper(string):
            return "<"+tag+">"+func(string)+"</"+tag+">"
        return wrapper
    return decorator

@add_tag("div")
def get_string(string):
    return string

if __name__ == '__main__':
    text = input("Write your HTML text: ")
    print(get_string(text))