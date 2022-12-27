from random import randint


class Bones:
    @staticmethod
    def random_throw():
        while True:
            side_ = randint(0, 6)
            contin = input('Желаете кинуть еще раз кубик? ')
            if contin == 'Нет' or contin == 'No':
                return side_
            else:
                print(side_)

# Ну это что-то совсем изи оказалось. Симулятор игры в кости. Боже, зачем?
asd = Bones()
print(asd.random_throw())