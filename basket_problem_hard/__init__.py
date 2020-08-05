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
    base.chapter = "abstract"
    abstract_basket = base.Notion(name="basket")
    abstract_basket.components.extend([
        base.Component(proto.stage()),
        base.Component(proto.collection(name="apples"))
        ])
    
    abstract_view = base.Notion(name="view")
    abstract_view.components.extend([
        base.Component(proto.stage(base.Notion.find(name="basket").component(name="stage"))),
        base.Component(base.Notion(name="text"))
        ])
    
    base.chapter = "real"
    
    real_basket = base.Notion(name="basket")    
    real_view = base.Notion(name="view")
    
    proto.instance(real_basket, abstract_basket)
    proto.instance(real_view, abstract_view)
    
    
def print_dump():
    for notion in base.Notion.nodes:
        print(notion)
    
    
if __name__ == "__main__":
    create_area()
    print_dump()