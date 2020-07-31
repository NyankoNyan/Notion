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

class BasketModelError(Exception):
    def get_text(self):
        return ''

class TooMuchApplesError(BasketModelError):
    def get_text(self):
        return 'В корзину не влезет столько яблок.'

class BadCountError(BasketModelError):
    def get_text(self):
        return 'Не может быть столько яблок.'

class BadVariableError(BasketModelError):
    def get_text(self):
        return 'Это не яблоки.'


class BasketModelFabric:
    def create(self, limit):
        return BasketModel(limit)


class BasketModel:
    __slots__ = ('apples', 'limit','receivers_change')
    def __init__(self, limit):
        self.apples = 0
        self.limit = limit
        self.receivers_change = []
        
    def add_apples(self, count):
        try:
            count = int(count)
        except ValueError:
            raise BadVariableError()
        if count <= 0:
            raise BadCountError()
        new_apples = self.apples+count
        if new_apples > self.limit:
            raise TooMuchApplesError()
        self.apples = new_apples
        for receiver in self.receivers_change:
            receiver(self.apples)
    
    def is_full(self):
        return self.limit == self.apples
    
    def free_space(self):
        return self.limit - self.apples


class BasketViewFabric:
    def create(self, model):
        return BasketView(model) 


class BasketView:
    def __init__(self, model):
        self.model = model
        model.receivers_change.append(self.on_model_change)
        self.receivers_input = []
        
    def __update(self, apples):
        print(f'В корзине {apples} {self.__apples_repr(apples)}.')
        if self.model.is_full():
            print('Корзина полная.')
        else:
            free_count = self.model.free_space()
            print(f'В корзине ещё есть место под {free_count} {self.__apples_repr(free_count)}. Введите число яблок:')
            
    def __apples_repr(self, count):
        base_word = 'яблок'
        if count%10 == 1 and count%100 != 11:
            return base_word+'о'
        elif count%10 in [2,3,4] and count%100 not in [12,13,14]:
            return base_word+'а'
        else:
            return base_word        
        
    def on_model_change(self, apples):
        self.__update(apples)
        
    def show(self):
        self.__update(self.model.apples)
        input_loop = ConsoleInputLoop()
        input_loop.receivers_input.append(self.on_input_loop)
        input_loop.start()
        
    def on_input_loop(self, user_input):
        for receiver in self.receivers_input:
            if not receiver(user_input):
                return False
        return True


class BasketControllerFabric:
    def create(self, model, view):
        return BasketController(model, view)
    

class BasketController:
    def __init__(self, model, view):
        self.model = model
        view.receivers_input.append(self.on_input_loop)
    
    def on_input_loop(self, user_input):
        try:
            self.model.add_apples(user_input)
        except BasketModelError as e:
            print(e.get_text())
        return not self.model.is_full()


class ConsoleInputLoop:
    def __init__(self):
        self.receivers_input = []
        
    def start(self):
        while True:
            user_input = input()
            for receiver in self.receivers_input:
                if not receiver(user_input):
                    return


def runMVC(model_fabric, view_fabric, controller_fabric, 
           model_attrs=[], view_attrs=[], controller_attrs=[]):
    model = model_fabric.create(*model_attrs)
    view = view_fabric.create(model, *view_attrs)
    controller_fabric.create(model, view, *controller_attrs)
    view.show()
                
                
def run(apples_count): 
    runMVC(model_fabric=BasketModelFabric(), 
           view_fabric=BasketViewFabric(), 
           controller_fabric=BasketControllerFabric(), 
           model_attrs=[apples_count])    


if __name__ == "__main__":
    run(10)