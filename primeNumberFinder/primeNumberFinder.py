import math

'''
    We want to find all the prime numbers within a range given by the user. 
    ChatGPT Hint: You can check to see if a number is prime by dividing by each number all the way until
                it's square root.
'''
'''
while True:
    try:
        print('This program will give you all prime numbers within your given range!!!')
        start_num = int(input('Enter a number above 0 to start the range:'))
        end_num = int(input('Enter a number above 0 to end the range:'))

        if start_num < 1 or end_num < 1:
            print('Invalid input. Number is below 1. Try again!!!')
            continue
        elif start_num > end_num:
            print('Invalid input. The first number has to be below second number. Try again!!!')
            continue
        else:
            break
    except ValueError:
        print('Oops not a valid number. Try again!!!')
        continue

for potential_prime_num in range(start_num, end_num+1):
    for i in range(2, int((potential_prime_num**0.5))+1):
        if potential_prime_num % i == 0:
            continue
        else:
            print(potential_prime_num)
'''

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(start, end):
    prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
    return prime_numbers

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    primes = find_primes(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")

if __name__ == "__main__":
    main()
