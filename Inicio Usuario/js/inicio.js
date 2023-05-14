$(document).ready(function(){
    $("#Ingresar").click(function(){

        
        var nombre = $("#nombre").val();
        var pass = $("#password").val();

        if(nombre == ""){
            $("#alerta1").fadeIn();
            return false;
        }else{
            if(pass == ""){
                $("#alerta2").fadeIn();
                 return false;
            }
        }
        
    })
});

