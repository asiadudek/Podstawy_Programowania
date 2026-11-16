

def hide(card_number):
    first = card_number[0:2]
    last = card_number[-4:]
    stars = "*"*10
    return first+stars+last
