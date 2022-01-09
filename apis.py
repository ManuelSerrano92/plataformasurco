from os import close
from sqlite3 import Error
from flask import jsonify, blueprints
from conn import conn, closeConn
from views import session

##versión 3.0

api = blueprints.Blueprint('api',__name__)



def buscarMateriasPorAlumno(alumno):
    query = "select nombreMateria from alumnosmaterias where idAlumno = ?"
    db = conn()
    valorABuscar = alumno
    materiasPorAlumno = db.execute(query, (valorABuscar,)).fetchall()
    materias = []
    for materia in materiasPorAlumno:
        materias.append(materia[0])
    closeConn()
    return list(materias)

def infoCompletaMateriasPorAlumno(alumno):
    query = "select * from alumnosmaterias where idAlumno = ?"
    db = conn()
    valorABuscar = alumno
    materiasPorAlumno = db.execute(query, (valorABuscar,)).fetchall()
    materias = []
    for materia in materiasPorAlumno:
        materiaedit = {}
        materiaedit["nombre"] = materia[0]
        materiaedit["nota"] = materia[2]
        materias.append(materiaedit)

    closeConn()
    return materias

def alumnosPorMaterias(materia):
    query = "select * from alumnosmaterias where nombreMateria = ?"
    db = conn()
    valorABuscar = materia
    alumnosPorMaterias = db.execute(query, (valorABuscar,)).fetchall()
    alumnos = []
    for alumno in alumnosPorMaterias:
        alumnoJson = {}
        alumnoJson["codigo"] = alumno[1]
        alumnoJson["nota"] = alumno[2]
        query = "select nombre, apellido from alumnos where id_alumno = ?"
        alumnoNombre=db.execute(query, (alumno[1],)).fetchone()
        alumnoJson["nombre"] = alumnoNombre[0] + " " + alumnoNombre[1]
        alumnos.append(alumnoJson)
    closeConn()
    return list(alumnos)

def buscarMateriasPorProfe(profesor):
    query = "select * from materias where id_profesor = ?"
    db = conn()
    valorABuscar = profesor
    materiasPorProfe = db.execute(query, (valorABuscar,)).fetchall()
    return materiasPorProfe

def todasLasMaterias():
    query = "select * from materias"
    db = conn()
    materiasRespuesta = db.execute(query).fetchall()
    closeConn()
    return materiasRespuesta

def infoBasicaAlumnos():
    query = "select id_alumno, nombre, apellido, user from alumnos;"
    db= conn()
    todosAlumnosConsulta = db.execute(query).fetchall()
    closeConn()
    return todosAlumnosConsulta

def infoCompletaAlumnos():
    query = "select * from alumnos;"
    db= conn()
    todosAlumnosConsulta = db.execute(query).fetchall()
    closeConn()
    return todosAlumnosConsulta

def infoCompletaProfesores():
    query = "select * from profesores;"
    db= conn()
    todosProfesoresConsulta = db.execute(query).fetchall()
    closeConn()
    return todosProfesoresConsulta

def infoBasicaProfesorPorId(id):
    query = "select nombre_p, apellido_p, user from profesores where id_profesor = ?;"
    db = conn()
    consultaProfesorPorId = db.execute(query, (id,)).fetchone()
    closeConn()
    return consultaProfesorPorId

def infoCompletaaProfesorPorId(id):
    query = "select * from profesores where user = ?;"
    db = conn()
    consultaProfesorPorId = db.execute(query, (id,)).fetchone()
    closeConn()
    return consultaProfesorPorId

def infoBasicaAlumnoPorId(id):
    query = "select nombre, apellido, user from alumnos where id_alumno = ?;"
    db = conn()
    consultaAlumnoPorId = db.execute(query, (id,)).fetchone()
    closeConn()
    return consultaAlumnoPorId

def infoCompletaAlumnoPorId(id):
    query = "select * from alumnos where user = ?;"
    db = conn()
    consultaAlumnoPorId = db.execute(query, (id,)).fetchone()
    closeConn()
    return consultaAlumnoPorId

def actividadesPorMateria(materia):
    query = "select * from actividades where nombreMateria = ?"
    db = conn()
    consultaActividadesPorMateria = db.execute(query, (materia,)).fetchall()
    closeConn()
    return consultaActividadesPorMateria

def notasAlumnosActividades(idActividad):
    query = "select * from actividadesPorAlumnos where idActividad = ?"
    db = conn()
    notasAlumnosActividades = db.execute(query, (idActividad,)).fetchall()
    closeConn()
    return notasAlumnosActividades

