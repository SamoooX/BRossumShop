$(document).ready(function(){
    $("#Ingresar").click(function(){

        var expPass = /^.{4,12}$/;

        var nombre = $("#nombre").val();
        var pass = $("#password").val();

        if(nombre == ""){
            $("#alerta1").fadeIn();
            return false;
        }else{
            if(pass == "" || !expPass.test(pass)){
                $("#alerta2").fadeIn();
                 return false;
            }
        }
        
    })
});
