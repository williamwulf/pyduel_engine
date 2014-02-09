__author__ = 'aelkikhia'


class Engine(object):

    def __init__(self):
        pass

    def create(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def save(self):
        pass

    def quit(self):
        pass

if __name__ == '__main__':
    engine = Engine()
    print('We got an engine')

    engine.start()
    print('start')

    engine.stop()
    print('stop')

    engine.save()
    print('save')

    engine.quit()
    print('quit')

    engine.create()
    print('create')