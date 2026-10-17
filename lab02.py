#-1
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("not a valid triangle")
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

#-2
def course_result(coursework, final, attendance):
    if not (0 <= coursework <= 40 and 0 <= final <= 60 and 0 <= attendance <= 100):
        raise ValueError("score out of range")
    if attendance < 75:
        return "fail"
    if final < 24:
        return "fail"
    total = coursework + final
    if total >= 85:
        return "distinction"
    elif total >= 50:
        return "pass"
    else:
        return "fail"

#-3
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

#-4
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

#-5
def primes_below(n):
    return [k for k in range(2, n) if is_prime(k)]

#-6
def first_repeated(values):
    for j in range(len(values)):
        for i in range(j):
            if values[i] == values[j]:
                return values[j]
    return None

#-7
def count_pairs_loop(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count

def count_pairs(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    return n * (n - 1) // 2

#-8
def calculator(command):
    match command.split():
        case ["add", a, b]:
            return float(a) + float(b)
        case ["sub", a, b]:
            return float(a) - float(b)
        case ["mul", a, b]:
            return float(a) * float(b)
        case ["div", a, b]:
            if float(b) == 0:
                raise ValueError("division by zero")
            return float(a) / float(b)
        case ["neg", a]:
            return -float(a)
        case ["sum", *nums] if nums:
            return sum(float(x) for x in nums)
        case _:
            raise ValueError(f"unknown command: {command!r}")

#-9
def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default

#-10
def stats(*numbers):
    if not numbers:
        raise ValueError("stats() needs at least one number")
    lo = hi = numbers[0]
    for x in numbers[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi

#-11
def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

#-12
def make_multiplier(k):
    def multiply(x):
        return x * k
    return multiply

#-13
def apply_n(f, x, n):
    for _ in range(n):
        x = f(x)
    return x