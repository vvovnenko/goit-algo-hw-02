from collections import deque


def is_palindrome(string: str) -> bool:
    deq = deque(list(string.strip().lower()))

    for _ in range(int(len(deq)/2)):
        if deq.pop() != deq.popleft():
            return False

    return True


while True:
    user_input = input("Enter a string ('q' to exit): ")

    if user_input == 'q':
        break

    if is_palindrome(user_input):
        print('The string is a palindrome')
    else:
        print('The string is NOT a palindrome')

