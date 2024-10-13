import json

number = 10

with open(file="translateData.json", mode="r", encoding="utf-8") as f:
    file_json = json.load(f)
    if number%10 == 0:
        print(file_json["divisible"][number//10])
    else:
        print("moemoe")