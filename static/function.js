$(".add-to-cart-btn").on("click", function(){

    let this_val = $(this)
    let index_val = this_val.attr("data-index")

    let quantity = $(".dish-quantity-" + index_val).val()
    let dish_title = $(".dish-title-" + index_val).val()
    let dish_id = $(".dish-id-" + index_val).val()
    let dish_did = $(".dish-did-" + index_val).val()
    let dish_price = $(".current-dish-price-" + index_val).text()
    let dish_photo = $(".dish-photo-" + index_val).val()


    console.log("Quantity: ", quantity);
    console.log("Title: ", dish_title);
    console.log("Price: ", dish_price);
    console.log("ID: ", dish_id);
    console.log("Dish_ID: ", dish_did);
    console.log("Photo: ", dish_photo);
    console.log("Index: ", index_val);
    console.log("Current element: ", this_val);

    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': dish_id,
            'dish_id': dish_did,
            'photo': dish_photo,
            'qty': quantity,
            'title': dish_title,
            'price': dish_price,
        },
        dataType: 'json',
        beforeSend: function(){
          console.log("Adding to the cart...");
        },
        success: function(response){
            this_val.html("Added to cart")
            console.log("Added!");
            // $(".cart-items-count").text(response.totalcartitems)
        }
    })
})