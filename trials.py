"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_numbers = []

    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


def get_odd_indices(items):

    odd_indices_num = []

    for index in range(len(items)):
        if index % 2 != 0:
            odd_indices_num.append(items[index])

    return odd_indices_num


def print_as_numbered_list(items):

    item_num = 1
    for item in items:

        print(f' {item_num}. {item}')
        item_num += 1


# print(print_as_numbered_list(['bird', 'pear tree', 'gift', 'coffee']))


def get_range(start, stop):
    num_lst = []

    for num in range(start, stop):
        num_lst.append(num)

    return num_lst


def censor_vowels(word):

    vowels_censor = []

    for letter in word:
        if letter in "aeiou":
            vowels_censor.append('*')
        else:
            vowels_censor.append(letter)

    return ''.join(vowels_censor)


def snake_to_camel(string):
    converted_to_camel = []

    # split_string = string.split('_')
    # for word in split_string:
    #     upper_cased = f"{word[0].upper()}{word[1:]}"
    #     converted_to_camel.append(upper_cased)

    for word in string.split('_'):
        converted_to_camel.append(f"{word[0].upper()}{word[1:]}")

    return ''.join(converted_to_camel)


def longest_word_length(words):
    longest = len(words[0])
    
    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest

def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
