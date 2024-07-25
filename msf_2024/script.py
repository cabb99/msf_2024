molecule_name='water'
molecule_atoms=['H', 'H', 'O']

class Molecule:
    def __init__(self, name, atoms: list): #Initialization
        self.name = name
        self.atoms =  atoms
        self._atoms = atoms # Please don't touch this variable
        self.__atoms = atoms # Really don't touch this variable please
        self.n_atoms = len(self.atoms) #Here the property wouldn't get updated if someone changes the number of atoms


    def num_atoms_method(self): #This is a good enough usually if the computation is fast
        return len(self.atoms)
    
    @property
    def atoms(self):
        return self.__atoms
    
    @atoms.setter
    def atoms(self, atoms):
        self.__atoms = atoms
        #self.num_atoms = len(self.__atoms)

    @property
    def num_atoms(self): # This makes the num_atoms method safer
        return len(self.__atoms)
      
    def __str__(self):
        return f"Molecule name: {self.name}, molecule atoms: {self.atoms}"

molecule=Molecule(molecule_name, molecule_atoms) #Instantiation
print(molecule)