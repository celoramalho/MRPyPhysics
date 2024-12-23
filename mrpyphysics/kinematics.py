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
        
        def time(distance: Unit, average_speed: Unit) -> Unit:
            distance, average_speed = Unit.validate_and_convert_to_si(distance, average_speed)
            if average_speed == 0:
                raise ValueError("Speed cannot be zero.")
            return Unit(distance / average_speed, 's')

    #=======================================================================
    #========================Average-Velocity-Formula========================
    #Velocidade Vetorial Média
    #Galileu Galilei (1564-1642)
    #Isaac Newton (1643-1727)
    class AverageVelocity():
        @staticmethod
        def calculate(displacement: Unit, time_interval: Unit) -> Unit:
            displacement, time_interval = Unit.validate_and_convert_to_si(displacement, time_interval)
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return Unit(displacement / time_interval, 'm/s') #velocidade = displacement / time

        @staticmethod
        def displacement(average_velocity: Unit, time: Unit) -> Unit:
            average_velocity, time = Unit.validate_and_convert_to_si(average_velocity, time)
            return Unit(average_velocity * time, 'm') #displacement = average_velocity * time

        @staticmethod
        def time(displacement: Unit, average_velocity: Unit) -> Unit:
            displacement, average_velocity = Unit.validate_and_convert_to_si(displacement, average_velocity)
            if average_velocity == 0:
                raise ValueError("Velocity cannot be zero.")
            return Unit(displacement / average_velocity, 's')
    

    #========================Uniform-Rectilinear-Motion========================
    class URM():
        #Galileu Galilei (1564-1642)
        #Isaac Newton (1643-1727)
        #Key Characteristics of URM
        #The velocity (v) remains constant.
        #The acceleration (a) is zero because the velocity does not change.
        #The displacement is directly proportional to the time (t).
        @staticmethod
        def displacement(velocity: Unit, time: Unit) -> Unit:
            velocity, time_interval = Unit.validate_and_convert_to_si(velocity, time_interval)
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return Unit(velocity * time_interval, 'm')
        
        @staticmethod
        def velocity(displacement: Unit, time: Unit) -> Unit:
            displacement, time_interval = Unit.validate_and_convert_to_si(displacement, time_interval)
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return Unit(displacement / time_interval, 'm/s') #velocidade = displacement / time
        
        def time_interval(displacement: Unit, velocity: Unit) -> Unit:
            displacement, velocity = Unit.validate_and_convert_to_si(displacement, velocity)
            if velocity == 0:
                raise ValueError("Velocity cannot be zero.")
            return Unit(displacement / velocity, 's')
        
        def position(initial_position: Unit, velocity: Unit, time_interval: Unit) -> Unit:
        #Fórmula do Sorvete
        #PositionTimeEquation
            initial_position, velocity, time_interval = Unit.validate_and_convert_to_si(initial_position, velocity, time_interval)
            if time_interval < 0:
                raise ValueError("Time cannot be negative.")
            return Unit(initial_position + velocity * time_interval, 'm')
    
    #========================Uniform-Accelerated-Motion========================
    class UAM():
        #Galileu Galilei (1564-1642)
        #Isaac Newton (1643-1727)
        def average_acceleration(velocity: Unit, time_interval: Unit) -> Unit:
            #Average Acceleration Formula
            velocity, time_interval = Unit.validate_and_convert_to_si(velocity, time_interval)
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return Unit(velocity / time_interval, 'm/s^2')

        def final_velocity(initial_velocity: Unit, acceleration: Unit, time_interval: Unit) -> Unit:
            #Velocity-Time Equation
            acceleration, time_interval = Unit.validate_and_convert_to_si(acceleration, time_interval)
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return Unit(initial_velocity + acceleration * time_interval, 'm/s')
        
        def time_interval(initial_velocity: Unit, final_velocity: Unit, acceleration: Unit) -> Unit:
            initial_velocity, final_velocity, acceleration = Unit.validate_and_convert_to_si(initial_velocity, final_velocity, acceleration)
            if acceleration == 0:
                raise ValueError("Acceleration cannot be zero.")
            return Unit((final_velocity - initial_velocity) / acceleration, 's')
        def final_velocity_torricelli(initial_velocity: Unit, displacement: Unit, acceleration: Unit) -> Unit:
            initial_velocity, displacement, acceleration = Unit.validate_and_convert_to_si(initial_velocity, displacement, acceleration)
            return Unit((initial_velocity**2 + 2 * acceleration * displacement)**0.5, 'm/s')
        
        def aceleration_torricelli(initial_velocity: Unit, final_velocity: Unit, displacement: Unit) -> Unit:
            initial_velocity, final_velocity, displacement = Unit.validate_and_convert_to_si(initial_velocity, final_velocity, displacement)
            return Unit((final_velocity**2 - initial_velocity**2) / (2 * displacement), 'm/s^2')
        def position(initial_position: Unit, initial_velocity: Unit, time_interval: Unit, acceleration: Unit) -> Unit:
            #Velocity-Displacement Equation
            #Evangelista Torricelli (1608–1647)
            initial_position, initial_velocity, time_interval, acceleration = Unit.validate_and_convert_to_si(initial_position, initial_velocity, time_interval, acceleration)
            if time_interval < 0:
                raise ValueError("Time cannot be negative.")
            return Unit(initial_position + initial_velocity * time_interval + 0.5 * acceleration * time_interval**2, 'm')