$(function () {

    $(document).on('click', '.addinterest', function () {
        let rel = this.rel.split("|");
        let name = rel[0];
        let id = rel[1];
        $("#setinteresttitle").text("Add interest to " + name);
        $("#sendinterest").attr("rel", id);

    });

    $("#sendinterest").on("click", function () {
        if (sessionStorage.getItem("session") === null){
            alert("do login!");
        } else {
            let adress = $("#customeradress").val();
            let adress_number = $("#customeradressnumber").val();
            let email = $("#customeremail").val();
            let phone = $("#customerphone").val();
            let customer_id = JSON.parse(sessionStorage.session).id;
            let vehicle_id = $("#sendinterest").attr("rel");

            let data = JSON.stringify({
                adress: adress,
                adress_number: adress_number,
                email: email,
                phone: phone,
                customer_id: customer_id,
                vehicle_id: vehicle_id
            });

            $.ajax({
                url: "http://localhost:5000/addInterest",
                method: "POST",
                dataType: "json",
                contentType: "application/json",
                data: data,
                success: function(response){
                    if (response.result === "ok"){
                        alert("Your interest has been saved, we will contact you shortly");
                    } else {
                        console.log(response);
                    }
                },
                error: function(response) {
                    console.log(response);
                }
            });
        }
    });

    $("#sendregistercustomer").on("click", function(){
        let name = $("#registercustomername").val();
        let age = $("#registercustomerage").val();
        let cpf = $("#registercustomercpf").val();
        let email = $("#registercustomeremail").val();
        let password = $("#registercustomerpassword").val();

        let data = JSON.stringify({
            name: name,
            age: age,
            cpf: cpf,
            email: email,
            password: password
        });

        $.ajax({
            url: "http://localhost:5000/addCustomer",
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: data,
            success: function(result){
                console.log(result);
            },
            error: function(result){
                console.log(result);
            }
        });
    });

    $.ajax({
        url: "http://192.168.1.3:5000/listCars",
        method: "GET",
        dataType: "json",
        success: function (response) {
            response.details.map(c => {
                let mainDiv = $("<div></div>").addClass("card").attr("style", "width: 18rem;");
                let image = $("<img>").attr("src", "http://192.168.1.3:5000/get_image/" + c.id);
                let bodyDiv = $("<div></div>").addClass("card-body");
                let cardTitle = $("<h5></h5>").addClass("card-title").text(c.name);
                let cardTextName = $("<p></p>").addClass("card-text").text("R$ " + c.price);
                let cardTextMileage = $("<p></p>").addClass("card-text").text(c.mileage + " Km");
                let link = $("<a></a>").attr("href", "#").addClass("btn btn-primary addinterest")
                    .text("I have interest").attr("data-bs-toggle", "modal")
                    .attr("data-bs-target", "#setinterest").attr("rel", c.name + "|" + c.id);
                bodyDiv.append(cardTitle);
                bodyDiv.append(cardTextName);
                bodyDiv.append(cardTextMileage);
                bodyDiv.append(link);
                mainDiv.append(image);
                mainDiv.append(bodyDiv);
                $("#cars").append(mainDiv);
            });
        },
        error: function () {
            $("#cars").append($("<h3></h3>").text("Nothing to see here... :("))
        }
    });

    $.ajax({
        url: "http://192.168.1.3:5000/listMotorcycles",
        method: "GET",
        dataType: "json",
        success: function (response) {
            response.details.map(m => {
                let mainDiv = $("<div></div>").addClass("card").attr("style", "width: 18rem;");
                let image = $("<img>").attr("src", "http://192.168.1.3:5000/get_image/" + m.id);
                let bodyDiv = $("<div></div>").addClass("card-body");
                let cardTitle = $("<h5></h5>").addClass("card-title").text(m.name);
                let cardTextName = $("<p></p>").addClass("card-text").text("R$ " + m.price);
                let cardTextMileage = $("<p></p>").addClass("card-text").text(m.mileage + " Km");
                let link = $("<a></a>").attr("href", "#").addClass("btn btn-primary addinterest")
                    .text("I have interest").attr("id", "addinterest").attr("data-bs-toggle", "modal")
                    .attr("data-bs-target", "#setinterest").attr("rel", m.name + "|" + m.id);
                bodyDiv.append(cardTitle);
                bodyDiv.append(cardTextName);
                bodyDiv.append(cardTextMileage);
                bodyDiv.append(link);
                mainDiv.append(image);
                mainDiv.append(bodyDiv);
                $("#motorcycles").append(mainDiv);
            });
        },
        error: function () {
            $("#motorcycles").append($("<h3></h3>").text("Nothing to see here... :("));
        }
    });

    $("#sendlogin").on("click", function () {
        let name = $("#customername").val();
        let email = $("#customeremaillogin").val();
        let password = $("#customerpassword").val();

        let data = JSON.stringify({
            name: name,
            email: email,
            password: password
        });

        $.ajax({
            url: "http://localhost:5000/validate_login",
            method: "POST",
            contentType: "application/json",
            dataType: "json",
            data: data,
            success: function (response) {
                if (response.result === "ok") {
                    sessionStorage.setItem("session", JSON.stringify(response.details));
                    sessionStorage.setItem("token", response.token);
                    alert("Login approved");
                    $('#loginmodal').modal('hide');
                } else {
                    alert(response.details);
                }
            },
            error: function (response) {
                alert(response.details);
            }
        });

    });

});