class EstudianteDto():
    
    def __init__(self, id, nombre, apellido, edad, mail, matricula, carrera):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail
        self.matricula = matricula
        self.carrera = carrera

    #Estos son los getters
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    def get_mail(self):
        return self.__mail
    
    def get_matricula(self):
        return self.__matricula
    
    def get_carrera(self):
        return self.__carrera
    
    #Estos son los Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_edad(self, edad):
        self.__edad = edad

    def set_mail(self, mail):
        self.__mail = mail

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_carrera(self, carrera):
        self.__carrera = carrera