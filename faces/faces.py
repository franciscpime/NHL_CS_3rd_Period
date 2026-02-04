def main():
    message = input("Write a message: ")
    print(convert(message))


def convert(message):
    emojis = {
        ":)": "🙂",
        ":(": "🙁",
        ":D": "😄",
        ";)": "😉",
        ":/": "😐",
        "xD": "😵",
        ":O": "😮"
    }

    for c in emojis:
        message = message.replace(c, emojis[c])

    return message


main()
