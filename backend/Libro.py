class Libro:
    #CONSTRUCTOR
    def __init__(self,id_libro,titulo_libro,tipo_libro,autor,contador, disponible, no_disponible,año,editorial):

        self.id_libro = id_libro
        self.titulo_libro = titulo_libro
        self.tipo_libro = tipo_libro
        self.autor=autor
        self.contador = contador
        self.disponible = disponible
        self.no_disponible = no_disponible
        self.año=año
        self.editorial=editorial

    #ENCAPSULAMIENTO
    def getId_libro(self):
        return self.id_libro
    
    def setId_libro(self, nombre):
        self.id_libro = id_libro

    def getTitulo_libro(self):
        return self.titulo_libro
    
    def setTitulo_libro(self, titulo_libro):
        self.titulo_libro = titulo_libro

    def getTipo_libro(self):
        return self.tipo_libro
    
    def setTipo_libro(self, tipo_libro):
        self.user = tipo_libro

    def getAutor(self):
        return self.autor
    
    def setAutor(self, autor):
        self.autor = autor

    def getContador(self):
        return self.contador
    
    def setContador(self, contador):
        self.contador = contador

    def getDisponibler(self):
        return self.disponible
    
    def setDisponible(self, disponible):
        self.disponible = disponible

    def getNo_disponible(self):
        return self.no_disponible
    
    def setNo_disponible(self, no_disponible):
        self.no_disponible = no_disponible

    def getAño(self):
        return self.año
    def setaAño(self, año):
        self.año = año

    def getEditorial(self):
        return self.editorial
    def setEditorial(self, editorial):
        self.editorial = editorial