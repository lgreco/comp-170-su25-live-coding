class Animal:

    def __init__(self, species, color:str, weight:int, fur:bool=True, mammal:bool=True, vocalization:str=""):
        self.species = species 
        self.color = color
        self.weight = weight
        self.fur = fur
        self.mammal = mammal
        self.vocalization = vocalization

    def animal_says(self):
        print(f"I am a {self.species} and I say: {self.vocalization}")
