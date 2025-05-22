class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if not isinstance(pet_type, str):
            raise Exception("pet_type must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an Owner instance or None")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added.")
        pet.owner = self
        self.pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda pet: pet.name)
