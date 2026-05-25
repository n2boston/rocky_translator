import pyttsx3
import csv
import sys

class Translator:
    def __init__(self, file_path = "translator.csv"):
        """
        by default, would use translator.csv, but can provide a new csv file
        if training a dictionary from scratch is desired
        """
        self.dictionary = {}
        self.file_path = file_path
        self.load_dictionary()
    
    def load_dictionary(self):
        try:
            with open(self.file_path) as file:
                reader = csv.reader(file)
                for k, v in reader:
                    self.dictionary[int(k)] = v
        except FileNotFoundError:
            print(f"new translator dictionary will be created as {self.file_path}")
            if self.file_path == "translator.csv":
                self.dictionary = Translator.sample_dict
                self.update_database()
    
    def get_notes(self):
        """
        input to be replaced with musical input snippets
        for now, asking users to provide integers that represent 
        notes via command line input
        """
        notes = input("musical notes: ").split()
        notes = [int(note) for note in notes]
        return notes
    
    def convert_notes(self, notes):
        phrase = ""
        for note in notes:
            if note not in self.dictionary:
                self.add_new_word(note)
            phrase += self.dictionary[note] + " "
        return phrase
    
    def say(self, s: str):
        pyttsx3.speak(s)
        print(s)
    
    def add_new_word(self, note):
        self.say(f"{note} not in dictionary")
        answer = input(f"Enter definition for {note}: ")
        self.dictionary[note] = answer.strip()
        self.update_database()


    def update_database(self):
        with open(self.file_path, "w") as file:
            writer = csv.writer(file)
            writer.writerows(self.dictionary.items())
    
    def translate(self):
        try:
            while True:
                notes = self.get_notes()
                phrase = self.convert_notes(notes)
                self.say(phrase)
        except KeyboardInterrupt:
            sys.exit("\n Goodbye!")


    def demo():
        print("Translate.translate() works like this (make sure sound is on):")
        print("musical notes: 0 1 2 3 4")
        pyttsx3.speak("Grace and Rocky save stars ")
        print("Grace and Rocky save stars ")
        print("musical notes: 5 5 5")
        pyttsx3.speak("amaze amaze amaze ")
        print("amaze amaze amaze ")
        print("musical notes: 9 10 11 12")
        pyttsx3.speak("you sleep I watch ")
        print("you sleep I watch ")
        print("usical notes: 28 29 30")
        pyttsx3.speak("fist my bump")
        print("fist my bump ")
    
    
    sample_dict = {
        0: "Grace",
        1: "and",
        2: "Rocky",
        3: "save",
        4: "stars",
        5: "amaze",
        6: "bad",
        7: "question",
        8: "statement",
        9: "you",
        10: "sleep",
        11: "I",
        12: "watch",
        13: "good",
        14: "life",
        15: "is",
        16: "reason",
        17: "understand",
        18: "die",
        19: "no",
        20: "hello",
        21: "Erid",
        22: "Adrian",
        23: "Taumeba",
        24: "kill",
        25: "Astrophage",
        26: "hydrogen",
        27: "Blip A",
        28: "fist",
        29: "my",
        30: "bump",
    }

def main():
    demo = input("do you want a demo? (Y/N) ")
    if demo.lower() == "y" or demo.lower() == "yes" :
        Translator.demo()
    #add a CSV filepath in Translator init to start with an empty dictionary (e.g., "output.csv")
    to_english = Translator()
    to_english.translate()

if __name__ == "__main__":
    main()
