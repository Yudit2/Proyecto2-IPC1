from flask import Flask, jsonify,request
from flask_cors import CORS
from Libro import Libro
from Actualizar import actualizar
from persona import persona

app =Flask (__name__)
CORS(app)
#se crea una lista 
Libros =[]
actualizar=[]

cliente=[]

#Metodo para crear libro
@app.route('/', methods = ['POST'])
def otraruta ():
    global book
    book_Repetido = False

    Nuevo_book = Libro(request.json['id_libro'],request.json['titulo_libro'], request.json['tipo_libro'], 
    request.json['autor'], request.json['contador'], request.json['disponible'],request.json['no_disponible'],request.json['año'],request.json['editorial'])

#Actualizar libro
@app.route('/Persona/Actualizar/<string:persona>',methods=['PUT'])
def actualizarlibro(actualizar):
    global Actualizar
    nactualizar = request.json['actulizarlibro']
    id_libro = request.json['id:libro']
    tipo_libro = request.json['tipo_libro']
    autor = request.json['autor']
    contador = request.json['contador'] 
    disponible = request.json['disponible']
    no_disponible = request.json['no_disponible']
    año = request.json['año']
    editorial= request.json['editorial']
    for i in range (len(Actulizar)):
        if actualizar == Actualizar [i].getActualizar():
            if verificacionId (request.json['actualizar'])==True:
                Actualizar[i].setId_libro(id_libro)
                Actualizar[i].settipo_libro(tipo_libro)
                Actualizar[i].setautoro(autor)
                Actualizar[i].setcontador(contador)
                Actualizar[i].setdisponible(disponible)
                Actualizar[i].setno_disponible(no_disponible)
                Actualizar[i].setaño(año)
                Actualizar[i].seteditorial(editorial)
                return jsonify({'Mensajea':'Se actulizó correctamente ','Mensaje':'Se actulizó correctamente' ,'estado':'true'})
            else:
                return jsonify({'Mensajea':'no se actualizo','estado':'false'})
    return jsonify({'Mensajea': 'No se encontró el libro','estado':'false'})

#ACTUALIZAR libro 
def ActualizarLibro(libr,libro):
    global Libro
    for Libro in Actualizar:
        if (str(user) == str(Libro.getlibro())):
            Libro.setLibro(user)
            break



    

@app.route('/',methods =['GET'])
def rutaInicial():
    global cliente
    envio=[]
    for cliente in cliente:

        objeto= {
        
            'id'  : cliente.getId(),
            'nombre':cliente.getNombre(),
            'contraseña':cliente.getContraseña(),
            'edad' : cliente.getEdad(),
            'carrera': cliente.getCarrera()
        }
        envio.append(objeto)
    return(jsonify(envio))

    #METODO PARA VER LOS Libros
@app.route('/Libros', methods=['GET'])
def MostrarLibros():
    global Libros
    objeto = []
    for Libro in Libros:
        objeto = {
            'id_libro':Libro.getId_libro(),
            'titulo_libro':Libro.getTitulo_libro(),
            'tipo_libro':Libro.getTipo_libro(),
            
        }
        objeto.append(objeto)
    return(jsonify(objeto))


    #Se define al usuario Administrador
personas.append(persona("Darlin","M","admin","admin@ipc1.com","admin@ipc1"))

    #Metodo para crear usuarios
@app.route('/', methods = ['POST'])
def otraruta ():
    global cliente
    cliente_Repetido = False

    Nuevo_cliente = persona(request.json['id'], request.json['nombre'], request.json['nickname'],
    request.json['contraseña'], request.json['edad'], request.json['carrera'])

    for cliente in cliente:
        if cliente.getId() == request.json['Id']:
            cliente_Repetido = True

    if cliente_Repetido == False:
        cliente.append(Nuevo_cliente)
        Respuesta = jsonify({
                    'Error': False,
                    'Mensaje' : 'se agrego con exito',
                    'Registro':True

        })
        return (Respuesta)
    else:
       Respuesta = jsonify({
            'Error':True,
            'Mensaje' : 'El id esta duplicado',
            'Registro' : False
        })
    return (Respuesta)

#VERIFICAR LOGIN
@app.route('/Login',methods=['POST'])
def VerificarCredenciales():
    global persona
    nickname = request.json['nickname']
    contraseña = request.json['contraseña']
    for persona in personas:
        if (nickname=="admin" and password =="admin@ipc1"):
            return jsonify({'Mensaje':'Bienvenido Administrador','Tipo':'Administrador','Login':'true'})
        elif Verificarpersonas(nickname,contraseña) == True:
            return jsonify({'Mensaje':'Bienvenido ' + nickname,'Tipo':'Usuario','Login':'true','persona': nickname})
    return jsonify({'Mensaje':'Credenciales Incorrectas','Tipo':'Error Effesinda', 'Login':'false'})


#METODO PARA VERIFICAR SI EL USUARIO EXISTE
def VerificarUsuarios(us,contra):
    global Usuarios
    validar=False
    for Usuario in Usuarios:
        if (str(Usuario.getUser()) == str(us)):
            if (str(contra)==str(Usuario.getContraseña())):
                validar = True
    return validar



    
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port =3000, debug =True)
