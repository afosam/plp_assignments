# 🐾 Polymorphism with Animals

class Animal:
    def move(self):
        pass  # Empty method to be overridden

class Dog(Animal):
    def move(self):
        return "🐕 The dog runs on four legs."

class Bird(Animal):
    def move(self):
        return "🐦 The bird flies in the sky."

class Fish(Animal):
    def move(self):
        return "🐠 The fish swims in the water."

# ✅ Create a list of animals
animals = [Dog(), Bird(), Fish()]

# 🖨️ Show how each moves
for animal in animals:
    print(animal.move())
