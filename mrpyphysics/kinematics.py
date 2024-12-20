class Kinematics():


    #========================Average-Speed-Formula========================
    #Velocidade Escalar Média
    class AverageSpeed():
        def calculate(self, distance: float, time_interval: float) -> float:
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return distance / time_interval
            #velocidade = constante, não sofre variação
        
        def distance(self, average_speed: float, time_interval: float) -> float:
            return average_speed * time_interval
        
        def time_interval(self, distance: float, average_speed: float) -> float:
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
        def calculate(displacement: float, time_interval: float) -> float:
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return displacement / time_interval

        @staticmethod
        def displacement(average_velocity: float, time_interval: float) -> float:
            return average_velocity * time_interval

        @staticmethod
        def time_interval(displacement: float, average_velocity: float) -> float:
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
        def displacement(velocity: float, time_interval: float) -> float:
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return velocity * time_interval
        
        @staticmethod
        def velocity(displacement: float, time_interval: float) -> float:
            if time_interval == 0:
                raise ValueError("Time cannot be zero.")
            return displacement / time_interval
        
        def time_interval(displacement: float, velocity: float) -> float:
            if velocity == 0:
                raise ValueError("Velocity cannot be zero.")
            return displacement / velocity
        
        def position(initial_position: float, velocity: float, time_interval: float) -> float:
        #Fórmula do Sorvete
        #PositionTimeEquation
        if time < 0:
            raise ValueError("Time cannot be negative.")
        return initial_position + velocity * time