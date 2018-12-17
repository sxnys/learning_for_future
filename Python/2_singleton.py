''' Python 中实现单例模式 '''

'''
单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。
通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。
如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。
'''

'''
1、__new__方法
其中 super(Singleton1, cls) 可以换成以下几种：
super(cls, cls)
super(__class__, cls)
super(cls.__class__, cls)
super(type(cls), cls)
object
'''
class Singleton1:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._instance


'''
2、共享属性
创建实例时把所有实例的__dict__指向同一个字典，这样它们具有相同的属性和方法
'''
class Singleton2:
    _state = {}
    def __new__(cls, *args, **kwargs):
        super_ins = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        super_ins.__dict__ = cls._state
        return super_ins


'''
3、装饰器实现，实例映射到字典，且仅有一个实例
'''
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Singleton3: pass


'''
4、使用模块，即import，天然的单例模式
'''
# singleton.py
class Singleton4:
    pass

singleton4 = Singleton4()

# to use
# from singleton import singleton4


if __name__ == '__main__':
    a1 = Singleton1()
    b1 = Singleton1()
    print('a1 is b1 : {}'.format(a1 is b1))  # True

    a2 = Singleton2()
    b2 = Singleton2()
    print('a2 is b2 : {}'.format(a2 is b2))  # False

    a3 = Singleton3()
    b3 = Singleton3()
    print('a3 is b3 : {}'.format(a3 is b3))  # True
