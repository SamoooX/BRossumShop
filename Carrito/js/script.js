$(document).ready(function () {
    num = 1
    var total = 0
    var precio = 0
    $("#enviar").click(function () {

        $.get("https://fakestoreapi.com/products/" + num, function (data) {

            $(".carrito").append("<div class='row mb-2'> <hr> <div class='col-md-3'>"
                + "<img src='" + data.image + "' alt='Product Image' class='img-fluid'></div>" +
                "<div class='col-md-9'>"
                + "<h5>Producto: " + data.title + "</h5>"
                + "<p>Precio: $<span class='precio'>" + data.price + "</span></p>"
                + "<p>Cantidad: 1 </p>"
                + "<button class='btn btn-sm btn-danger borrar'>Eliminar</button>"
                + "</div>"
                + "</div>");

            total = (parseFloat(total) + parseFloat(data.price)).toFixed(2);

            $("#total").text(

                '$' + total

            );

        });
        num++
        if (num % 20 == 1) num = 1
    });

    // antiado un nuevo click por cada boton borrar

    $(document).on('click', '.borrar', function (event) {
        precio = $(this).closest('.row').find('.precio').text();
        total = (parseFloat(total) - parseFloat(precio)).toFixed(2);
        $("#total").text(
            '$' + total
        );

        event.preventDefault();
        $(this).closest('div.row').remove();


    });
});
