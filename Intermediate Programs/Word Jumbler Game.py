import random
from datetime import datetime

my_words = (("questionnaire", "noun", "a list of questions survey"),
            ("unconscious", "adjective", "not conscious or without awareness"),
            ("precocious", "adjective", "unusually mature, especially in mental development"),
            ("liaison", "noun", "a person who maintains a connection between people or groups"),
            ("surveillance", "noun", "continuous observation of a person, place, or activity in order to gather information"),
            ("malfeasance", "noun", "conduct by a public official that violates the public trust or is against the law"),
            ("irascible", "adjective", "irritable, quick-tempered"),
            ("idiosyncrasy", "noun", "a tendency, habit or mannerism that is peculiar to an individual; a quirk"),
            ("foudroyant", "adjective", "sudden and overwhelming or stunning"),
            ("eudemonic", "adjective", "pertaining to conducive to happiness"))

record = ()


def shuffler(word):
  characters_list = list(word)
  random.shuffle(characters_list)
  shuffled = "".join(characters_list)
  return shuffled


score = 0
player_name = input("Enter your name: ")

print("GUESS A WORD GAME".center(78, "-"))
print("If you want to end the the game, type 's'")

start = datetime.now()

for i in range(len(my_words)):

    word = my_words[i][0]
    shuffled_word = shuffler(word)

    print(f"""Jumbled Letters: {shuffled_word}
Part of speech: {my_words[i][1]}
Meaning: {my_words[i][2]}""")

    user_input = input("Enter your guess: ").lower()

    if user_input == "s":
        break
    elif user_input == word:
        print("Correct!")
        print()
        score += 1
    else:
        print("Wrong!")
        print("Correct word: " + word.upper())
        print()

total_time = datetime.now() - start
minutes = (total_time.seconds // 60) % 60
seconds = total_time.seconds - (minutes * 60)
print(f"You took {minutes} minute(s) and {seconds} seconds to guess {score} words correctly")
print()

print(f"""Complete word list
{"-" * 125}
##|{"Word".rjust(15, " ")}|{"Parts Of Speech".rjust(10, " ")}|Meaning""")

for i in range(len(my_words)):
    print(
        f"""{str(i + 1).rjust(2, "0")}|{my_words[i][0].capitalize().rjust(15, " ")}|{my_words[i][1].capitalize().rjust(15, " ")}| {my_words[i][2].capitalize()}
{"-" * 125}""")

print()

player_record = ({
                     "Name": player_name,
                     "Guess Count": score,
                     "Time Taken": f"{minutes}:{seconds}"
                 },)

records = records + player_record

print(f"""LEADERBOARD
{"-" * 125}""")

for i in range(len(records)):

    player_indentification = list(records[i].keys())
    player_attributes = list(records[i].values())

    for j in range(3):
        print(f"{player_indentification[j]}: {player_attributes[j]}")

    print()