def notasActividadesPorAlumno(codigo):
    query = "select * from actividadesPorAlumnos where idAlumno = ?"
    db = conn()
    notasAlumno= db.execute(query, (codigo,)).fetchall()
    closeConn()
    actividades = []
    for nota in notasAlumno:
        activ = {}
        activ["id"] = nota[1]
        activ["nota"] = nota[2]
        activ["retroalimentacion"] = nota[3]
        actividades.append(activ)
    return actividades


@api.route("/baseContenido/")
def contenidoPaginaAside():
    rol = session["rol"]
    usuario = session["usuario"]
    respuestaParaBaseContenido = {}
    respuestaParaBaseContenido["infoSesion"] = {"rol": rol, "usuario": usuario}
    if (rol == "Administrador"):
        respuestaParaBaseContenido["linksAside"] = {"0" : "Administrar Materias", "1": "Administrar Usuarios", "2": "Registro Usuarios"}
        respuestaParaBaseContenido["linksDeAcceso"] = {"0" : '/plataformaNotas/adminAdministraMaterias/', "1": '/plataformaNotas/busquedasadmin/', "2": '/plataformaNotas/adminRegistro/'}
    if (rol != "Administrador"):
        id = session["id"]
        nombre = session["nombre"]
        respuestaParaBaseContenido["infoSesion"]["id"] = id
        respuestaParaBaseContenido["infoSesion"]["nombre"] = nombre
        if (rol == "Profesor"):
            respuestaParaBaseContenido["linksAside"] = {"0" : "Administrar Materias", "1": "Ver Información"}
            respuestaParaBaseContenido["linksDeAcceso"] = {"0" : '/plataformaNotas/administrarCursosProfesor/', "1": '/plataformaNotas/informacion/'}
        if (rol == "Estudiante"):
            respuestaParaBaseContenido["linksAside"] = {"0": "Ver Notas", "1":"Ver Información"}
            respuestaParaBaseContenido["linksDeAcceso"] = {"0" : '/plataformaNotas/notasestudiante/', "1": '/plataformaNotas/informacion/'}
    return jsonify(respuestaParaBaseContenido)

    

@api.route("/administracionMaterias/")
def administracionMaterias():
    rol = session["rol"]
    respuestaParaAdminMaterias = {}
    if (rol =="Administrador"):
        materiasRespuesta = todasLasMaterias()
        materiasParaAgregar = []
        for materia in materiasRespuesta:
            materiaJson={}
            materiaJson["id"] = materia[0]
            materiaJson["nombre"] = materia[1]
            materiaJson["profesor"] = {}
            consultaProfesor = infoBasicaProfesorPorId(materia[2])
            materiaJson["profesor"]["codigo"] = materia[2]
            materiaJson["profesor"]["nombre"] = consultaProfesor[0] + " "+ consultaProfesor[1]
            materiasParaAgregar.append(materiaJson)

        respuestaParaAdminMaterias["materias"] = materiasParaAgregar
        todosAlumnosConsulta = infoBasicaAlumnos()
        alumnosParaAgregar = []
        for alumno in todosAlumnosConsulta:
            alumnoJson={}
            idAlumno = alumno[0]
            alumnoJson["id"] = alumno[0]
            alumnoJson["nombre"] = alumno[1] +" "+ alumno[2]
            alumnoJson["usuario"] = alumno[3]
            alumnoJson["materiasMatriculadas"] = buscarMateriasPorAlumno(idAlumno)
            alumnosParaAgregar.append(alumnoJson)

        respuestaParaAdminMaterias["listaGeneralAlumnos"] = alumnosParaAgregar
        respuestaParaAdminMaterias["rol"] = rol


    if (rol =="Profesor"):
        codigo = session["id"]
        materiasRespuesta = buscarMateriasPorProfe(codigo)
        materiasParaAgregar = []
        for materia in materiasRespuesta:
            materiaJson={}
            materiaJson["id"] = materia[0]
            materiaJson["nombre"] = materia[1]
            materiaJson["alumnos"] = alumnosPorMaterias(materia[1])

            materiaJson["actividades"] = []
            consultaActividades = actividadesPorMateria(materia[1])
            for actividad in consultaActividades:
                notasActividad = notasAlumnosActividades(actividad[0])
                actividadJson = {}
                actividadJson["nombre"] = actividad[1]
                actividadJson["id"] = actividad[0]
                actividadJson["descripcion"] = actividad[2]
                actividadJson["materia"] = actividad[3]
                actividadJson["notas"] = []
                for actividadNota in notasActividad:
                    actividadNotaJson = {}
                    actividadNotaJson["idEstudiante"] = actividadNota[0]
                    actividadNotaJson["nota"] = actividadNota[2]
                    actividadNotaJson["retroalimentacion"] = actividadNota[3]
                    actividadJson["notas"].append(actividadNotaJson)
                materiaJson["actividades"].append(actividadJson)

            materiasParaAgregar.append(materiaJson)
        respuestaParaAdminMaterias["materias"] = materiasParaAgregar
        respuestaParaAdminMaterias["rol"] = rol
    if (rol =="Estudiante"):
        codigo = session["id"]
        materiasMatriculadas =infoCompletaMateriasPorAlumno(codigo)
        respuestaParaAdminMaterias["materias"] = materiasMatriculadas
        #respuestaParaAdminMaterias["materias"].append(materiasMatriculadas)
        actividadesCalificadas = notasActividadesPorAlumno(codigo)
        respuestaParaAdminMaterias["actividades"] = []
        for actividad in actividadesCalificadas:
            respuestaParaAdminMaterias["actividades"].append(actividad)
        respuestaParaAdminMaterias["actividadesPorRealizar"] = []
        respuestaParaAdminMaterias["rol"] = rol
        
        for materia in respuestaParaAdminMaterias["materias"]:
            actividadesARealizar = actividadesPorMateria(materia["nombre"])
            
            for actividad in actividadesARealizar:
                actividadJson = {}
                actividadJson["nombre"] = actividad[1]
                actividadJson["id"] = actividad[0]
                actividadJson["descripcion"] = actividad[2]
                respuestaParaAdminMaterias["actividadesPorRealizar"].append(actividadJson)
            
        
    return jsonify(respuestaParaAdminMaterias)

