class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except:
            pass
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer(object):

    def __init__(self):
        pass

    def update(self):
        pass

class ConcreteSubject(Subject):

    def __init__(self, state):
        Subject.__init__(self)
        self._state = state
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class ConcreteObserver(Observer):

    def __init__(self, name = ''):
        self._name = name

    def update(self, subject):
        print('Observer: %s, Subject: %s' %(self._name, subject._state))

def main():
    print 'init publish state to 1'
    publish = ConcreteSubject('state 1')
    subscriber1 = ConcreteObserver('subscriber1')
    subscriber2 = ConcreteObserver('subscriber2')
    print 'attach subscribers'
    publish.attach(subscriber1)
    publish.attach(subscriber2)
    print 'changed state to 2'
    publish.state = 'state 2'
    print 'detach subscriber2'
    publish.detach(subscriber2)
    print 'changed state to 3'
    publish.state = 'state 3'

if __name__ == '__main__':
    main()

'''
output:
init publish state to 1
attach subscribers
changed state to 2
Observer: subscriber1, Subject: state 2
Observer: subscriber2, Subject: state 2
detach subscriber2
changed state to 3
Observer: subscriber1, Subject: state 3
'''