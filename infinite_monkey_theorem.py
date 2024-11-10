import random
def generate_word(word_len):
    letters = "abcdefghijklmnopqrstuvwxyz "
    word = ""

    for i in range(word_len):
        word += letters[random.randint(0, 26)]
    return word


def score(goal_str, generated_str):
    score = 0
    for i in range(len(goal_str)):
        if goal_str[i] == generated_str[i]:
            score += 1
    score /= len(goal_str)
    return score

def best_score():
    goal_string = input("Enter the word in lowercase you want the monkey to type : ")
    scored = score(goal_string, generate_word(len(goal_string)))
    tracker = 1
    best = scored
    while best < 1:
        current_word = generate_word(len(goal_string))
        scored = score(goal_string, current_word)
        tracker += 1
        if scored > best:
            best, word = scored, current_word
    return best, word, tracker

def main():
    score, word, tracker = best_score()
    print(f"After {tracker} trials, our monkey finally typed the word '{word}'.")

main()
