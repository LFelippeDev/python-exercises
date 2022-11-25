"""Module to translate a word or sentence into Pig Latin."""


def first_letters_in_word_sound_vowel(word):
    """Check if the first letter of the word is a vowel."""
    if word[:2] == "xr" or word[:2] == "yt":
        return True
    return word[0] in "aeiou"


def is_consonant_consecutive_by_qu(word):
    """Return if the consonant is consecutive by qu."""
    if word[1:3] == "qu":
        return 1
    if word[:2] == "qu":
        return 2
    return 0


def has_a_y_after_consonant_cluster(text):
    """Return if the word has a y after a consonant cluster."""
    if len(text) == 2 and text[1] == "y":
        return True

    consonant_sequence = 0
    for letter in text:
        if letter == "y" and consonant_sequence > 1:
            return True
        if letter in "aeiou":
            consonant_sequence = 0
        if letter not in "aeiouy":
            consonant_sequence += 1
    return False


def first_vowel_index(word):
    """Return the first consonant sound of a word."""
    for index, letter in enumerate(word):
        if letter in "aeiou":
            return index


def translate(text):
    """Translate a word or sentence into Pig Latin."""
    if first_letters_in_word_sound_vowel(text):
        return f"{text}ay"
    if 0 < is_consonant_consecutive_by_qu(text) < 3:
        limit = is_consonant_consecutive_by_qu(text)
        return f"{text[limit:]}{text[:limit]}ay"
    if has_a_y_after_consonant_cluster(text):
        first_word = text.split("y")[1]
        second_word = text.split("y")[0]
        return f"{first_word}y{second_word}ay"
    limit = first_vowel_index(text)
    return f"{text[limit:]}{text[:limit]}ay"
