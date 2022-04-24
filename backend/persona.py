
class persona:
   #Constructor
   
  def __init__(self, id,nombre,nickname,contraseña,edad,carrera,carnet):
    self.id = id
    self.nombre = nombre
    self.nickname = nickname
    self.contraseña = contraseña
    self.edad = edad
    self.carrera = carrera
    self.carnet = carnet
    


# Metodos GET
# creando metodos para obtener la informacion , usando self

def getId(self):
  return self.id

def getNombre (self):
  return self.nombre

  def getContraseña(self):
    return self.constraseña

  def getEdad(self):
    return self.edad
  def getContraseña(self):
    return self.constraseña

  def getCarrera(self):
    return self.carrera




  #METODOS SET 
  # Creando metodos para setear ña informacion, usando el self y el parametro

  def setId(delf, Id):
    self.id=Id

  def setNombre(delf, Nombre):
    self.nombre=Nombre

  def setContraseña(delf, Constraseña):
    self.contraseña=Contraseña

  def setEdad(delf, Edad):
    self.edad = Edad

  def setCarrera(delf, Carrera):
    self.carrera=Carrera

