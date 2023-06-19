$(document).ready(function(){
    $("#Ingresar").click(function(){

            var expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
            var expPass = /^.{4,12}$/;

            
            var nombre = $("#nombre").val();
            var apellido = $("#apellido").val();
            var correo = $("#correo").val();
            var contraseña = $("#contraseña").val();
            var contraseña2 = $("#confcontraseña").val();

            if(nombre == ""){
                $("#alerta1").fadeIn();
                return false;
            }else{
                if(apellido == ""){
                    $("#alerta2").fadeIn();
                    return false;
                }
            }
            
            if(correo == "" || !expReg.test(correo)){
                $("#alerta3").fadeIn();
                return false;
            }

            if(contraseña == ""|| !expPass.test(contraseña)){
                $("#alerta4").fadeIn();
                return false;
            }else{
                if(contraseña2 == ""){
                    $("#alerta5").fadeIn();
                    return false;
                }else{
                    $("#alerta5").fadeOut();
                }
            }

            if(!expPass.test(contraseña2)){
                $("#alerta6").fadeIn();
                return false;
            }else{
                $("#alerta6").fadeOut();
            }

            if(contraseña != contraseña2){
                $("#alerta7").fadeIn();
                return false;
            }else{
                $("#alerta7").fadeOut();
            }
         
    })
});
