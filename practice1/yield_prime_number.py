#!/usr/bin/python

def list_primes(num):
    for n in range(1, num+1):
        if(len(list(list_factors(n))) == 2):
            yield(n)

def list_factors(num):
    for n in range(1, num+1):
        if (num % n) == 0:
            yield(n)

def get_next_prime(num):
    num = num + 1
    while(len(list(list_factors(num))) != 2):
        num = num + 1
    return num

def generate_primes(count):
    primes = []
    prime_temp = 2
    if (count == 0):
        return []
    elif (count == 1):
        return [2]
    else:
        while(len(primes) != count):
            primes.append(prime_temp)
            temp = get_next_prime(prime_temp)
            prime_temp = temp
    return(primes)


if __name__ == "__main__":
    print(list(list_primes(int(input("List all prime numbers between (1, num). Enter a number: ")))))
    print(get_next_prime(int(input("Given a number find the next prime number. Enter a number: "))))
    print(generate_primes(int(input("Given a number n generate first n prime numbers. Enter a number: "))))
