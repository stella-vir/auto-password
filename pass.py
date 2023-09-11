import random
import string

def generate_password(words):
    password = ""

    for word in words:
        random_index = random.randint(0, len(word) - 1)
        word = word[:random_index] + word[random_index].upper() + word[random_index + 1:]

        twisted_word = ''.join(random.sample(word, len(word)))

        password += twisted_word

    password += str(random.randint(0, 9))
    password += random.choice(string.punctuation)

    return password


prompt_words = []

first_word = input("1. Give the first word: ")
prompt_words.append(first_word)

second_word = input("2. Give the second word: ")
prompt_words.append(second_word)

third_word = input("3. Give the third word: ")
prompt_words.append(third_word)

print("You entered:", prompt_words)


generated_password = generate_password(prompt_words)
print("Generated Password:", generated_password)
