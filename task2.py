from collections import deque


def is_palindrome(string: str) -> bool:
    deq = deque(list(string.strip().lower()))

    for _ in range(int(len(deq)/2)):
        if deq.pop() != deq.popleft():
            return False

    return True
