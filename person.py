class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbier = []
    
    def leggTilHobby(self, hobby):
        self._hobbier.append(hobby)
    
    def skrivHobbier(self):
        for hobby in self._hobbier:
            print(hobby)
    
    def skrivUt(self):
        print(f'Navnet er: {self._navn} og alder er: {self._alder}')
        self.skrivHobbier()