def is_palindrome(string: str) -> bool:
    string = string.replace(" ","")
    return string == string[::-1]

def run():
    print(is_palindrome("ana"))


if __name__ == '__main__':
    run()