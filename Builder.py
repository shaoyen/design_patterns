class Director(object):
    builder = None

    def __init__(self, builder):
        self.builder = builder

    def create_car(self):
        self.builder.build_wheel()
        self.builder.build_body()


class CarBuilder(object):

    def build_wheel(self):
        pass

    def build_body(self):
        pass


class BusBuilder(CarBuilder):
    type = 'Bus'

    def build_wheel(self):
        print('build %s\'s wheel' % self.type)

    def build_body(self):
        print('build %s\'s body' % self.type)


class TruckBuilder(CarBuilder):
    type = 'Truck'

    def build_wheel(self):
        print('build %s\'s wheel' % self.type)

    def build_body(self):
        print('build %s\'s body' % self.type)


def main():
    bus = BusBuilder()
    director = Director(bus)
    director.create_car()

    truck = TruckBuilder()
    director = Director(truck)
    director.create_car()

if __name__ == '__main__':
    main()

'''
output:
build Bus's wheel
build Bus's body
build Truck's wheel
build Truck's body
'''
