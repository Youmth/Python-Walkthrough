import sys
'''
En este archivo está una explicación de las clases

Para este, la explicación consiste de un solo ejemplo con la funcionalidad
más básica de las clases
'''

def Print(*msgs, sep:str=' ', end:str='\n'):
  print(f"Línea {sys._getframe().f_back.f_lineno}: ",*msgs, sep=sep, end=end)

def Input(msg):
  return input(f"Línea {sys._getframe().f_back.f_lineno}: {msg}")

def intro(times:int=10):
   print('\n'*times)

class Form:
    def __init__(self, **kwargs):
        '''Inicializa la clase Form.
        
        #Inputs:
        kwargs: nombre de la información que se pide y su estatus
        '''

        self.status = ('private', 'public', 'secret')

        self.titles = list(kwargs.keys())

        self.data = {}

        for key, value in kwargs.items():
            self.data[key] = {
                'value': None,
                'status': value
            }

    def ask_info(self, *args):
        for title in args:
            if title not in self.titles:
                Print('Título inválido.')
                continue

            self.data[title]['value'] = Input(f'Ingrese {title}:    ')

    def ask_all_info(self):
        self.ask_info(*self.titles)

    def set_status(self, title:str, status:str):
        if (title in self.titles) and (status in self.status):
            self.data[title]['status'] = status
        else:
            Print('Estado o título inválidos.')

    def set_private(self, *titles:str):
        for title in titles:
            self.set_status(title, 'private')

    def set_public(self, *titles:str):
        for title in titles:
            self.set_status(title, 'public')

    def set_secret(self, titles:str):
        for title in titles:
            self.set_status(title, 'secret')

    def show_info(self, *titles:str):
        for title in titles:
            if title not in self.titles:
                Print('Título inválido.')
                return
            
            if self.data[title]['status'] == 'public':
                Print(f'{title}: {self.data[title]['value']}')
            if self.data[title]['status'] == 'private':
                Print(f'{title}: {'*'*len(self.data[title]['value'])}')
            if self.data[title]['status'] == 'secret':
                Print('No disponible.')


    def show_all_info(self):
        self.show_info(*self.titles)
        


form = Form(Nombre='public', Edad='private', Sexo='secret')

form.ask_all_info()
intro(4)
form.show_all_info()

intro()

form2 = Form(Nombre='public', Edad='public', DNI='private')

form2.ask_all_info()
intro(4)
if int(form2.data['Edad']['value'])<18:
    form2.set_private(*form2.titles)
form2.show_all_info()



    


