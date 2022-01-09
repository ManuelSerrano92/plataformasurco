function contenidoPaginaAside() {
    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/baseContenido/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }

    function completado(evt) {
        let dataConsulta = JSON.parse(this.response);
        document.getElementById("tituloRol").innerHTML = dataConsulta.infoSesion["rol"];
        document.getElementById("tituloGeneral").innerHTML = dataConsulta.infoSesion["rol"];
        
        
        if ((dataConsulta.infoSesion["rol"] == "Profesor")||(dataConsulta.infoSesion["rol"] == "Estudiante")){
        
            document.getElementById("listaInfoSesion").innerHTML = "<li id='codigoEnDocumento'>"+dataConsulta.infoSesion["id"]+"</li>" + 
            "<li>Usuario: "+dataConsulta.infoSesion["usuario"]+"</li>"+"<li>Nombre: "+dataConsulta.infoSesion["nombre"]+"</li>";
        }

        if (dataConsulta.infoSesion["rol"] == "Administrador") {
            document.getElementById("listaInfoSesion").innerHTML = "<li>Usuario: "+dataConsulta.infoSesion["usuario"]+"</li>";
        }
        
        for (let i = 0; i < Object.keys(dataConsulta.linksAside).length; i++) {
         
            document.getElementById("listaLinksAside").innerHTML += "<li><a href="+ dataConsulta.linksDeAcceso[i] +"> "+ dataConsulta.linksAside[i] +"</a></li>"
        }
    }
}



function listaProfesoresAdmin() {
    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/administrarUsuarios/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }
    
    function completado(evt) {
        let dataConsulta = JSON.parse(this.response);
        document.getElementById("listaGeneralEstudiantes").innerHTML = "";
        for (let i= 0; i < dataConsulta.profesores.length; i++){
            document.getElementById("listaGeneralEstudiantes").innerHTML += "<li>Código: "+dataConsulta.profesores[i].id + " Nombre: " + dataConsulta.profesores[i].nombre + "<br> Usuario: " + dataConsulta.profesores[i].usuario +" telefono: " + dataConsulta.profesores[i].telefono +"<br> correo: " + dataConsulta.profesores[i].correo +"</li>";
        }
    }
}

function listaAlumnosAdmin() {
    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/administrarUsuarios/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }
    
    function completado(evt) {
        let dataConsulta = JSON.parse(this.response);
        document.getElementById("listaGeneralEstudiantes").innerHTML = "";
        for (let i= 0; i < dataConsulta.alumnos.length; i++){
            document.getElementById("listaGeneralEstudiantes").innerHTML += "<li>Código: "+dataConsulta.alumnos[i].id + " Nombre: " + dataConsulta.alumnos[i].nombre + "<br> Usuario: " + dataConsulta.alumnos[i].usuario +" telefono: " + dataConsulta.alumnos[i].telefono +"<br> correo: " + dataConsulta.alumnos[i].correo +"</li>";
        }
    }
}

