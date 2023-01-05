import random

computer_score=0
player_score=0

print("Камень давит ножницы, ножницы режут бумагу, а бумага накрывает камень.")

computer_attack = ["камень","ножницы", "бумага"]
while True:
    if computer_score==10:
        print("Компьютер набрал 10 баллов и победил окончательно. Конец игры")
        break
    elif player_score==10:
        print("Ты набрал 10 баллов и победил окончательно. Конец игры")
        break
    print("Компьютер:", computer_score, "\nИгрок:", player_score)
    player = input("Выберите: камень, ножницы или бумага (выйти)?\n").lower()
    computer = random.choice(computer_attack)
    print("Твой выбор: ", player, "\nКомпьютер выбрал: ", computer)
    
    if player == computer:
        print("Ничья")
    
    
    elif player == "бумага":
        if computer == "камень":
            print("Ты победил!")
            player_score=player_score + 1
        else:
            print("Победил компьютер")
            computer_score=computer_score + 1
    elif player == "камень":
        if computer == "бумага":
            print("Ты победил!")
            player_score=player_score + 1
        else:
            print("Победил компьютер")
            computer_score=computer_score + 1
    elif player == "ножницы":
        if computer == "бумага":
            print("Ты победил!")
            player_score=player_score + 1
        else:
            print("Победил компьютер")
            computer_score=computer_score + 1
    elif player=="выйти":
        print("Вы вышли из игры")
        break
    
    else:
        print("Произошла ошибка")
