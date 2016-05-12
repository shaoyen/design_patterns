class Person(object):

    def __init__(self, name):
        self._name = name

    def weapon(self):
        print '%s \'s weapon:' % self._name

class DecoratorBase(Person):

    _component = None

    def __init__(self):
        pass

    def decorate(self, component):
        self._component = component

    def weapon(self):
        if self._component:
            self._component.weapon()

class DecoratorGun(DecoratorBase):

    def weapon(self):
        self._component.weapon()
        print 'Gun'

class DecoratorSword(DecoratorBase):

    def weapon(self):        
        self._component.weapon()
        print 'Sword'

def main():
    hero = Person('Hero')
    gun = DecoratorGun()
    sword = DecoratorSword()
    gun.decorate(hero)
    sword.decorate(gun)
    sword.weapon()

if __name__ == '__main__':
    main()

'''
output:
Hero 's weapon:
Gun
Sword
'''