def is_prime(number: int) -> bool:
    for n in range(2,number):
        if n != number and number % n == 0 :
            return False
    return True

def run():
    print(is_prime(137))

if __name__ == '__main__':
    run()