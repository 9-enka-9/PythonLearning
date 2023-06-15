#Blackjack project

################### HƯỚNG DẪN CHƠI ########################
# Để bắt đầu trò chơi thì ấn nút Run ở phía trên
#
# 'Do you want to play a game of blackjack? Type 'y' to play, type 'n' to stop program:'
# nghĩa là bạn có muốn chơi bài xì lác không, nếu có thì gõ 'y' nếu không thì gõ 'n'
# Khi bạn nhập vào 'n' thì lập tức chương trình sẽ dừng, nếu bạn nhập 'y' thì ván bài sẽ bắt đầu 
#
# 'Type 'y' to get another card. Type 'n' to pass.' nghĩa là gõ 'y' để rút bài, gõ 'n' để bỏ qua không rút nữa
# Nếu bạn chọn 'y' thì máy sẽ tự ngẫu nhiên chọn một lá cho bạn, nếu bạn chọn 'n' thì máy sẽ rút bài và hiện luôn
# kết quả ra màn hình
#
# 'Your cards:' có nghĩa là những lá bài của bạn
# 'Your score:' có nghĩa là điểm của bạn là
# 'Your final score:' là điểm cuối cùng của bạn
# 'Computer's first card:' có nghĩa là một lá bài đầu tiên của máy tính
# 'Computer's score:' là điểm của máy tính
# 'Computer's final cards:' là những lá bài của máy tính sau khi rút xong
# 'Computer's final score:' là số điểm của máy tính
# 
# Trong đó Jack là lá J, King là K, Queen là Q và đều có giá trị là 10
# Ace là át, nó vừa có giá trị là 1, vừa có giá trị là 11, nếu như số điểm của bạn lớn hơn 10 
# thì tự động giá trị của Ace sẽ quy về 1 để khiến số điểm của bạn không vượt quá 21
# Lần lượt như thế thì Two là 2, Three là 3,...
# Đến khi nào bạn không muốn rút nữa hoặc số điểm bạn đã lớn hơn hoặc bằng 21 thì 
# máy sẽ tự động đưa ra kết quả cuối cùng của bạn và máy tính
# 
# 'I lose, you win' là tôi thua, bạn thắng tức là máy thua, bạn thắng
# 'I win, you lose' là tôi thắng bạn thua tức là máy thắng, bạn thua
# 'We are even' là chúng ta huề nhau
#
# Để biết được ai thắng ai thua thì rất đơn giản, ai có số điểm lớn hơn và không vượt quá 21 thì thắng
# Nếu cả hai có giá trị bằng nhau hoặc đều lớn hơn 21 thì hòa
#
# P/S: trò chơi không mất tiền, chỉ mang tính giải trí
################### HƯỚNG DẪN CHƠI ########################

################### Start Code ########################
from os import system, name
from tabnanny import check
from tkinter import Y
from art import logo
import random
import time
play=input("Do you want to play a game of blackjack? Type 'y' to play, type 'n' to stop program: ")
time.sleep(1)
player_cards=[]
dealer_cards=[]
get_card='y'


def check_ace(this_cards, this_score_without_ace):
    if 'Ace' in this_cards and this_score_without_ace>10:
        return this_score_without_ace+1
    elif 'Ace' in this_cards and this_score_without_ace<=10:
        return this_score_without_ace+11
    else:
        return calc_score(this_cards)
    
def calc_score(calc_cards):
    the_score=0
    for card in calc_cards:
        the_score+=cards[card]
    return the_score

def random_cards():
    random_card=random.choice(list(cards.keys()))
    return random_card
    
def check_score(dealer_score, player_score):
    time.sleep(1)
    if (dealer_score > 21 and player_score > 21) or (dealer_score == player_score):
        print("---We are even.---")
    elif dealer_score<=21 and player_score<=21:
        if dealer_score>player_score:
            print("---I win, you lose.---")
        else:
            print("---I lose, you win.---")
    elif dealer_score<=21 and player_score>21:
        print("---I win, you lose.---")
    else:
        print("---I lose, you win.---")   

while play=='y':
    if name == "nt":
        _=system("cls")
    else:
        _=system("clear")
    
    player_cards=[]
    dealer_cards=[]
    print(logo)
    cards={'Jack':10, 'King':10, 'Queen':10, 'Ace': 11, 'Ten':10, 'Nine':9, 'Eight':8, 'Seven':7, 'Six': 6, 'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2,}
    
    player_cards.append(random_cards())
    dealer_cards.append(random_cards())
    get_card='y'
    
    # Người chơi rút bài 
    while get_card=='y':
        player_cards.append(random_cards())
        player_score_without_Ace=calc_score(player_cards)-11
        player_score=check_ace(player_cards, player_score_without_Ace)
        print(f"   Your cards: {player_cards}. Your score: {player_score}.")
        time.sleep(1)
        print(f"   Computer's first card: {dealer_cards}. Computer's score: {calc_score(dealer_cards)}.")
        time.sleep(1)
        if player_score>=21:
            break
        else:
            get_card=input("Type 'y' to get another card. Type 'n' to pass: ")

    # Máy rút bài 
    dealer_score=calc_score(dealer_cards)
    while dealer_score<17:
        dealer_cards.append(random_cards())
        dealer_score_without_Ace=calc_score(dealer_cards)-11
        dealer_score=check_ace(dealer_cards, dealer_score_without_Ace)
    
    time.sleep(1)
    print(f"***Your final cards: {player_cards}. Your final score: {player_score}.")
    time.sleep(1)
    print(f"***Computer's final cards: {dealer_cards}. Computer's final score: {dealer_score}.")
    check_score(dealer_score,player_score)
    play=input("Do you want to play a game of Blackjack? Type 'y' to play, type 'n' to stop program: ")
################### End Code ########################  