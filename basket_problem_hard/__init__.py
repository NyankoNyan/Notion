'''
Создать программу по накладыванию яблок в виртуальную корзину. 
Пользователю надо положить 10 яблок в корзину.
1) Выводится сообщение сколько яблок сейчас в корзине и сколько осталось положить.
2) Вводим число яблок. Проверяем ввод на корректность (неотрицательное число).
3) Если яблок кладётся больше чем нужно, выводим текст ошибки.
4) Увеличиваем число яблок в корзине.
5) Если корзина не полная, возвращаемся к пункту 1.
6) Если корзина полная выводим сообщение и завершаем работу.
'''

import basket_problem_hard.base as base
import basket_problem_hard.proto as proto

def create_area():
    abstract_basket = base.Node(name="basket", chapter="abstract")
    abstract_basket.components.extend([
        base.Component(proto.stage()),
        base.Component(proto.collection(name="apples"))
        ])
    
    abstract_view = base.Node(name="view", chapter="abstract")
    abstract_view.components.extend([
        base.Component(proto.stage(base.Node.find(name="basket", chapter="abstract").component(name="stage"))),
        base.Component(base.Node(name="text"))
        ])
    
    real_basket = base.Node(name="basket", chapter="real")
    
    real_view = base.Node(name="view", chapter="real")
    
if __name__ == "__main__":
    create_area()