function buscarInfoUsuarioAdmin() {
    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/administrarUsuarios/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }
    
    function completado(evt) {
        let dataConsulta = JSON.parse(this.response);
        let usuarioAbuscar = document.getElementById("UsuarioABuscar").value;
        document.getElementById("listaGeneralEstudiantes").innerHTML = "";
        console.log(usuarioAbuscar);
            if (usuarioAbuscar.length > 4) {
                for (let i= 0; i < dataConsulta.alumnos.length; i++) {
                    if (dataConsulta.alumnos[i].usuario == usuarioAbuscar) {
                        document.getElementById("listaGeneralEstudiantes").innerHTML = "<li>Código: "+dataConsulta.alumnos[i].id + " Nombre: " + dataConsulta.alumnos[i].nombre + "<br> Usuario: " + dataConsulta.alumnos[i].usuario +" telefono: " + dataConsulta.alumnos[i].telefono +"<br> correo: " + dataConsulta.alumnos[i].correo +"</li>";
                        break;
                    }
                }
                for (let i= 0; i < dataConsulta.profesores.length; i++) {
                    if (dataConsulta.profesores[i].usuario == usuarioAbuscar) {
                        document.getElementById("listaGeneralEstudiantes").innerHTML = "<li>Código: "+dataConsulta.profesores[i].id + " Nombre: " + dataConsulta.profesores[i].nombre + "<br> Usuario: " + dataConsulta.profesores[i].usuario +" telefono: " + dataConsulta.profesores[i].telefono +"<br> correo: " + dataConsulta.profesores[i].correo +"</li>";
                        break;
                    }
                }
            } else {
                for (let i= 0; i < dataConsulta.alumnos.length; i++) {
                    if (dataConsulta.alumnos[i].id == usuarioAbuscar) {
                        document.getElementById("listaGeneralEstudiantes").innerHTML = "<li>Código: "+dataConsulta.alumnos[i].id + " Nombre: " + dataConsulta.alumnos[i].nombre + "<br> Usuario: " + dataConsulta.alumnos[i].usuario +" telefono: " + dataConsulta.alumnos[i].telefono +"<br> correo: " + dataConsulta.alumnos[i].correo +"</li>";
                        break;
                    }
                }
                for (let i= 0; i < dataConsulta.profesores.length; i++) {
                    if (dataConsulta.profesores[i].id == usuarioAbuscar) {
                        document.getElementById("listaGeneralEstudiantes").innerHTML = "<li>Código: "+dataConsulta.profesores[i].id + " Nombre: " + dataConsulta.profesores[i].nombre + "<br> Usuario: " + dataConsulta.profesores[i].usuario +" telefono: " + dataConsulta.profesores[i].telefono +"<br> correo: " + dataConsulta.profesores[i].correo +"</li>";
                        break;
                    }
                }
            }
    }
}


function eliminarUsuarioAdmin() {
    let usuarioAbuscar = document.getElementById("UsuarioABuscar").value;
    if (usuarioAbuscar.length > 4) {
        window.alert("Para eliminar un usuario debe digitar el código único")
    } else {
        let confirmacion = window.confirm("¿Está seguro de eliminar el usuario?")

        if (confirmacion) {
            let objXMLHTTP= new XMLHttpRequest();

            let urlParaConsulta = "http://127.0.0.1:5000/api/eliminarUsuario/"
            urlParaConsulta += usuarioAbuscar + "/"

            objXMLHTTP.open("GET", urlParaConsulta);
            objXMLHTTP.addEventListener('load', completado);
            objXMLHTTP.addEventListener('error', manejarError);
            objXMLHTTP.send();
            
            function manejarError(evt) {
                console.log('ocurrio un error.');
            }

            function completado(evt) {
                let dataConsulta = JSON.parse(this.response);
                window.alert(dataConsulta.respuesta);
                location.reload();
            }
        } else {
            window.alert("Acción cancelada")
        }
    }
    
}


function cargarNuevaMateria(materia) {
    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/administracionMaterias/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }
    
    function completado(evt) {
        let dataConsulta = JSON.parse(this.response);
        document.getElementById("listaEstudiantesMatriculados").innerHTML = "";
        if (dataConsulta.rol == "Administrador") {
            document.getElementById("nombreMateriaCampoAgregaEstudiante").value = materia;
            document.getElementById("nombreMateriaCampoRemoverEstudiante").value = materia;
            for (let i= 0; i < dataConsulta.listaGeneralAlumnos.length; i++){

                for (let j= 0; j < dataConsulta.listaGeneralAlumnos[i].materiasMatriculadas.length; j++ ) {
                    if (dataConsulta.listaGeneralAlumnos[i].materiasMatriculadas[j] == materia) {
                        document.getElementById("listaEstudiantesMatriculados").innerHTML += "<li>Usuario: "+dataConsulta.listaGeneralAlumnos[i].id + " " + dataConsulta.listaGeneralAlumnos[i].nombre +"</li>";
                    }
                }
            }
            for (let i= 0; i < dataConsulta.materias.length; i++) {
                if (dataConsulta.materias[i].nombre == materia) {
                    document.getElementById("nombreProfeConsultarMateria").innerHTML = dataConsulta.materias[i].profesor.nombre;
                }
            }
        }

        if (dataConsulta.rol == "Profesor") {
            document.getElementById("nombreMateriaAdministrarMateria").innerHTML = materia
            for (let i= 0; i < dataConsulta.materias.length; i++) {
                if (dataConsulta.materias[i].nombre == materia) {
                    for (let j=0; j < dataConsulta.materias[i].alumnos.length; j++) {
                        document.getElementById("listaEstudiantesMatriculados").innerHTML += "<li> Codigo:" +dataConsulta.materias[i].alumnos[j].codigo + " Nombre: " +dataConsulta.materias[i].alumnos[j].nombre + " Nota: " + dataConsulta.materias[i].alumnos[j].nota  +"</li>";
                    }
                }
            }
        }
    }
}

