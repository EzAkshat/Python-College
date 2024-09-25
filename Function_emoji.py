def Emoji(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😔",
        "<3": "❤️"
}
    output = ""
    for emoji in words:
        output += emojis.get(emoji,emoji)+" "
        print(output)
        return output

message = input(">")
Emoji(message)
print(Emoji)