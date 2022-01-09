from flask import blueprints, render_template, request, session, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from forms import *
from conn import *
from werkzeug.security import check_password_hash, generate_password_hash
from sqlite3 import Error
import functools
from apis import infoBasicaProfesorPorId
##import yagmail


main= blueprints.Blueprint("main", __name__)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "usuario" not in session:
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view

def login_estudiante(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["rol"] != "Estudiante":
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view

def login_profesor(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["rol"] != "Profesor":
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view

def login_administrador(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["rol"] != "Administrador":
            return redirect(url_for("main.inicio"))
        return view(**kwargs)
    return wrapped_view


    
@main.route("/", methods=["GET", "POST"])
def inicio():
    form = FormInicio()
    if (form.validate_on_submit()):
        usuario=request.form["usuario"]
        contrasena=request.form["contrasena"]
        db=conn()
        usuarioConsulta = db.execute("select * from login where user = ?", (usuario,)).fetchone()
        print(usuarioConsulta)

        if usuarioConsulta is not None:
            contrasena = contrasena + usuario + "Surcolombiana"
            sw = check_password_hash(usuarioConsulta[1], contrasena)        
            if(sw):
                if(usuarioConsulta[2] == "Estudiante"):
                    session["usuario"]=usuarioConsulta[0]
                    session["rol"]=usuarioConsulta[2]
                    idAlumnoconsulta = db.execute("select * from alumnos where user = ?", (usuarioConsulta[0],)).fetchone()
                    session["id"] = idAlumnoconsulta[0]
                    session["nombre"] = idAlumnoconsulta[1] + " " + idAlumnoconsulta[2]
                    closeConn()
                    return redirect("informacion")
                if(usuarioConsulta[2] == "Profesor"):
                    session["usuario"]=usuarioConsulta[0]
                    session["rol"]=usuarioConsulta[2]
                    idProfeconsulta = db.execute("select * from profesores where user = ?", (usuarioConsulta[0],)).fetchone()
                    session["id"] = idProfeconsulta[0]
                    session["nombre"] = idProfeconsulta[1] + " " + idProfeconsulta[2]
                    closeConn()
                    return redirect("administrarCursosProfesor")
                if(usuarioConsulta[2] == "Administrador"):
                    session["usuario"]=usuarioConsulta[0]
                    session["rol"]=usuarioConsulta[2]
                    closeConn()
                    return redirect("adminAdministraMaterias")
            else:
                flash("Contraseña incorrecta")
        if usuarioConsulta is None:
            flash("Usuario incorrecto")

    return render_template("index.html", form=form)



@main.route("/adminAdministraMaterias/", methods=["GET", "POST"])
@login_required
@login_administrador
def adminAdministraMaterias():

    formularioAgregarEstudiante = FormAgregarEstudiantesCrearMateria()
    formularioRemoverEstudiante = FormRemoverEstudiantesCrearMateria()
    formularioCrearMateria = FormCrearMateria()

    if (formularioAgregarEstudiante.validate_on_submit()):
        estudiante = request.form["codigoEstudianteAgrega"]
        materia = request.form["nombreMateria"]
        queryActualizacion = "insert into alumnosmaterias(nombreMateria, idAlumno) values (?,?) "
        db = conn()
        valoresParaActualizar = (materia, estudiante)
        db.execute(queryActualizacion,valoresParaActualizar)
        db.commit()
        return redirect(request.referrer)
    
    if (formularioRemoverEstudiante.validate_on_submit()):
        estudiante = request.form["codigoEstudianteRemueve"]
        materia = request.form["nombreMateria"]
        queryConsulta = "delete from alumnosmaterias where idAlumno = ? and nombreMateria LIKE ?"
        valoresABorrar = (estudiante, materia)
        db = conn()
        db.execute(queryConsulta, valoresABorrar)
        db.commit()
        return redirect(request.referrer)
    
    if (formularioCrearMateria.validate_on_submit()):
        nombreMateria = request.form["nombreMateriaCrear"]
        codigoProfesor = request.form["profesorMateria"]

        if infoBasicaProfesorPorId(codigoProfesor) == None:
            flash("El Código de profesor seleccionado, no existe.")
        else:
            query = "INSERT into materias(nombre_materia,id_profesor) VALUES(?,?);" 
            valoresAIngresar=(nombreMateria,codigoProfesor)
            db = conn()
            db.execute(query, valoresAIngresar)
            db.commit()
            flash("Materia creada con éxito.")
            return redirect(request.referrer)


    return render_template("adminMaterias.html", formularioAgregarEstudiante=formularioAgregarEstudiante, formularioRemoverEstudiante=formularioRemoverEstudiante, formularioCrearMateria=formularioCrearMateria)




@main.route("/adminRegistro/", methods=["GET", "POST"])
@login_required
@login_administrador
def adminRegistro():
    form = FormRegistrarUsuario()
    if (form.validate_on_submit()):
        nombre= request.form["nombre"]
        apellido= request.form["apellido"]
        codigo= request.form["codigo"]
        telefono= request.form["telefono"]
        correo= request.form["correo"]
        rol= request.form["rol"]
        usuario= request.form["usuario"]
        contrasena= request.form["contrasena"]
        contrasena= contrasena + usuario + "Surcolombiana"
        contrasena = generate_password_hash(contrasena)
        valoresAIngresar=(usuario,contrasena,rol)
        query="insert into login(user, password, rol)values(?,?,?)"
        try:
            db = conn()
            db.execute(query, valoresAIngresar)
            db.commit()
            closeConn()
           
        except Error:
            print(Error)    
        
        if (rol == "Estudiante"):
            try:
                valoresAIngresar=(codigo, nombre, apellido, correo, telefono, usuario)
                query="INSERT into alumnos(id_alumno,nombre,apellido,correo,telefono,user)values(?,?,?,?,?,?)"
                print((query, valoresAIngresar))
                db = conn()
                db.execute(query, valoresAIngresar)
                db.commit()
                closeConn()
                flash("Usuario ingresado con éxito")
                return redirect(request.referrer)
            except Error:
                flash("Hay un error en el ingreso de usuario, probablemente un código o nombre de usuario ya utilizado.")
                print(Error)
        
        if (rol == "Profesor"):
            try:
                valoresAIngresar=(codigo, nombre, apellido, correo, telefono, usuario)
                query="INSERT into profesores(id_profesor,nombre_p,apellido_p,correo_p,telefono_p,user)values(?,?,?,?,?,?)"
                print(query, valoresAIngresar)
                db = conn()
                db.execute(query, valoresAIngresar)
                db.commit()
                closeConn()
                flash("Usuario ingresado con éxito")
                return redirect(request.referrer)
            except Error:
                flash("Hay un error en el ingreso de usuario, probablemente un código ya utilizado.")
                print(Error)
    return render_template("adminRegistro.html", form=form)


@main.route("/busquedasadmin/")
@login_required
@login_administrador
def busquedasadmin():
    return render_template("busquedasadmin.html")


@main.route("/administrarCursosProfesor/", methods=["GET", "POST"])
@login_required
@login_profesor
def administrarCursosProfesor():
    formularioCrearActividad = FormCrearActividad()
    formularioCalificarActividad = FormCalificarActividad()
    if (formularioCrearActividad.validate_on_submit()):
        nombreActividad = request.form["nombreActividad"]
        nombreMateria = request.form["materia"]
        descripcion = request.form["descripcion"]
        try:
            query = "insert into actividades (nombre_actividad, nombreMateria, descripcion) values(?,?,?)"
            db = conn()
            valoresAIngresar = (nombreActividad,nombreMateria,descripcion)
            db.execute(query,(valoresAIngresar))
            db.commit()
            closeConn()
            flash("Actividad Creada")
            return redirect(request.referrer)
        except Error:
            print(Error)

    if (formularioCalificarActividad.validate_on_submit()):
        idActividad = request.form["idActividad"]
        idAlumno = request.form["idAlumno"]
        notaActividad = request.form["notaActividad"]
        retroalimentacion = request.form["retroalimentacion"]
        try:
            query = "insert into actividadesPorAlumnos (idAlumno,idActividad,nota,retroalimentacion) values(?,?,?,?)"
            valoresAIngresar = (idAlumno,idActividad,notaActividad,retroalimentacion)
            db = conn()
            db.execute(query,(valoresAIngresar))
            db.commit()
            closeConn()
            flash("Actividad Calificada")
            return redirect(request.referrer)
        except Error:
            print(Error)
            flash("No se pudo actualizar la calificación, revise los valores")

    return render_template("administrarCursosProfesor.html", formularioCrearActividad=formularioCrearActividad, formularioCalificarActividad=formularioCalificarActividad)


@main.route("/informacion/", methods=["GET", "POST"])
@login_required
def informacion():

    formActualizar= FormActualizar()
    if (formActualizar.validate_on_submit()):
        telefonoNuevo=request.form["telefono"]
        correoNuevo=request.form["correo"]
        usuarioActual=session["usuario"]
        query="update profesores set telefono_p = ?, correo_p = ? where user = ?"
        valoresACambiar = (telefonoNuevo, correoNuevo, usuarioActual)
        print(query,valoresACambiar)
        try:
            db = conn()
            db.execute(query, valoresACambiar)
            db.commit()
            closeConn()
            flash("La información fué actualizada.")
        except Error:
            print(Error)



    formCambioContra= FormCambiarContrasena()
    if (formCambioContra.validate_on_submit()):
        contrasenaActual = request.form["contrasena"]
        contrasenaNueva = request.form["contrasenaNueva"]
        contrasenaConfirmacion = request.form["contrasenaConfirmada"]
        if (contrasenaNueva != contrasenaConfirmacion):
            flash("La confirmación debe ser igual a la contraseña nueva")
        else :
            db=conn()
            usuarioConsulta = db.execute("select * from login where user = ?", (session["usuario"],)).fetchone()

            if usuarioConsulta is not None:
                contrasena = contrasenaActual + session["usuario"] + "Surcolombiana"
                sw = check_password_hash(usuarioConsulta[1], contrasena)        
                if(sw):
                    contrasenaNueva= contrasenaNueva + session["usuario"] + "Surcolombiana"
                    contrasenaNueva = generate_password_hash(contrasenaNueva)
                    query="update login set password = ? where user = ?"
                    valoresACambiar = (contrasenaNueva,session["usuario"])
                    db.execute(query,(valoresACambiar))
                    db.commit()
                    closeConn()
                    flash("La contraseña fué cambiada con éxito")
                    return redirect(request.referrer)
                else:
                    flash("La contraseña ingresada, es incorrecta")

    return render_template("informacion.html", formActualizar=formActualizar,formCambioContra=formCambioContra)



@main.route("/notasestudiante/")
@login_required
@login_estudiante
def notasestudiante():
    return render_template("notasestudiante.html")



@main.route("/salir/")
@login_required
def salir():
    session.clear()
    return redirect(url_for("main.inicio"))


@main.route("/preguntas/", methods=["GET", "POST"])
@login_required
def preguntas():

    formularioError = FormReportaError()

    if (formularioError.validate_on_submit()):
        asunto = request.form["asunto"]
        email = request.form["correo"]
        rol = request.form["rol"]
        mensaje = request.form["reporte"]
        
        """clienteCorreo = yagmail.SMTP("surcoplataforma@gmail.com","equipoocho")
        clienteCorreo.send(to=email, subject=session["nombre"] +" Hemos recibido tu reporte.", contents="Esta es una copia auto generada de tu reporte <br> en la mayor brevedad nuestro equipo estará en contacto contigo, Gracias."+ asunto +"<br>"+rol+"<br>"+mensaje)
        """    
        flash("Reporte enviado.")
        return redirect(request.referrer)


    return render_template("preguntas.html", formularioError=formularioError)
