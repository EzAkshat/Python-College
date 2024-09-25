message = input(">")
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