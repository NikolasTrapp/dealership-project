$(function (){
    $.ajax({
        url: "http://localhost:5000/listCars",
        method: "GET",
        dataType: "json",
        success: function (response){
            response.details.map(c => {
                let mainDiv = $("<div></div>").attr("class", "card").attr("style", "width: 18rem;");
                let image = $("<img>").attr("src", "http://localhost:5000/get_image/"+c.id);
                let bodyDiv = $("<div></div>").attr("class", "card-body");
                let cardTitle = $("<h5></h5>").attr("class", "card-title").text(c.name);
                let cardText = $("<p></p>").attr("class", "card-text").text(c.price);
                let link = $("<a></a>").attr("href", "#").attr("class", "btn btn-primary").text("Add to cart");
                bodyDiv.append(cardTitle);
                bodyDiv.append(cardText);
                bodyDiv.append(link);
                mainDiv.append(image);
                mainDiv.append(bodyDiv);
                $("#cars").append(mainDiv);
            })
        }
    });

    $.ajax({
        url: "http://localhost:5000/listMotorcycles",
        method: "GET",
        dataType: "json",
        success: function (response){
            response.details.map(m => {
                let mainDiv = $("<div></div>").attr("class", "card text-center").attr("style", "width: 18rem;");
                let image = $("<img>").attr("src", "http://localhost:5000/get_image/"+m.id);
                let bodyDiv = $("<div></div>").attr("class", "card-body");
                let cardTitle = $("<h5></h5>").attr("class", "card-title").text(m.name);
                let cardText = $("<p></p>").attr("class", "card-text").text(m.price);
                let link = $("<a></a>").attr("href", "#").attr("class", "btn btn-primary").text("Add to cart");
                bodyDiv.append(cardTitle);
                bodyDiv.append(cardText);
                bodyDiv.append(link);
                mainDiv.append(image);
                mainDiv.append(bodyDiv);
                $("#motorcycles").append(mainDiv);
            })
        }
    });
});