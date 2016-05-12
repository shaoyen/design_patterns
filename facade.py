class SubsystemOne(object):

    def method11(self):
        print 'subsystem method 11'

    def method12(self):
        print 'subsystem method 12'


class SubsystemTwo(object):

    def method21(self):
        print 'subsystem method 21'

    def method22(self):
        print 'subsystem method 22'


class SubsystemThree(object):

    def method31(self):
        print 'subsystem method 31'

    def method32(self):
        print 'subsystem method 32'


class Facade(object):

    def __init__(self):
        self._one = SubsystemOne()
        self._two = SubsystemTwo()
        self._three = SubsystemThree()

    def method_a(self):
        print '=== method_a() ==='
        self._one.method11()
        self._two.method21()
        self._three.method31()

    def method_b(self):
        print '=== method_b() ==='
        self._one.method12()
        self._two.method22()
        self._three.method32()


def main():
    facade = Facade()
    facade.method_a()
    facade.method_b()

if __name__ == '__main__':
    main()

'''
output:
=== method_a() ===
subsystem method 11
subsystem method 21
subsystem method 31
=== method_b() ===
subsystem method 12
subsystem method 22
subsystem method 32
'''
