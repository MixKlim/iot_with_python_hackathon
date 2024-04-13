# Implement here
from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": " ",
}

input_message = input("Enter your input message: ")
print(f"Message entered: {input_message}")
while True:
    try:
        for letter in input_message.upper():
            morse_code = MORSE_CODE_DICT.get(letter)
            for ch in morse_code:
                if ch == ".":
                    pin.toggle()
                    sleep(1)
                    pin.off()
                    sleep(1)
                elif ch == "-":
                    pin.toggle()
                    sleep(3)
                    pin.off()
                    sleep(1)
                elif ch == " ":
                    sleep(7)
                    break
            sleep(3)

        print("Finished.")
    except KeyboardInterrupt:
        break
