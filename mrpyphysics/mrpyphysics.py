from .unit import Unit
from .kinematics import Kinematics
#from .dynamics import Dynamics
#from .thermodynamics import Thermodynamics

class MRPyPhysics(Unit, Kinematics):
    """
    Main class to provide access to all physics-related calculations.
    """

    def __init__(self):
        pass
        #self.kinematics = Kinematics()
        #self.unit = Unit()
        #self.dynamics = Dynamics()
        #self.thermodynamics = Thermodynamics()