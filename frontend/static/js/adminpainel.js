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

    function loadSales(response) {
        $('#graphic').remove();
        $('.table').remove();
        const div = document.createElement('div');
        div.id = 'graphic';
        document.body.appendChild(div);
        var layout = {
            height: 400,
            width: 500
        };
        Plotly.newPlot('graphic', [response.details], layout);
    }

    function loadCustomersTable(response) {
        $('#graphic').remove();
        $('.table').remove();
        const table = createCustomersTable();
        console.log(response.details);
        response.details.map(c => {
            const tbodyRow = table.insertRow();
            const tbodyRowId = tbodyRow.insertCell(0);
            tbodyRowId.innerHTML = c.id;
            const tbodyRowName = tbodyRow.insertCell(1);
            tbodyRowName.innerHTML = c.name;
            const tbodyRowAge = tbodyRow.insertCell(2);
            tbodyRowAge.innerHTML = c.age;
            const tbodyRowCpf = tbodyRow.insertCell(3);
            tbodyRowCpf.innerHTML = c.cpf;
            const tbodyRowEmail = tbodyRow.insertCell(4);
            tbodyRowEmail.innerHTML = c.email;
            const tbodyRowPassword = tbodyRow.insertCell(5);
            tbodyRowPassword.innerHTML = c.password;
        });
        $('body').append(table);
    }

    function loadVehiclesTable(response) {
        $('#graphic').remove();
        $('.table').remove();
        const table = createVehiclesTable();
        response.details.map(v => {
            // const tbody = $('#vehiclestablebody');
            const tbodyRow = table.insertRow();
            const tbodyRowId = tbodyRow.insertCell(0);
            tbodyRowId.innerHTML = v.id;
            const tbodyRowName = tbodyRow.insertCell(1);
            tbodyRowName.innerHTML = v.name;
            const tbodyRowColor = tbodyRow.insertCell(2);
            tbodyRowColor.innerHTML = v.color;
            const tbodyRowYear = tbodyRow.insertCell(3);
            tbodyRowYear.innerHTML = v.year;
            const tbodyRowMileage = tbodyRow.insertCell(4);
            tbodyRowMileage.innerHTML = v.mileage + ' km';
            const tbodyRowEngineCapacity = tbodyRow.insertCell(5);
            tbodyRowEngineCapacity.innerHTML = (v.type === 'car' ? v.engine_capacity + ' HP' : v.engine_capacity + ' CC');
            const tbodyRowPrice = tbodyRow.insertCell(6);
            tbodyRowPrice.innerHTML = 'R$ ' + v.price;
            const tbodyRowType = tbodyRow.insertCell(7);
            tbodyRowType.innerHTML = v.type;
        });
        $('body').append(table);
    }

    function createCustomersTable() {
        const table = document.createElement('table');
        table.classList = 'table table-bordered';
        const thead = table.createTHead();
        const theadRow = thead.insertRow();
        const theadRowId = theadRow.insertCell(0);
        theadRowId.innerHTML = 'Id';
        const theadRowName = theadRow.insertCell(1);
        theadRowName.innerHTML = 'Name';
        const theadRowAge = theadRow.insertCell(2);
        theadRowAge.innerHTML = 'Age';
        const theadRowCpf = theadRow.insertCell(3);
        theadRowCpf.innerHTML = 'CPF';
        const theadRowEmail = theadRow.insertCell(4);
        theadRowEmail.innerHTML = 'Email';
        const theadRowPassword = theadRow.insertCell(5);
        theadRowPassword.innerHTML = 'Password';
        const tbody = table.createTBody();
        tbody.id = 'customerstablebody';    
        return table;
    }

    function createVehiclesTable() {
        const table = document.createElement('table');
        table.classList = 'table table-bordered';
        const thead = table.createTHead();
        const theadRow = thead.insertRow();
        const theadRowId = theadRow.insertCell(0);
        theadRowId.innerHTML = 'Id';
        const theadRowName = theadRow.insertCell(1);
        theadRowName.innerHTML = 'Name';
        const theadRowColor = theadRow.insertCell(2);
        theadRowColor.innerHTML = 'Color';
        const theadRowYear = theadRow.insertCell(3);
        theadRowYear.innerHTML = 'Year';
        const theadRowMileage = theadRow.insertCell(4);
        theadRowMileage.innerHTML = 'Mileage';
        const theadRowEngineCapacity = theadRow.insertCell(5);
        theadRowEngineCapacity.innerHTML = 'Engine Capacity';
        const theadRowPrice = theadRow.insertCell(6);
        theadRowPrice.innerHTML = 'Price';
        const theadRowType = theadRow.insertCell(7);
        theadRowType.innerHTML = 'Type';
        const tbody = table.createTBody();
        tbody.id = 'vehiclestablebody';
        return table;
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
        let adress = $("#customeradress").val();
        let adress_number = $("#customeadressnumber").val();
        let cpf = $("#customercpf").val();
        let email = $("#customeremail").val();
        let password = $("#customerpassword").val();

        let data = JSON.stringify({
            name: name,
            age: age,
            adress: adress,
            adress_number: adress_number,
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
            })
            data.employees.map(e => {
                $("#selectemployee").append(`<option value="${e.id}">${e.name}</option>`)
            })
            data.customers.map(c => {
                $("#selectcustomer").append(`<option value="${c.id}">${c.name}</option>`)
                $("#selectcustomer-remove").append(`<option value="${c.id}">${c.name}</option>`)
            })
        },
        error: function() {
            alert("erro");
        }
    });


});