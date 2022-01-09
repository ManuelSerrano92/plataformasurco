window.addEventListener("load", cargueInformacion, true); function cargueInformacion() {

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
        document.getElementById("campoNombreInfo").textContent =dataConsulta.nombre;
        document.getElementById("campoApellidoInfo").textContent = dataConsulta.apellido;
        document.getElementById("codigoEnInfo").textContent = dataConsulta.id;
        document.getElementById("campoTelefonoInfo").value = dataConsulta.telefono;
        document.getElementById("campoCorreoInfo").value = dataConsulta.correo;

    }
}
