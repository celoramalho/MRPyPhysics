from .unit import Unit

class Kinematics():

    #========================Average-Speed-Formula========================
    #Velocidade Escalar Média
    class AverageSpeed():

        def calculate(distance : Unit, time: Unit) -> Unit:
            distance_unit, time_unit = distance.unit, time.unit
            distance, time = Unit.validate_and_convert_to_si(distance, time)
            if time == 0:
                raise ValueError("Time cannot be zero.")
            return Unit(distance / time, 'm/s') #velocidade = distance / time
        
        def distance(average_speed: Unit, time: Unit) -> Unit:
            average_speed_unit, time_unit = average_speed.unit, time.unit
            average_speed, time = Unit.validate_and_convert_to_si(average_speed, time)
            return Unit(average_speed * time, 'm')
        
        def time(self, distance: float, average_speed: float) -> float:
            if average_speed == 0:
                raise ValueError("Speed cannot be zero.")
            return distance / average_speed

    #=======================================================================
    #========================Average-Velocity-Formula========================
    #Velocidade Vetorial Média
    #Galileu Galilei (1564-1642)
    #Isaac Newton (1643-1727)
    class AverageVelocity():
        @staticmethod
        def calculate(displacement: float, time: float) -> float:
            if time == 0:
                raise ValueError("Time cannot be zero.")
            return displacement / time

        @staticmethod
        def displacement(average_velocity: float, time: float) -> float:
            return average_velocity * time

        @staticmethod
        def time(displacement: float, average_velocity: float) -> float:
            if average_velocity == 0:
                raise ValueError("Velocity cannot be zero.")
            return displacement / average_velocity
    

    #========================Uniform-Rectilinear-Motion========================
    class UniformRectilinearMotion():
        #Key Characteristics of URM
        #The velocity (v) remains constant.
        #The acceleration (a) is zero because the velocity does not change.
        #The displacement is directly proportional to the time (t).
        @staticmethod
        def displacement(velocity: float, time: float) -> float:
            if time == 0:
                raise ValueError("Time cannot be zero.")
            return velocity * time
        
        @staticmethod
        def velocity(displacement: float, time: float) -> float:
            if time == 0:
                raise ValueError("Time cannot be zero.")
            return displacement / time
        
        def time(displacement: float, velocity: float) -> float:
            if velocity == 0:
                raise ValueError("Velocity cannot be zero.")
            return displacement / velocity
        
        def position(initial_position: float, velocity: float, time: float) -> float:
        #Fórmula do Sorvete
        #PositionTimeEquation
            if time < 0:
                raise ValueError("Time cannot be negative.")
            return initial_position + velocity * time