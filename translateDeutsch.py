import json

def translateNumber(number: int):

    timeDeutsch: str

    with open(file="translateData.json", mode="r", encoding="utf-8") as f:
        file_json = json.load(f)

        if number == 0:
            timeDeutsch = file_json["under12"][0]

        elif number%10 == 0:
            timeDeutsch = file_json["divisible"][(number-1) // 10]

        elif number <= 12:
            timeDeutsch = file_json["under12"][number]

        elif number == 16:
            timeDeutsch = file_json["under12"][13]

        elif number == 17:
            timeDeutsch = file_json["under12"][14]

        elif number > 12 and number < 20:
            under12 = file_json["under12"][number%10]
            timeDeutsch = f"{under12}zehn"

        elif number > 12 and number < 60:
            divisible = file_json["divisible"][number//10 - 1]
            under12 = file_json["under12"][number%10]
            timeDeutsch = f"{under12}und{divisible}"

        else:
            timeDeutsch = "ZERO"

    return timeDeutsch


def translateTime(hour: int, minutes: int, second: int):
    if minutes == 0:
        timeDeutsch: str = f""
    
    elif minutes == 15:
        timeDeutsch: str = f""

    elif minutes == 30:
        timeDeutsch: str = f""

    elif minutes == 45:
        timeDeutsch: str = f""