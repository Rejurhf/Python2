# Rejurhf
# 24.09.2018

class Bike:
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")

red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

red_bike.brake()
