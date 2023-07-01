#Has a Relationship

class Engine:
    def boot_Engine(self):
        print("Booted!")

class Vehicle:
    def start_engine(self):
        Engine().boot_Engine()  # This Vehicle Has a Relationship Vehicle Has a Engine
        print("Engine Started")


v = Vehicle()
v.start_engine()