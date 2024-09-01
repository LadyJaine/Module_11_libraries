import inspect
# lang_names = ['Russian','English',"French","Chinese",'German','Arabic']
#
# for name in lang_names:
#     quest1 = input(f'Do you speak {name} ?')
#     if name == 'Arabic':
#         print('I cannot understand you.')
#     else:
#         print('Me too!')
class Language():
    lang_names = ['Russian', 'English', "French", "Chinese", 'German', 'Arabic']
    def __init__(self,name:str):
        self.name = name



    def do_you_speak(self):
        quest1 = input(f'Do you speak {self.name} ?')
        if self.name == 'Arabic':
            print('I cannot understand you.')
        else:
            print('Me too!')




    def introspection_info(name):
        print(Language.__name__)
        print(type(Language))
        print()


some_student = Language('French')
print(dir(some_student))
print(type(some_student))
print(hasattr(some_student,'lang_names'))
print(getattr(some_student,'lang_names'))
print(getattr(some_student,'Greek','No such language'))
print(callable(some_student.lang_names))
print(callable(some_student.do_you_speak))
print(inspect.isclass(Language))