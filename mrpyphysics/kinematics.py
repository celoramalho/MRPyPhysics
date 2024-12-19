class Kinematics():

    #========================Average-Velocity-Formula========================
    #Galileu Galilei (1564-1642)
    #Isaac Newton (1643-1727)
    @staticmethod
    def average_velocity(displacement: float, time_interval: float) -> float:
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
    
    #========================Average-Velocity-Formula========================
    def average_speed(self, displacement: float, time_interval: float) -> float:
        average_speed = abs(self.average_velocity(displacement, time_interval))
        return average_speed

    #=======================================================================
