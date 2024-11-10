import random
LETTER_SCORES = {
    "А":1, "Б":3, "В":1, "Г":3, "Д":2, "Е":1, "Ё":3, "Ж":5, "З":5, "И":1,
    "Й":4, "К":2, "Л":2, "М":2, "Н":1, "О":1, "П":2, "Р":1, "С":1, "Т":1,
    "У":2, "Ф":10, "Х":5, "Ц":5, "Ч":5, "Ш":8, "Щ":10, "Ъ":10,"Ы":4, "Ь":3,
    "Э":8, "Ю":8, "Я":3
}
converted_dictionary = list(LETTER_SCORES.keys())


def get_random_letter():
    random_letter = random.choice(converted_dictionary)
    return random_letter
    

def get_word_with_letter(first_letter):
    print(f"Первая буква - {first_letter}")
    number = 0
    players_info = []
    while number <2:
        number+=1
        input_word = input(f"Игрок {number}\nВведите слово на букву {first_letter}: ").upper()
        if len(input_word) == 0:
            print("ВВЕДИ СЛОВО БАЛДА")
            number-=1
            continue
        elif input_word[0] != first_letter:
            print(f"Слово должно начинаться на букву {first_letter}. Попробуйте снова") 
            number-=1
            continue
        else:
            player_word = input_word
            player_scores = calculate_score(input_word)
            players_info.append({"word":player_word, "scores":player_scores})
    return players_info
        
    
def calculate_score(word):
    all_scores = []
    for symbol in word:
        scores = LETTER_SCORES.get(symbol)
        all_scores.append(scores)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    first_letter = get_random_letter()
    player_results = get_word_with_letter(first_letter)
    for x in range(2):
        print(f"Игрок {x+1} ввел слово '{player_results[x]["word"]}' и набрал {player_results[x]["scores"]} очков")
    if player_results[0]["scores"] > player_results[1]["scores"]:
        print("Победил игрок 1!")
    elif player_results[0]["scores"] < player_results[1]["scores"]:
        print("Победил игрок 2!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    main()
