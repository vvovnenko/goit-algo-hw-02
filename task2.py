from collections import deque


def is_palindrome(string: str) -> bool:
    deq = deque(list(string.lower().replace(' ', '')))

    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False

    return True


while True:
    user_input = input("Enter a string ('q' to exit): ")

    if user_input == 'q':
        break

    if is_palindrome(user_input):
        print('True')
    else:
        print('False')

