from .unit import Unit
from .kinematics import Kinematics
#from .dynamics import Dynamics
#from .thermodynamics import Thermodynamics

class MRPyPhysics(Kinematics):
    """
    Main class to provide access to all physics-related calculations.
    """
    Unit = Unit
    def __init__(self):
        pass
        #self.kinematics = Kinematics()
        #self.unit = Unit()
        #self.dynamics = Dynamics()
        #self.thermodynamics = Thermodynamics()
    
    def unit(self, value: float | int, unit: str):
        return self.Unit(value, unit)