from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.fields.html5 import EmailField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Email

class FormInicio(Form):
    usuario = StringField("Usuario", validators=[InputRequired()])
    contrasena = PasswordField("Contrasena", validators=[InputRequired()])
    enviar = SubmitField("Iniciar Sesión")

class FormAgregarEstudiantesCrearMateria(Form):
    codigoEstudianteAgrega= StringField("Codigo estudiante", validators=[InputRequired()])
    nombreMateria= StringField("Nombre materia", validators=[InputRequired()])
    agregarEstudiante= SubmitField("Agregar estudiante")

class FormRemoverEstudiantesCrearMateria(Form):
    codigoEstudianteRemueve= StringField("Codigo estudiante", validators=[InputRequired()])
    nombreMateria= StringField("Nombre materia", validators=[InputRequired()])
    removerEstudiante= SubmitField("Remover estudiante")

class FormCrearMateria(Form):
    nombreMateriaCrear= StringField("Nombre Materia", validators=[InputRequired()])
    profesorMateria = StringField("Codigo Profesor", validators=[InputRequired()])
    crearMateria= SubmitField("Crear materia")

class FormRegistrarUsuario(Form):
    nombre= StringField("Nombre", validators=[InputRequired()])
    apellido= StringField("Apellido", validators=[InputRequired()])
    codigo= StringField("Codigo", validators=[InputRequired()])
    telefono= StringField("Telefono", validators=[InputRequired()])
    correo= EmailField("Correo", validators=[InputRequired(), Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    rol= RadioField("Rol", choices=[("Estudiante"), ("Profesor")])
    usuario= StringField("Usuario", validators=[InputRequired()])
    contrasena = PasswordField("Contrasena", validators=[InputRequired()])
    crear= SubmitField("Crear")

class FormCrearActividad(Form):
    nombreActividad= StringField("Nombre", validators=[InputRequired()])
    descripcion= TextAreaField("Descripción", validators=[InputRequired()])
    materia= StringField("Materia", validators=[InputRequired()])
    enviar= SubmitField("Guardar")

class FormCalificarActividad(Form):
    idActividad=StringField("id Actividad", validators=[InputRequired()])
    idAlumno= StringField("id Alumno", validators=[InputRequired()])
    notaActividad = StringField("nota", validators=[InputRequired()])
    retroalimentacion = TextAreaField("Retroalimentación", validators=[InputRequired()])
    enviar= SubmitField("Calificar")

class FormActualizar(Form):
    telefono= StringField("Telefono", validators=[InputRequired()])
    correo= EmailField("Correo", validators=[InputRequired(), Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    guardar= SubmitField("Guardar")

class FormCambiarContrasena(Form):
    contrasena= PasswordField("Contraseña", validators=[InputRequired()])
    contrasenaNueva= PasswordField("Contraseña", validators=[InputRequired()])
    contrasenaConfirmada= PasswordField("Contraseña", validators=[InputRequired()])
    cambiar= SubmitField("Cambiar Contraseña")

class FormReportaError(Form):
    asunto = StringField("Telefono", validators=[InputRequired()])
    correo = EmailField("Correo", validators=[InputRequired(), Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    rol= RadioField("Rol", choices=[("Estudiante"), ("Profesor"), ("Administrador")])
    reporte = TextAreaField("Reporte", validators=[InputRequired()])
    enviar = SubmitField("Enviar")

