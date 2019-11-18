class Hello:
    def __init__(self, name):
        self._name = name

    def say(self):
        print('{}さん、こんにちは。'.format(self._name))


if __name__ == '__main__':
    h = Hello('太郎')
    h.say()