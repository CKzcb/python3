from a import aa

def bb():
    aa()
    print(__name__)
    print("this is b")

if __name__ == '__main__':
    bb()