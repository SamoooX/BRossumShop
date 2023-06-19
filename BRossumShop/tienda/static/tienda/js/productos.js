$(document).ready(function () {
    num = 1 

    $("#activarBalon").click(function () {
        // Obtener el elemento del icono del carrito de compras
        var carritoIcono = $("#carrito");

        // Agregar una clase "pendiente" al elemento del icono del carrito de compras
        carritoIcono.addClass("pendiente");
    });

    for (let i = 1; i <= 20; i++) {

        $.get("https://fakestoreapi.com/products/" + num, function (data) {

            $(".tuki").append("<div class='col-lg-3 col-md-6 mb-4'>"
            + "<div class='card h-100'>" 
            + "<img class='card-img-top' src='" + data.image + "' alt=''>"
            +  "<div class='card-body'>"
            +    "<h4 class='card-title'>" + data.title + "</h4>"
            +    "<h5> $"  + data.price + "</h5>"
            +    "<p class='card-text'>" + data.description + "</p>"
            +  "</div>"
            +  "<div class='card-footer'>"
            +    "<a href='#' class='btn btn-block Agregar'>Añadir al carrito</a>"
            +  "</div>"
            + "</div>"
            + "</div>");

            // Agregar controlador de eventos click al botón "Añadir al carrito"
            $(".Agregar").last().click(function () {
                $('#añadirModal').modal('show'); // Mostrar el modal        
            });
        });
        num++
        if (num % 20 == 1) num = 1
    };

});
