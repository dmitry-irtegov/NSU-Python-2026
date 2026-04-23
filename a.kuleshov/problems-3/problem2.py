import unittest

class LivingOrganism:
    def __init__(self, name):
        self.name = name

    def is_alive(self):
        return True

    def describe(self):
        return f"{self.name} is a living organism"

class Animal(LivingOrganism):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def can_move(self):
        return True

    def move(self):
        return "moves"

class Chordate(Animal):
    def has_spine(self):
        return True

class Mammal(Chordate):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def has_fur(self):
        return True

    def gives_milk(self):
        return True

class Bird(Chordate):
    def can_fly(self):
        return True

    def move(self):
        return "flies"

class Carnivore(Mammal):
    def eats_meat(self):
        return True

class Herbivore(Mammal):
    def eats_plants(self):
        return True

class Felidae(Carnivore):
    def has_claws(self):
        return True

class Canidae(Carnivore):
    def is_pack_animal(self):
        return True

class Cat(Felidae):
    def sound(self):
        return "meow"

    def move(self):
        return "gracefully walks"

    def describe(self):
        return f"Cat {self.name}, {self.age} years old"

class Lion(Felidae):
    def sound(self):
        return "roar"

    def is_wild(self):
        return True

class Dog(Canidae):
    def sound(self):
        return "woof"

    def is_domestic(self):
        return True

class Wolf(Canidae):
    def sound(self):
        return "howl"

    def is_wild(self):
        return True

class Eagle(Bird):
    def sound(self):
        return "screech"

class Penguin(Bird):
    def can_fly(self):
        return False

    def move(self):
        return "swims"

    def sound(self):
        return "squawk"

class TestBiologyHierarchy(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Milo", 3, 4.5)
        self.dog = Dog("Buddy", 5, 10)
        self.lion = Lion("Simba", 7, 190)
        self.eagle = Eagle("Sky", 4)
        self.penguin = Penguin("Pingu", 2)

    def test_basic_properties(self):
        self.assertTrue(self.cat.is_alive())
        self.assertTrue(self.cat.can_move())
        self.assertTrue(self.cat.has_spine())

    def test_mammal_features(self):
        self.assertTrue(self.cat.has_fur())
        self.assertTrue(self.cat.gives_milk())

    def test_carnivore(self):
        self.assertTrue(self.cat.eats_meat())
        self.assertTrue(self.dog.eats_meat())

    def test_felidae(self):
        self.assertTrue(self.cat.has_claws())

    def test_canidae(self):
        self.assertTrue(self.dog.is_pack_animal())

    def test_sounds(self):
        self.assertEqual(self.cat.sound(), "meow")
        self.assertEqual(self.dog.sound(), "woof")
        self.assertEqual(self.lion.sound(), "roar")

    def test_birds(self):
        self.assertTrue(self.eagle.can_fly())
        self.assertFalse(self.penguin.can_fly())

    def test_movement(self):
        self.assertEqual(self.cat.move(), "gracefully walks")
        self.assertEqual(self.eagle.move(), "flies")
        self.assertEqual(self.penguin.move(), "swims")

    def test_polymorphism(self):
        animals = [self.cat, self.dog, self.lion]
        sounds = [a.sound() for a in animals]
        self.assertEqual(sounds, ["meow", "woof", "roar"])

    def test_inheritance(self):
        self.assertIsInstance(self.cat, Felidae)
        self.assertIsInstance(self.cat, Mammal)
        self.assertIsInstance(self.cat, Animal)
        self.assertIsInstance(self.cat, LivingOrganism)

    def test_describe(self):
        self.assertEqual(self.cat.describe(), "Cat Milo, 3 years old")

if __name__ == "__main__":
    unittest.main()