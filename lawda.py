import random

def generate_random_number(start, end):
    """Generates a random integer between start and end (inclusive)."""
    return random.randint(start, end)

def generate_random_list(length, start, end):
    """Generates a list of random integers."""
    return [random.randint(start, end) for _ in range(length)]

def shuffle_list(data):
    """Shuffles the elements of a list in place."""
    random.shuffle(data)
    return data

if __name__ == "__main__":
    # Example usage
    random_number = generate_random_number(1, 100)
    print(f"Random number between 1 and 100: {random_number}")

    random_list = generate_random_list(10, 1, 10)
    print(f"Random list of 10 numbers between 1 and 10: {random_list}")

    my_list = [1, 2, 3, 4, 5]
    shuffled_list = shuffle_list(my_list)
    print(f"Shuffled list: {shuffled_list}")