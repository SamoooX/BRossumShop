$(document).ready(function () {
    num = 1 

    for (let i = 1; i <= 2; i++) {

        $.get("https://fakestoreapi.com/products/" + num, function (data) {

            $(".Lista").append(
            "<div class='card'>"
            +  "<div class='card-body'>"
            +    "<h5 class='text-center'>"+data.title+"</h5>"
            +   "<div class='row mb-3 pt-3'>"
            +      "<div class='col-4'>"
            +        "<img src='"+ data.image +"' alt='' id='iphone'>"
            +      "</div>"
            +      "<div class='col-4'>"
            +        "<p class='text-light'>Pedido en camino...</p>"
            +      "</div>"
            +      "<div class='col-4'>"
            +        "<input type='submit' class='btn btn-block Cancelar' value='CANCELAR PEDIDO'>"
            +      "</div>"
            +    "</div>"
            +  "</div>"
            +"</div>"
            +"</div>");

            // $(".Cancelar").last().click(function(){
            //     $('#modalCancelar').modal('show');
            // });
                
            
        });
        num++
        if (num % 2 == 1) num = 1
    };

    $(document).on('click','.Cancelar', function(event){
        event.preventDefault();
        $(this).closest('.card').remove();
        
    });
    


});