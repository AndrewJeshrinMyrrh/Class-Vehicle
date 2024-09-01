class Vehicle:

    def __init__(self, max_speed, mileage):

        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(240, 18)
model2 = Vehicle(250, 19)

print("Model Max Speed:", modelx.max_speed)
print("Model Mileage:", modelx.mileage)

print("Model Max Speed:", model2.max_speed)
print("Model Mileage:", model2.mileage)
