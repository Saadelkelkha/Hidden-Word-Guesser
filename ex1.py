def is_valid_word(m):
    # Check if the word length is between 4 and 25 characters
    if 4 <= len(m) <= 25:
        f = "true"
    else:
        f = "false"
    i = 0
    while True:
        # Check if each character in the word is an uppercase letter
        if 65 <= ord(m[i]) <= 90:
            q = "true"
        else:
            q = "false"
        i = i + 1
        if q == "false" or len(m) == i:
            break
    # Return "true" if both length and character criteria are met, otherwise "false"
    if f == "false" or q == "false":
        return "false"
    else:
        return "true"


def is_letter_in_word(m, a):
    i = 0
    f = "false"
    while True:
        # Check if the guessed letter is in the word
        if a == m[i]:
            f = "true"
        i = i + 1
        if i == len(m):
            return f


hidden_word = []

while True:
    # Input the word and check if it's valid
    m = str(input("Enter the word: "))
    n = is_valid_word(m)
    if n == "true":
        break

for i in range(0, len(m)):
    # Initialize the hidden word with asterisks
    hidden_word.append("*")

j = 0
w = 5

while True:
    # Input a character and check if it has been guessed before
    a = input("Enter a character: ")
    if a in hidden_word:
        while True:
            a = input("This letter was guessed before. Please type another letter: ")
            if a in hidden_word:
                continue
            else:
                break

    for i in range(0, len(m)):
        # Update the hidden word if the guessed letter is in the word
        if a == m[i]:
            hidden_word[i] = m[i]
            j = j + 1
    print(hidden_word)

    n = is_letter_in_word(m, a)
    # Update the attempts left based on whether the guessed letter is in the word
    if n == "false":
        w = w - 1
    print("ATTEMPTS LEFT:", w)

    # Check if the word is fully guessed or if there are no attempts left
    if j == len(m) or w == 0:
        break

if w == 0:
    print("LOSE")
else:
    print("WIN")