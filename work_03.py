import random
dict = {
    "福岡県":"明太子",
    "佐賀県":"佐賀牛",
    "長崎県":"カステラ",
    "熊本県":"馬刺し",
    "大分県":"農後牛",
    "宮崎県":"マンゴー",
    "鹿児島県":"黒牛",
    "沖縄県":"黒糖"
}

a = random.choice(list(dict.keys()))

print("これから出す都道府県の名産品（食べ物）を答えよ")


a = input(a)

if a == input():
    print("正解")
else:
    print("不正解")