class PublicacionDto:
    
    def __init__(self, id, titulo, contenido, estudiante_id):
        self.__id = id
        self.__titulo = titulo
        self.__contenido = contenido
        self.__estudiante_id = estudiante_id

    #Aqui van los getters
    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_contenido(self):
        return self.__contenido
    
    def get_estudiante_id(self):
        return self.__estudiante_id
    
    #Aqui van los setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_contenido(self, contenido):
        self.__contenido = contenido

    def set_estudiante_id(self, estudiante_id):
        self.__estudiante_id = estudiante_id