@api.route("/administrarUsuarios/")
def administrarUsuarios():
    rol = session["rol"]
    respuestaParaAdminUsuarios = {}
    if (rol =="Administrador"):
        alumnosInscritos = infoCompletaAlumnos()
        alumnosParaAgregar = []
        for alumno in alumnosInscritos:
            alumnoJson={}
            alumnoJson["id"] = alumno[0]
            alumnoJson["nombre"] = alumno[1] +" "+ alumno[2]
            alumnoJson["correo"] = alumno[3]
            alumnoJson["telefono"] = alumno[4]
            alumnoJson["usuario"] = alumno[5]
            alumnosParaAgregar.append(alumnoJson)
        respuestaParaAdminUsuarios["alumnos"] = alumnosParaAgregar

        profesoresInscritos = infoCompletaProfesores()
        profesoresParaAgregar = []
        for profesor in profesoresInscritos:
            profesorJson={}
            profesorJson["id"] = profesor[0]
            profesorJson["nombre"] = profesor[1] +" "+ profesor[2]
            profesorJson["correo"] = profesor[3]
            profesorJson["telefono"] = profesor[4]
            profesorJson["usuario"] = profesor[5]
            profesoresParaAgregar.append(profesorJson)
        respuestaParaAdminUsuarios["profesores"] = profesoresParaAgregar

        return jsonify(respuestaParaAdminUsuarios)
    if (rol == "Profesor"):
        idProfesor = session["usuario"]
        profesorInfo = infoCompletaaProfesorPorId(idProfesor)
        infoProfeJson = {}
        infoProfeJson["id"] = profesorInfo[0]
        infoProfeJson["nombre"] = profesorInfo[1]
        infoProfeJson["apellido"] = profesorInfo[2]
        infoProfeJson["correo"] = profesorInfo[3]
        infoProfeJson["telefono"] = profesorInfo[4]
        return jsonify(infoProfeJson)
    if (rol == "Estudiante"):
        idEstudiante = session["usuario"]
        alumnoInfo = infoCompletaAlumnoPorId(idEstudiante)
        infoAlumnoJson = {}
        infoAlumnoJson["id"] = alumnoInfo[0]
        infoAlumnoJson["nombre"] = alumnoInfo[1]
        infoAlumnoJson["apellido"] = alumnoInfo[2]
        infoAlumnoJson["correo"] = alumnoInfo[3]
        infoAlumnoJson["telefono"] = alumnoInfo[4]
        return jsonify(infoAlumnoJson)





