
class Singleton(object):

    _instance = None
    
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return  Singleton._instance

def main():
    print 'use singleton to get instance'
    s1 = Singleton().get_instance()
    s2 = Singleton().get_instance()
    if s1 == s2:
        print 'get the same instance'

if __name__ == '__main__':
    main()

'''
output:
use singleton to get instance
get the same instance
'''