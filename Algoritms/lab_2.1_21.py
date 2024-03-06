n, m, r = input().split()
def_cards = list(map(str, input().split()))
att_cards = list(map(str, input().split()))
ranks = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
def_cards.sort(key=lambda x: (not x[1].startswith(r), ranks.index(x[0])))
att_cards.sort(key=lambda x: (not x[1].startswith(r), ranks.index(x[0])))

for card in att_cards:
    for card_def in def_cards:
        if card_def != -1 and ranks.index(card[0]) <= ranks.index(card_def[0]) and card[1] == card_def[1]:
            def_cards[def_cards.index(card_def)] = -1
            att_cards[att_cards.index(card)] = -1
            break
    else:
        if card[1] == r:
            print('NO')
            exit()
        else:
            for card_def in def_cards:
                if card_def != -1 and card_def[1] == r:
                    def_cards[def_cards.index(card_def)] = -1
                    att_cards[att_cards.index(card)] = -1
                    break
            else:
                print('NO')
                exit()
else:
    print('YES')
#Работает!!!!!!



# 6 2 C
# KD KC AD 7C AH 9C
# 6D 6C

# 5 4 C
# 8C KH 7H 6C AK
# 6C 6K AK KH
