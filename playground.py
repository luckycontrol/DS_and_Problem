def run():
    pass

def my_decorator(func):
    print("before called")
    func()
    print("after called")

@my_decorator
def say_hello():
    print("Hello!")

if __name__ == '__main__':
    run()