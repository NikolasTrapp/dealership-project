$(function (){

    $(document).on('click', '.addinterest', function () {
        console.log("OIoioi");
        let rel = this.rel.split("|");
        let name = rel[0];
        let id = rel[1];
        $("#setinteresttitle").text("Add interest to " + name);
        $("#sendinterest").attr("rel", id);
    });

    $("#sendinterest").on("click", function () {
        let adress = $("#customeradress").val();
        let adress_number = $("#customeradressnumber").val();
        let email = $("#customeremail").val();
        let phone = $("#custmerphone").val();
        let customer_id = localStorage.getItem("id");
        let vehicle_id = $("#sendinterest").attr("rel");

        let data = JSON.stringify({
            adress: adress,
            adress_number: adress_number,
            email: email,
            phone: phone,
            customer_id: customer_id,
            vehicle_id: vehicle_id
        });

        // $.ajax({
        //     url: "http://localhost:5000/addInterest",
        //     method: "POST",
        //     dataType: "json",
        //     contentType: "application/json",
        //     data: data,
        //     success: function(response){
        //         console.log(response);
        //     },
        //     error: function(response) {
        //         console.log(response);
        //     }
        // });
    })

    $.ajax({
        url: "http://192.168.1.3:5000/listCars",
        method: "GET",
        dataType: "json",
        success: function (response){
            response.details.map(c => {
                let mainDiv = $("<div></div>").addClass("card").attr("style", "width: 18rem;");
                let image = $("<img>").attr("src", "http://192.168.1.3:5000/get_image/"+c.id);
                let bodyDiv = $("<div></div>").addClass("card-body");
                let cardTitle = $("<h5></h5>").addClass("card-title").text(c.name);
                let cardTextName = $("<p></p>").addClass("card-text").text("R$ " + c.price);
                let cardTextMileage = $("<p></p>").addClass("card-text").text(c.mileage + " Km");
                let link = $("<a></a>").attr("href", "#").addClass("btn btn-primary addinterest")
                    .text("I have interest").attr("data-bs-toggle", "modal")
                    .attr("data-bs-target", "#setinterest").attr("rel", c.name+ "|" + c.id);
                bodyDiv.append(cardTitle);
                bodyDiv.append(cardTextName);
                bodyDiv.append(cardTextMileage);
                bodyDiv.append(link);
                mainDiv.append(image);
                mainDiv.append(bodyDiv);
                $("#cars").append(mainDiv);
            });
        },
        error: function(){
            $("#cars").append($("<h3></h3>").text("Nothing to see here... :("))
        }
    });

    $.ajax({
        url: "http://192.168.1.3:5000/listMotorcycles",
        method: "GET",
        dataType: "json",
        success: function (response){
            response.details.map(m => {
                let mainDiv = $("<div></div>").addClass("card").attr("style", "width: 18rem;");
                let image = $("<img>").attr("src", "http://192.168.1.3:5000/get_image/"+m.id);
                let bodyDiv = $("<div></div>").addClass("card-body");
                let cardTitle = $("<h5></h5>").addClass("card-title").text(m.name);
                let cardTextName = $("<p></p>").addClass("card-text").text("R$ " + m.price);
                let cardTextMileage = $("<p></p>").addClass("card-text").text(m.mileage + " Km");
                let link = $("<a></a>").attr("href", "#").addClass("btn btn-primary addinterest")
                    .text("I have interest").attr("id", "addinterest").attr("data-bs-toggle", "modal")
                    .attr("data-bs-target", "#setinterest").attr("rel", m.name+ "|" + m.id);
                bodyDiv.append(cardTitle);
                bodyDiv.append(cardTextName);
                bodyDiv.append(cardTextMileage);
                bodyDiv.append(link);
                mainDiv.append(image);
                mainDiv.append(bodyDiv);
                $("#motorcycles").append(mainDiv);
            });
        },
        error: function(){
            $("#motorcycles").append($("<h3></h3>").text("Nothing to see here... :("));
        }
    });
    
});