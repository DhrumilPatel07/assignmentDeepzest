from itertools import permutations

def generate_anagrams(input_text):
    input_text = input_text.replace(" ", "").lower()
    permutations_list = [''.join(perm) for perm in permutations(input_text)]
    return list(set(permutations_list))

def find_word_anagrams(word, word_list):
    anagrams = []
    for candidate in word_list:
        if sorted(word) == sorted(candidate) and word != candidate:
            anagrams.append(candidate)
    return anagrams

choice = input("Enter '1' to generate anagrams or '2' to find anagrams from a list: ")

if choice == '1':
    input_text = input("Enter a word or phrase: ")
    anagrams = generate_anagrams(input_text)
    print("Anagrams:")
    for anagram in anagrams:
        print(anagram)
elif choice == '2':
    input_word = input("Enter a word: ")
    word_list = ["enlist", "inlets", "silent", "banana", "tinsel"]
    anagrams = find_word_anagrams(input_word, word_list)
    if anagrams:
        print(f"Anagrams of '{input_word}': {', '.join(anagrams)}")
    else:
        print(f"No anagrams of '{input_word}' found in the list.")
else:
    print("Invalid choice.")
