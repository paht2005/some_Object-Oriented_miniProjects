
# Base class
class Creature:
    def speak(self):
        print("An unknown creature makes a noise...")

# Derived classes
class Hound(Creature):
    def speak(self):
        print("🐶 Hound says: Bark bark!")

class Feline(Creature):
    def speak(self):
        print("🐱 Feline says: Meow meow!")

class Bovine(Creature):
    def speak(self):
        print("🐄 Bovine says: Moo moo!")

class Quacker(Creature):
    def speak(self):
        print("🦆 Quacker says: Quack quack!")

# Simulator class
class VoiceSimulator:
    def __init__(self):
        self.creature_list = []

    def insert_creature(self, creature):
        if isinstance(creature, Creature):
            self.creature_list.append(creature)
            print(f"{creature.__class__.__name__} has joined the voice simulator.")
        else:
            print("❌ This object is not a valid creature!")

    def play_all_sounds(self):
        if not self.creature_list:
            print("📭 No creatures in the simulator yet.")
            return
        print("\n🔊 All Creatures Make Sounds:")
        for creature in self.creature_list:
            creature.speak()


# Console Interface
def run_voice_console():
    sim = VoiceSimulator()

    while True:
        print("\n===== 🐾 Creature Voice Console =====")
        print("1. Add Hound")
        print("2. Add Feline")
        print("3. Add Bovine")
        print("4. Add Quacker")
        print("5. Play All Voices")
        print("6. Exit")

        user_input = input("Choose an action (1–6): ").strip()

        if user_input == '1':
            sim.insert_creature(Hound())
        elif user_input == '2':
            sim.insert_creature(Feline())
        elif user_input == '3':
            sim.insert_creature(Bovine())
        elif user_input == '4':
            sim.insert_creature(Quacker())
        elif user_input == '5':
            sim.play_all_sounds()
        elif user_input == '6':
            print("👋 Exiting simulator. Have a nice day!")
            break
        else:
            print("⚠️ Invalid selection. Please choose again.")


# Run the application
if __name__ == "__main__":
    run_voice_console()