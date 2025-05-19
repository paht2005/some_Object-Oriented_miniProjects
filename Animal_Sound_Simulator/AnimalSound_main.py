# 🧬 Base entity class
class Animal:
    def make_sound(self):
        print("🔈 Some mysterious creature makes a sound...")

# 🐾 Derived animal classes with specific behaviors
class Dog(Animal):
    def make_sound(self):
        print("🐶 Dog barks: Woof woof!")

class Cat(Animal):
    def make_sound(self):
        print("🐱 Cat meows: Meow meow!")

class Cow(Animal):
    def make_sound(self):
        print("🐄 Cow moos: Moo moo!")

class Duck(Animal):
    def make_sound(self):
        print("🦆 Duck quacks: Quack quack!")

# 🔊 Sound board controller
class SoundBoard:
    def __init__(self):
        self.animal_queue = []

    def add_animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.animal_queue.append(animal)
            print(f"✅ {animal.__class__.__name__} was added to the sound board.")
        else:
            print("❌ Error: Only animals can be added to the sound board.")

    def play_sounds(self):
        if not self.animal_queue:
            print("📭 The sound board is empty. Add some animals first!")
            return
        print("\n🎵 All animals are making sounds:")
        for creature in self.animal_queue:
            creature.make_sound()

# 🎮 Simple console-based interaction
def launch_soundboard_console():
    board = SoundBoard()

    while True:
        print("\n===== 🎤 Animal SoundBoard Menu =====")
        print("1. Add a Dog")
        print("2. Add a Cat")
        print("3. Add a Cow")
        print("4. Add a Duck")
        print("5. Play All Animal Sounds")
        print("6. Exit Program")

        choice = input("Enter your choice (1–6): ").strip()

        match choice:
            case '1':
                board.add_animal(Dog())
            case '2':
                board.add_animal(Cat())
            case '3':
                board.add_animal(Cow())
            case '4':
                board.add_animal(Duck())
            case '5':
                board.play_sounds()
            case '6':
                print("👋 Goodbye! Thanks for playing.")
                break
            case _:
                print("⚠️ Invalid option. Please select a number between 1 and 6.")

# 🚀 Entry point
if __name__ == "__main__":
    launch_soundboard_console()