function alertaVentana(mensaje) {
    window.alert(mensaje);
}

function confirmacionVentana(mensaje) {
    window.confirm(mensaje);
}

function eliminarMateria(materia) {
    let materiaAEliminar = materia;

    let confirmacion = window.confirm("¿Está seguro de eliminar la materia?")

    if (confirmacion) {
        let objXMLHTTP= new XMLHttpRequest();

        let urlParaConsulta = "http://127.0.0.1:5000/api/eliminarMateria/"
        urlParaConsulta += materiaAEliminar + "/"

        objXMLHTTP.open("GET", urlParaConsulta);
        objXMLHTTP.addEventListener('load', completado);
        objXMLHTTP.addEventListener('error', manejarError);
        objXMLHTTP.send();
        
        function manejarError(evt) {
            console.log('ocurrio un error.');
        }

        function completado(evt) {
            let dataConsulta = JSON.parse(this.response);
            window.alert(dataConsulta.respuesta);
            location.reload();
        }
    } else {
        window.alert("Acción cancelada")
    }
}

window.addEventListener("load", administrarMaterias, true); function administrarMaterias(){

    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/administracionMaterias/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }
    
    function completado(evt) {
        let dataConsulta = JSON.parse(this.response);

        document.getElementById("tituloVistaSection").innerHTML = "Administración de materias para " + dataConsulta["rol"];
        

        
        if (dataConsulta.rol == "Administrador") {
            for (let i= 0; i < dataConsulta.materias.length; i++){
                let materiaAConsultar = dataConsulta.materias[i].nombre;
                document.getElementById("listaMaterias").innerHTML += "<button onclick=cargarNuevaMateria('"+materiaAConsultar+"')"+">"+ materiaAConsultar + "<button onclick=eliminarMateria('"+materiaAConsultar+"')"+">x</button></button><br>";
            }

            for (let i= 0; i < dataConsulta.listaGeneralAlumnos.length; i++){
                document.getElementById("listaGeneralEstudiantes").innerHTML += "<li>Usuario: "+dataConsulta.listaGeneralAlumnos[i].id + " " + dataConsulta.listaGeneralAlumnos[i].nombre +"</li>";
            }
        }

        if (dataConsulta.rol == "Profesor") {

            for (let i= 0; i < dataConsulta.materias.length; i++){
                let materiaAConsultar = dataConsulta.materias[i].nombre;
                document.getElementById("listaMaterias").innerHTML += "<button"+" id='boton"+materiaAConsultar+"' onclick="+"cargarNuevaMateria('"+materiaAConsultar+"')"+">"+ materiaAConsultar + "</button>";
            }
            
        }

        if (dataConsulta.rol == "Estudiante") {
            console.log(dataConsulta);
            for (let i= 0; i < dataConsulta.materias.length; i++) {
                document.getElementById("listaParaLlenarNotasMateria").innerHTML += "<li>Materia: "+dataConsulta.materias[i].nombre + " Nota: " + dataConsulta.materias[i].nota +"</li>";
            }
            for (let i= 0; i < dataConsulta.actividades.length; i++) {
                document.getElementById("listaParallenarDeActividadesMaterias").innerHTML += "<li>Id actividad: "+dataConsulta.actividades[i].id + " Nota: " + dataConsulta.actividades[i].nota + " Retroalimentación: " + dataConsulta.actividades[i].retroalimentacion + "</li>";
            }
            for (let i= 0; i < dataConsulta.actividadesPorRealizar.length; i++) {
                document.getElementById("listaParaLlenarDeTodasLasActividades").innerHTML += "<li>Id actividad: "+dataConsulta.actividadesPorRealizar[i].id+" Nombre actividad: "+ dataConsulta.actividadesPorRealizar[i].nombre + "<br>Descripción: " + dataConsulta.actividadesPorRealizar[i].descripcion +"</li>";
            }
        }
        
    }

}

