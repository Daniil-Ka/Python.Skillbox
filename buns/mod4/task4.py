def generate_palindrome(word):
    char_counts = dict()

    for char in word:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_chars = [char for char, count in char_counts.items() if count % 2]

    if len(odd_chars) > 1:
        raise ValueError(f'Невозможно составить палиндром из данного слова: {word}')

    half = ''.join((char * (count // 2) for char, count in char_counts.items()))
    palindrome = half + odd_chars.pop() + half[::-1]

    return palindrome


word = input().strip()
print(generate_palindrome(word))
