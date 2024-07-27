def count_letters(string: str) -> tuple[int, int]:
    """
    Count the number of vowels and consonants in a string

    Parameters
    ----------
    string: str
        The string to count the vowels and consonants in

    Returns
    -------
    tuple[int, int]
        A tuple containing the number of vowels and consonants in the string
    """
    vowels = consonants = 0
    for letter in string.lower():
        if letter in "aeiou":
            vowels += 1
        elif letter.isalpha():
            consonants += 1
    return vowels, consonants


if __name__ == "__main__":
    string = input("Enter a string: ")
    vowels, consonants = count_letters(string)
    print(f"It contains Vowels: {vowels}, Consonants: {consonants}")