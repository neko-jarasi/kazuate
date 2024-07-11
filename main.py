import random

def main():
    namber=random.randint(1,100)

    for i in range(1,8):
        Q=int(input("1~100までの整数を入力してください  "))
        if namber>Q:
            print("high")
        elif namber<Q:
            print("low")
        else:
            print("正解!")
            break
        
def yorn():
    print("もう一度遊ぶ？")
    yesno=input("yesかnoで答えてね  ")
    if yesno=="yes" or yesno=="y":
        main()
    elif yesno=="no" or yesno=="n":
        print("このゲームを終了するよ")
    else:
        print("yesかnoもしくはyかnで答えてね")
        yorn()
        
main()
yorn()
