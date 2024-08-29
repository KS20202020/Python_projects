with open("story.txt", "r") as f:
    text = f.read()

words = set()
start_of_word = -1

target_start = "["
target_end = "]"

for i, char in enumerate(text):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = text[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"Enter a word {word} : ")
    answers[word] = answer

for word in words:
    text = text.replace(word, answers[word])

print(text)
