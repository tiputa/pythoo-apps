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

ken = random.choice(list(dict.keys()))

print("これから出す都道府県の名産品（食べ物）を答えよ")
answer = input(f"{ken}の名産品は？：")

if answer == dict[ken]:
    print("正解")
else:
    print("不正解")
print(f"{ken}の名産品は{dict[ken]}です")
print("お疲れ様でした")
print("次の問題に行きます")