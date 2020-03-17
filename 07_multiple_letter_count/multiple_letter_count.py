def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    let_freq = {}
    for letter in phrase:
        if letter not in let_freq:
            let_freq[letter] = 1
        else:
            let_freq[letter]+= 1

    return let_freq

    # comprehension



print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))