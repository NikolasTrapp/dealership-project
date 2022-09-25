$(function () {

    $(document).on("click", "#queryvehicles", function () {

        $.ajax({
            url: "http://localhost:5000/listVehicles",
            method: "GET",
            dataType: 'json',
            success: loadVehiclesTable,
            error: function (response) {
                alert("Some error ocourred! backend details: " + response.details);
            }
        });
    });

    $(document).on("click", "#querycustomers", function () {

        $.ajax({
            url: "http://localhost:5000/listCustomers",
            method: "GET",
            dataType: 'json',
            success: loadCustomersTable,
            error: function (response) {
                alert("Some error ocourred! backend details: " + response.details);
            }
        });
    });

    $(document).on("click", "#querysales", function () {

        $.ajax({
            url: "http://localhost:5000/listSales",
            method: "GET",
            dataType: 'json',
            success: loadSales,
            error: function (response) {
                alert("Some error ocourred! backend details: " + response.details);
            }
        });
    });

    function loadSales(response) {
        $("#graphic").remove();
        $(".table").remove();
        const div = document.createElement("div");
        div.id = "graphic";
        document.body.appendChild(div);
        var layout = {
            height: 400,
            width: 500
        };
        Plotly.newPlot('graphic', [response.details], layout);
    }

    function loadCustomersTable(response) {
        $("#graphic").remove();
        $(".table").remove();
        const table = createCustomersTable();
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
        $("body").append(table);
    }

    function loadVehiclesTable(response) {
        $("#graphic").remove();
        $(".table").remove();
        const table = createVehiclesTable();
        response.details.map(v => {
            // const tbody = $("#vehiclestablebody");
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
            tbodyRowMileage.innerHTML = v.mileage + " km";
            const tbodyRowEngineCapacity = tbodyRow.insertCell(5);
            tbodyRowEngineCapacity.innerHTML = (v.type === "car" ? v.engine_capacity + " HP" : v.engine_capacity + " CC");
            const tbodyRowPrice = tbodyRow.insertCell(6);
            tbodyRowPrice.innerHTML = "R$ " + v.price;
            const tbodyRowType = tbodyRow.insertCell(7);
            tbodyRowType.innerHTML = v.type;
        });
        $("body").append(table);
    }

    function createCustomersTable() {
        const table = document.createElement("table");
        table.classList = "table table-bordered";
        const thead = table.createTHead();
        const theadRow = thead.insertRow();
        const theadRowId = theadRow.insertCell(0);
        theadRowId.innerHTML = "Id";
        const theadRowName = theadRow.insertCell(1);
        theadRowName.innerHTML = "Name";
        const theadRowAge = theadRow.insertCell(2);
        theadRowAge.innerHTML = "Age";
        const theadRowCpf = theadRow.insertCell(3);
        theadRowCpf.innerHTML = "CPF";
        const theadRowEmail = theadRow.insertCell(4);
        theadRowEmail.innerHTML = "Email";
        const theadRowPassword = theadRow.insertCell(5);
        theadRowPassword.innerHTML = "Password";
        const tbody = table.createTBody();
        tbody.id = "customerstablebody"
        return table;
    }

    function createVehiclesTable() {
        const table = document.createElement("table");
        table.classList = "table table-bordered";
        const thead = table.createTHead();
        const theadRow = thead.insertRow();
        const theadRowId = theadRow.insertCell(0);
        theadRowId.innerHTML = "Id";
        const theadRowName = theadRow.insertCell(1);
        theadRowName.innerHTML = "Name";
        const theadRowColor = theadRow.insertCell(2);
        theadRowColor.innerHTML = "Color";
        const theadRowYear = theadRow.insertCell(3);
        theadRowYear.innerHTML = "Year";
        const theadRowMileage = theadRow.insertCell(4);
        theadRowMileage.innerHTML = "Mileage";
        const theadRowEngineCapacity = theadRow.insertCell(5);
        theadRowEngineCapacity.innerHTML = "Engine Capacity";
        const theadRowPrice = theadRow.insertCell(6);
        theadRowPrice.innerHTML = "Price";
        const theadRowType = theadRow.insertCell(7);
        theadRowType.innerHTML = "Type";
        const tbody = table.createTBody();
        tbody.id = "vehiclestablebody";
        return table;
    }

});