function mostrarActividades(){
    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/administracionMaterias/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }
    
    function completado(evt) {
        let materiaAConsultar = document.getElementById("nombreMateriaAdministrarMateria").textContent;
        let dataConsulta = JSON.parse(this.response);
        console.log(dataConsulta)

        document.getElementById("listaActividadesMateria").innerHTML = ""
        


        for (let i= 0; i < dataConsulta.materias.length; i++){

            if (dataConsulta.materias[i].nombre == materiaAConsultar) {
                document.getElementById("materiaActividadesQueSeVen").textContent = "Se muestran actividades de "+materiaAConsultar; 
                for (let j= 0; j < dataConsulta.materias[i].actividades.length; j++){
                    document.getElementById("listaActividadesMateria").innerHTML += "<li>Id: "+dataConsulta.materias[i].actividades[j].id + " " + dataConsulta.materias[i].actividades[j].nombre + "<br> Descripción: "+ dataConsulta.materias[i].actividades[j].descripcion+"</li>";
                }
            }
        }
    }
}


function mostrarCalificaciones() {
    let objXMLHTTP= new XMLHttpRequest();

    let urlParaConsulta = "http://127.0.0.1:5000/api/administracionMaterias/"

    objXMLHTTP.open("GET", urlParaConsulta);
    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }
    
    function completado(evt) {
        let materiaAConsultar = document.getElementById("nombreMateriaAdministrarMateria").textContent;
        let dataConsulta = JSON.parse(this.response);
        console.log(dataConsulta)

        document.getElementById("listaEstudiantesCalificados").innerHTML = "";
        


        for (let i= 0; i < dataConsulta.materias.length; i++){

            if (dataConsulta.materias[i].nombre == materiaAConsultar) {
                document.getElementById("calificacionesActividadesQueSeVen").textContent = "Se muestran las calificaciones de actividades para: " + materiaAConsultar;
                
                for (let j= 0; j < dataConsulta.materias[i].actividades.length; j++){
                    for (let k=0; k < dataConsulta.materias[i].actividades[j].notas.length; k++)
                        document.getElementById("listaEstudiantesCalificados").innerHTML += "<li> Id Actividad: "+dataConsulta.materias[i].actividades[j].id+" Alumno: "+dataConsulta.materias[i].actividades[j].notas[k].idEstudiante + " Nota: " + dataConsulta.materias[i].actividades[j].notas[k].nota + "<br> Retroalimentación: "+ dataConsulta.materias[i].actividades[j].notas[k].retroalimentacion +"</li>";
                }
            }
        }
    }
}

function eliminarActividad() {
    actividadAEliminar = document.getElementById("actividadAEliminar").value;

    if (actividadAEliminar.length > 3) {
        window.alert("Para eliminar una actividad debe digitar el código único")
    } else {
        let confirmacion = window.confirm("¿Está seguro de eliminar la actividad?")
        
        if (confirmacion) {
            let objXMLHTTP= new XMLHttpRequest();

            let urlParaConsulta = "http://127.0.0.1:5000/api/eliminarActividad/"
            urlParaConsulta += actividadAEliminar + "/"

            objXMLHTTP.open("GET", urlParaConsulta);
            objXMLHTTP.addEventListener('load', completado);
            objXMLHTTP.addEventListener('error', manejarError);
            objXMLHTTP.send();
            
            function manejarError(evt) {
                console.log('ocurrio un error.');
            }

            function completado(evt) {
                let dataConsulta = JSON.parse(this.response);
                window.alert(dataConsulta.respuesta);
                location.reload();
            }
        } else {
            window.alert("Acción cancelada")
        }
    }

}

function revisarPromedios() {
    let codigo = document.getElementById("codigoEnDocumento").textContent;
    let objXMLHTTP= new XMLHttpRequest();

            let urlParaConsulta = "http://127.0.0.1:5000/api/refrescarPromedios/"
            urlParaConsulta += codigo + "/"

            objXMLHTTP.open("GET", urlParaConsulta);
            objXMLHTTP.addEventListener('load', completado);
            objXMLHTTP.addEventListener('error', manejarError);
            objXMLHTTP.send();
            
            function manejarError(evt) {
                console.log('ocurrio un error.');
            }

            function completado(evt) {
                let dataConsulta = JSON.parse(this.response);
                window.alert(dataConsulta.respuesta);
                document.getElementById("promedioFinal").innerHTML = dataConsulta.promedio;
                
            }
} 
