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
import basket_problem_hard.tools as tools
from basket_problem_hard.base import NotionFabric as nf
from basket_problem_hard.proto import CollectionFabric as col
from basket_problem_hard.proto import ComponentFabric as cmp
from basket_problem_hard.proto import StageFabric as stg
from basket_problem_hard.proto import InstanceFabric as ins
    
    
def simple_basket():
    base.chapter = "abstract"
    a_basket = nf.get("basket")
    a_apple = nf.get("apple")
    col_apple = col.get(a_apple)
    cmp_apple = cmp.get(col_apple, a_basket)
    stg_basket = stg.get(a_basket)
    
    base.chapter = "world"
    w_basket = nf.get("basket")
    ins.get(w_basket, a_basket)
    
    tools.define_notion_full(w_basket)
    
    
def print_dump():
    for notion in base.Notion.nodes:
        print(notion)
    
    
if __name__ == "__main__":
    simple_basket()
    print_dump()