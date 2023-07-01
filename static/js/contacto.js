/*jquery */
function validarFormulario(){
}

$(document).ready(function() {
    const nombreLenth = 3;
    const asuntoLenth = 3;
    const mensajeLength = 20; 
    

    $("#basic-form").validate({
        rules:{
            nombre:{
                required:true,
                minlength: nombreLenth
                
            },
            correo: {
                required: true,
                email: true
            },
            asunto: {
                required: true,
                minlength: asuntoLenth
            },
            mensaje:{
                required: true,
                minlength: mensajeLength
            }
        },
        messages:{
            nombre:{
                required: mensajeRequired("nombre"),
                minlength: mensajeMinLength(nombreLenth)
            },
            correo: {
                required: mensajeRequired("correo"),
                email: "debe ser un correo con formato contacto@contacto.com"
            },
            asunto:{
                required: mensajeRequired("asunto"),
                minlength: mensajeMinLength(asuntoLenth)
            },
            mensaje:{
                required: mensajeRequired("mensaje"),
                minlength: mensajeMinLength(mensajeLength)
            }
        }
    } );

  });

