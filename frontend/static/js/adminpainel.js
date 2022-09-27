$(function () {

    $('#queryvehicles').on('click', function () {

        $.ajax({
            url: 'http://localhost:5000/listVehicles',
            method: 'GET',
            dataType: 'json',
            success: loadVehiclesTable,
            error: function (response) {
                alert('Some error ocourred! backend details: ' + response.details);
            }
        });
    });

    $('#querycustomers').on('click', function () {

        $.ajax({
            url: 'http://localhost:5000/listCustomers',
            method: 'GET',
            dataType: 'json',
            success: loadCustomersTable,
            error: function (response) {
                alert('Some error ocourred! backend details: ' + response.details);
            }
        });
    });

    $('#querysales').on('click', function () {
        $.ajax({
            url: 'http://localhost:5000/listSales',
            method: 'GET',
            dataType: 'json',
            success: loadSales,
            error: function (response) {
                alert('Some error ocourred! backend details: ' + response.details);
            }
        });
    });

    $("#queryoffers").on("click", function(){
        $.ajax({
            url: 'http://localhost:5000/listOffers',
            method: 'GET',
            dataType: 'json',
            success: loadOffers,
            error: function (response) {
                alert('Some error ocourred! backend details: ' + response.details);
            }
        });
    });

    function loadOffers(response){
        console.log(response);
        $('#graphic').remove();
        $('.table').remove();
        createOffersTable();
        response.details.map(o => {
            const row = $("<tr></tr>");
            const tdId = $("<td></td>").text(o.id);
            const tdDate = $("<td></td>").text(o.date);
            const tdAdress = $("<td></td>").text(o.adress);
            const tdAdressNumber = $("<td></td>").text(o.adress_number);
            const tdPhone = $("<td></td>").text(o.phone);
            const tdEmail = $("<td></td>").text(o.email);
            const tdCustomerId = $("<td></td>").text(o.customer);
            const tdVehicleId = $("<td></td>").text(o.vehicle);
            row.append(tdId, tdDate, tdAdress, tdAdressNumber, tdPhone,
                 tdEmail, tdCustomerId, tdVehicleId);
            $("#offerstablebody").append(row);
        });
    }

    function loadSales(response) {
        $('#graphic').remove();
        $('.table').remove();
        const div = $("<div></div>").attr("id", "graphic");
        $("#tables").append(div);
        var layout = {
            height: 400,
            width: 500
        };
        Plotly.newPlot('graphic', [response.details], layout);
    }

    function loadCustomersTable(response) {
        $('#graphic').remove();
        $('.table').remove();
        createCustomersTable();
        response.details.map(c => {
            const row = $("<tr></tr>");
            const tdId = $("<td></td>").text(c.id);
            const tdName = $("<td></td>").text(c.name);
            const tdAge = $("<td></td>").text(c.age);
            const tdCpf = $("<td></td>").text(c.cpf);
            const tdEmail = $("<td></td>").text(c.email);
            const tdPassword = $("<td></td>").text(c.password);
            row.append(tdId, tdName, tdAge, tdCpf, tdEmail, tdPassword);
            console.log(row);
            $("#customerstablebody").append(row);
        });
    }

    function loadVehiclesTable(response) {
        $('#graphic').remove();
        $('.table').remove();
        const table = createVehiclesTable();
        response.details.map(v => {
            // const tbody = $('#vehiclestablebody');
            const row = $("<tr></tr>");
            const tdId = $("<td></td>").text(v.id);
            const tdName = $("<td></td>").text(v.name);
            const tdColor = $("<td></td>").text(v.color);
            const tdYear = $("<td></td>").text(v.year);
            const tdMileage = $("<td></td>").text(v.mileage + "Km");
            const tdEngineCapacity = $("<td></td>").text(v.type === 'car' ? v.engine_capacity + ' HP' : v.engine_capacity + ' CC');
            const tdPrice = $("<td></td>").text(v.price);
            const tdType = $("<td></td>").text(v.type);
            row.append(tdId, tdName, tdColor, tdYear, tdMileage, tdEngineCapacity, tdPrice, tdType);
            $("#vehiclestablebody").append(row);
        });
    }

    function createCustomersTable() {
        const table = $("<table></table>").addClass("table table-bordered");
        const thead = $("<thead></thead>");
        const theadRow = $("<tr></tr>");
        const tbody = $("<tbody></tbody>").attr("id", "customerstablebody");
        const thID = $("<th></th>").text("Id");
        const thName = $("<th></th>").text("Name");
        const thAge = $("<th></th>").text("Age");  
        const thCpf = $("<th></th>").text("CPF");
        const thEmail = $("<th></th>").text("Email");
        const thPassword = $("<th></th>").text("Password");
        theadRow.append(thID, thName, thAge, thCpf, thEmail, thPassword);
        thead.append(theadRow);
        table.append(thead);
        table.append(tbody);
        $("#tables").append(table);
    }

    function createVehiclesTable() {
        const table = $("<table></table>").addClass("table table-bordered");
        const thead = $("<thead></thead>");
        const theadRow = $("<tr></tr>");
        const tbody = $("<tbody></tbody>").attr("id", "vehiclestablebody");
        const thId = $("<th></th>").text("Id");
        const thName = $("<th></th>").text("Name");
        const thColor = $("<th></th>").text("Color");
        const thYear = $("<th></th>").text("Year");
        const thMileage = $("<th></th>").text("Mileage");
        const thEngineCapacity = $("<th></th>").text("Engine Capacity");
        const thPrice = $("<th></th>").text("Price");
        const thType = $("<th></th>").text("Type");
        theadRow.append(thId, thName, thColor, thYear, thMileage,
                        thEngineCapacity, thPrice, thType);
        thead.append(theadRow);
        table.append(thead);
        table.append(tbody);
        $("#tables").append(table);
    }

    function createOffersTable() {
        const table = $("<table></table>").addClass("table table-bordered");
        const thead = $("<thead></thead>");
        const theadRow = $("<tr></tr>");
        const tbody = $("<tbody></tbody>").attr("id", "offerstablebody");
        const thId = $("<th></th>").text("Id");
        const thDate = $("<th></th>").text("Date");
        const thAdress = $("<th></th>").text("Adress");
        const thAdressNumber = $("<th></th>").text("Adress number");
        const thPhone = $("<th></th>").text("Phone");
        const thEmail = $("<th></th>").text("Email");
        const thCustomerId = $("<th></th>").text("Customer Id");
        const thVehicleId = $("<th></th>").text("Vehicle Id");
        theadRow.append(thId, thDate, thAdress, thAdressNumber, thPhone,
             thEmail, thCustomerId, thVehicleId);
        thead.append(theadRow);
        table.append(thead);
        table.append(tbody);
        $("#tables").append(table);
    }


    $('#sendvehicle').on('click', function() {
        let name = $('#vehiclename').val();
        let color = $('#vehiclecolor').val();
        let year = $('#vehicleyear').val();
        let mileage = $('#vehiclemileage').val();
        let engine_capacity = $('#vehicleenginecapacity').val();
        let price = $('#vehicleprice').val();
        let vehicletype = $('#vehicletype').val();
        let image_name = $('#vehicleimage').val().substr(12);

        let vehicledata = JSON.stringify({
            name: name,
            color: color,
            year: year,
            mileage: mileage,
            engine_capacity: engine_capacity,
            price: price,
            image_name: image_name
        });

        $.ajax({
            url: 'http://localhost:5000/add' + vehicletype,
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: vehicledata,
            success: function (response) {
                console.log(response);
                if (response.result != "ok") return;
                sendImage()
            },
            error: function (response) {
                console.log(response);
                alert('pause2');
            }
        });
    });

    function sendImage() {
        var image = new FormData($('#vehicleform')[0]);

        $.ajax({
            url: 'http://localhost:5000/save_image',
            method: 'POST',
            data: image,
            contentType: false,
            cache: false,
            processData: false,
            success: function (response) {
                console.log(response);
                // if (response.result != 'ok') return;
                sendVehicle();
            },
            error: function (response) {
                alert('Backend message: ' + response.result);
            }
        });
    }

    $("#sendcustomer").on("click", function(){
        let name = $("#customername").val();
        let age = $("#customerage").val();
        let cpf = $("#customercpf").val();
        let email = $("#customeremail").val();
        let password = $("#customerpassword").val();

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

    $("#sendsale").on("click", function(){
        let value = $("#salevalue").val();
        let customer_id = $("#selectcustomer").val();
        let employee_id = $("#selectemployee").val();
        let vehicle_id = $("#selectvehicle").val();

        let data = JSON.stringify({
            value: value,
            customer_id: customer_id,
            employee_id: employee_id,
            vehicle_id: vehicle_id
        });

        console.log(data);

        $.ajax({
            url: "http://localhost:5000/addSale",
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

    $("#removecustomerbt").on("click", function(){
        let customer_id = $("#selectcustomer-remove").val();
        
        $.ajax({
            url: "http://localhost:5000/deleteCustomer/" + customer_id,
            method: "DELETE",
            success: function(result){
                console.log(result);
            },
            error: function(result){
                console.log(result);
            }
        });
    });

    $("#removevehiclebt").on("click", function(){
        let vehicle_id = $("#selectvehicle-remove").val();
        let vehicle_type = $("#selectvehicle-remove").find(":selected").attr("rel");
        let vt = vehicle_type[0].toUpperCase() + vehicle_type.substring(1);
        console.log(vehicle_id);
        console.log(vehicle_type);
        console.log(vt);
        
        $.ajax({
            url: `http://localhost:5000/delete${vt}/${vehicle_id}`,
            method: "DELETE",
            success: function(result){
                console.log(result);
            },
            error: function(result){
                console.log(result);
            }
        });
    });

    $.ajax({
        url: "http://localhost:5000/getData",
        method: "GET",
        dataType: "json",
        success: function (data){
            console.log(data);
            data.vehicles.map(v => {
                $("#selectvehicle").append(`<option value="${v.id}">${v.name}</option>`)
                $("#selectvehicle-remove").append(`<option rel=${v.type} value="${v.id}">${v.name}</option>`)
            });
            data.employees.map(e => {
                $("#selectemployee").append(`<option value="${e.id}">${e.name}</option>`)
            });
            data.customers.map(c => {
                $("#selectcustomer").append(`<option value="${c.id}">${c.name}</option>`)
                $("#selectcustomer-remove").append(`<option value="${c.id}">${c.name}</option>`)
            });
            createOffersTable();
            data.offers.map(o => {
                const row = $("<tr></tr>");
                const tdId = $("<td></td>").text(o.id);
                const tdDate = $("<td></td>").text(o.date);
                const tdAdress = $("<td></td>").text(o.adress);
                const tdAdressNumber = $("<td></td>").text(o.adress_number);
                const tdPhone = $("<td></td>").text(o.phone);
                const tdEmail = $("<td></td>").text(o.email);
                const tdCustomerId = $("<td></td>").text(o.customer);
                const tdVehicleId = $("<td></td>").text(o.vehicle);
                row.append(tdId, tdDate, tdAdress, tdAdressNumber, tdPhone,
                     tdEmail, tdCustomerId, tdVehicleId);
                $("#offerstablebody").append(row);
            });
        },
        error: function() {
            alert("erro");
        }
    });
});