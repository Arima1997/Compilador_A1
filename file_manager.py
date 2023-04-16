import os

class file_mgr:

    def __init__(self, assem_path, hexa_path):
        self._assem_path = assem_path
        self._rutaHexa = hexa_path
        self.contadorbytes = 0

    @property
    def assem_path(self):
        return self._assem_path

    @property
    def rutaHexa(self):
        return self._rutaHexa

    @assem_path.setter
    def assem_path(self, assem_path):
        self._assem_path = assem_path

    @rutaHexa.setter
    def rutaHexa(self, rutaHexa):
        self._rutaHexa = rutaHexa

    def create_file(self):
        """Este metodo se encarga de crear los archivos necesarios
        en formato txt, el primero donde se colocará el código ensamblador
        y el segundo donde se colocará la traducción al código hexadecimal"""

        if os.path.exists(self._assem_path):
            print(f'Archivo {self._assem_path} encontrado...')
        else:
            f = open(self._assem_path, 'x', encoding='utf8')
            f.close()
            print(f'Archivo {self._assem_path} generado...')

        if os.path.exists(self._rutaHexa):
            print(f'Archivo {self._rutaHexa} encontrado...')
        else:
            f = open(self._rutaHexa, 'x', encoding='utf8')
            f.close()
            print(f'Archivo {self._rutaHexa} generado...')

    def read_file(self):
        lista = []
        f = open(self._assem_path, 'r', encoding='utf8')
        lista = f.readlines()
        f.close()
        return lista

    def write_file(self, ensamble:list):
        f = open(self._rutaHexa, 'w', encoding='utf8')
        f.write(f'Inicio del ensamble'.center(50, '-'))
        f.write('\n')
        for line in ensamble:
            f.write(line.__str__() + "\n")
        f.write('\n')
        f.write(f'Fin del ensamble'.center(50, '-'))
        f.write('\n')
        f.close()

if __name__ == '__main__':
    Compil = file_mgr('Prueba1.txt', 'Prueba2.txt')
    Compil.create_file()
    lista = Compil.read_file()
    if lista == 0:
        print(f'El archivo esta vacio..')
    else:
        Compil.write_file(lista)