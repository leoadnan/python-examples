def method_1():
    print('method 1')


class ClassA:
    @staticmethod
    def class_method_1():
        print('ClassA class_method_1')

if __name__ == '__main__':
    method_1()
    ClassA.class_method_1()