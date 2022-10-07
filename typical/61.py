from tkinter import N


N = int(input())
front_cards=[]
back_cards=[]
for i in range(N):
    t, x = map(int,input().split())
    if t==1:
        front_cards.append(x)
    if t==2:
        back_cards.append(x)
    if t==3:
        if len(front_cards)>=x:
            print(front_cards[-x])
        else:
            print(back_cards[x-len(front_cards)-1])
            