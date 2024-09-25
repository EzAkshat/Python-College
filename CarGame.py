Cmd = ""
car_started = False  

while True:
    Cmd = input("> ").lower()
    if Cmd == "start":
        if car_started:
            print("Car is already started...Ready to go")
        else:
            car_started = True
            print("Car started...Ready to go")
    elif Cmd == "stop":
        if not car_started:
            print("Car is already stopped.")
        else:
            car_started = False
            print("Car stopped.")
    elif Cmd == "help":
        print(
            """Start = to start the car
Stop = to stop the car
Quit = to Quit"""
        )
    elif Cmd == "quit":
        break
    else:
        print("I don't understand that...")