@api.route("/eliminarMateria/<string:materia>/")
def eliminarMateria(materia):
    rol = session["rol"]
    if (rol =="Administrador"):
        try:
            query = "delete from materias where nombre_materia = ?"
            db = conn()
            db.execute(query, (materia,))
            db.commit()
            query = "delete from alumnosmaterias where nombreMateria = ?"
            db.execute(query, (materia,))
            db.commit()
            query = "delete from actividades where nombreMateria = ?"
            db.execute(query, (materia,))
            db.commit()
            closeConn()
            respuesta = {"respuesta": "Registro borrado"}
            return jsonify(respuesta)
        except:
            respuesta = {"respuesta": "Hubo un error borrando el registro"}
            return jsonify(respuesta)




@api.route("/eliminarUsuario/<string:codigo>/")
def eliminarUsuario(codigo):
    rol = session["rol"]
    usuarioAlumno = infoBasicaAlumnoPorId(codigo)[2]
    usuarioProfesor = infoBasicaProfesorPorId(codigo)[2]
    if (rol =="Administrador"):
        if (usuarioAlumno != None):
            try:
                query = "delete from login where user = ?"
                db = conn()
                db.execute(query, (usuarioAlumno,))
                db.commit()
                query = "delete from alumnos where id_alumno = ?"
                db = conn()
                db.execute(query, (codigo,))
                db.commit()
                query = "delete from alumnosmaterias where idAlumno = ?"
                db = conn()
                db.execute(query, (codigo,))
                db.commit()
                query = "delete from actividadesPorAlumnos where idAlumno = ?"
                db = conn()
                db.execute(query, (codigo,))
                db.commit()
                closeConn()
                respuesta = {"respuesta": "Registro borrado"}
                return jsonify(respuesta)
            except:
                respuesta = {"respuesta": "Hubo un error borrando el registro"}
                return jsonify(respuesta)
        if (usuarioProfesor != None):
            try:
                query = "delete from login where user = ?"
                db = conn()
                db.execute(query, (usuarioAlumno,))
                db.commit()
                query = "delete from profesores where id_profesor = ?"
                db = conn()
                db.execute(query, (codigo,))
                db.commit()
                query = "delete from materias where id_profesor = ?"
                db = conn()
                db.execute(query, (codigo,))
                db.commit()
                respuesta = {"respuesta": "Registro borrado"}
                return jsonify(respuesta)
            except:
                respuesta = {"respuesta": "Hubo un error borrando el registro"}
                return jsonify(respuesta)



@api.route("/eliminarActividad/<string:actividad>/")
def eliminarActividad(actividad):
    rol = session["rol"]
    if (rol =="Profesor"):
        try:
            query = "delete from actividades where id_actividad = ?"
            db = conn()
            db.execute(query, (actividad,))
            db.commit()
            query = "delete from actividadesPorAlumnos where idActividad = ?"
            db.execute(query, (actividad,))
            db.commit()
            closeConn()
            respuesta = {"respuesta": "Actividad eliminada"}
            return jsonify(respuesta)
        except Error:
            respuesta = {"respuesta": "Hubo un error borrando el registro"}
            print(Error)
            return jsonify(respuesta)

@api.route("/refrescarPromedios/<string:codigo>/")
def refrescaPromedios(codigo):
    db= conn()
    query= "select nombreMateria from alumnosmaterias where idAlumno = ?"
    materias = db.execute(query,(codigo,)).fetchall()
    cantidadDeMaterias = 0
    cantidadActividades = 0
    sumatoriaNotasMaterias = 0
    notaMateria = 0
    notaPromedio = 0
    for materia in materias:
        cantidadDeMaterias=+1
        
        query= "select * from actividades where nombreMateria = ?"
        actividades = db.execute(query, (materia[0],)).fetchall()
        cantidadActividades = 0
        sumatoriaNotasMateria = 0
        for actividad in actividades:
            query="select nota from actividadesPorAlumnos where idActividad = ?"
            sumaNotaActividades= db.execute(query, (actividad[0],)).fetchall()
            
            for nota in sumaNotaActividades:
                cantidadActividades+=1
                sumatoriaNotasMateria+=int(nota[0])
        if (cantidadActividades != 0):
            notaMateria = sumatoriaNotasMateria/cantidadActividades
            sumatoriaNotasMaterias += notaMateria
            notaMateria= "{:.2f}".format(notaMateria)
    if (cantidadDeMaterias != 0):
        notaPromedio = sumatoriaNotasMaterias/cantidadDeMaterias
        notaPromedio = "{:.2f}".format(notaPromedio)

    query = "update alumnosmaterias set notaFinal = ? where idAlumno = ?"
    valoresACambiar = (notaMateria, codigo)
    db.execute(query, (valoresACambiar))
    db.commit()
    respuesta = {"respuesta": "notas actualizadas", "promedio": notaPromedio}

        
    return jsonify(respuesta)

