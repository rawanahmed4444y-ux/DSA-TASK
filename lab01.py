def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


seconds = int(input("Enter seconds: "))
print(seconds_to_hms(seconds))

def celsius_to_fahrenheit(celsius):
    fehrnhit = celsius*1.8 + 32
    return fehrnhit
celsius = float(input("Enter celisus: "))
print (round(celsius_to_fahrenheit(celsius)))

def split_evenly(people, total):
    naseb_elfard = total // people 
    elba2y = total%people
    return naseb_elfard , elba2y
total = float(input("Enter total: "))
people = int(input("Enter people num: "))
print (split_evenly(people, total))


def initials(full_name):
    words = full_name.split()
    result = ""
    i = 0
    while i < len(words):
        result += words[i][0]
        i += 1
    return result

name_input = input("Enter full name: ")
print(initials(name_input))

def is_palindrome_word(word):
    final_word = word.strip().lower()
    return final_word == final_word[::-1]

user_word = input("Enter a word: ")
print(is_palindrome_word(user_word))

def mask_email(email):
    at_pos = email.index("@")
    user = email[:at_pos]
    domain = email[at_pos:]
    
    if len(user) <= 2:
        masked_user = user
    else:
        masked_user = user[0] + ("*" * (len(user) - 2)) + user[-1]
        
    return masked_user + domain

email_input = input("Enter email: ")
print(mask_email(email_input))


def middle(values):
    mid = len(values) // 2
    if len(values) % 2 == 1:
        return values[mid:mid+1]
    else:
        return values[mid-1:mid+1]

data = input("Enter values separated by spaces: ").split()
print(middle(data))


def rotate_left(values, k):
    if len(values) == 0:
        return values[:]
    shift = k % len(values)
    return values[shift:] + values[:shift]

items = input("Enter items separated by spaces: ").split()
steps = int(input("Enter k: "))
print(rotate_left(items, steps))


def fib_list(n):
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result

num = int(input("Enter n: "))
print(fib_list(num))

def fib_list(n):
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result

num = int(input("Enter n: "))
print(fib_list(num))