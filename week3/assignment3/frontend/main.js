fillTable(true);

/*
* We were asked to create a reset button for the form in the index page that will send the form to the server via a
* HTTP GET. The problem is that this form already uses the method POST when the user presses the button submit.
* This function chooses the right form method and completes the form submission.
* */
function submitForm(caller) {

    var data ={
        brand: $('#inputBrand').val(),
        model: $('#inputModel').val(),
        os: $('#inputOS').val(),
        screensize: $('#inputScreensize').val(),
        image: $('#inputImage').val()
    }
    form = document.getElementById("myForm");
    if(caller.value === "submit") {
        $.ajax({
            url: 'http://localhost:8089/api',
            type: 'POST',
            data: data
        }).done(function(data,status,xhr){
            console.log("jens here");
            console.log(data.URI);
            console.log(data,status, xhr);
            fillTable(false);
        });
    } else if (caller.value === "reset") {
        $.ajax({
            url: 'http://localhost:8089/api',
            type: 'GET',
            data: data
        }).done(function(data,status,xhr){
        });
    }
}

/*
This function should be called at the beginning of the code to fill in the table with data coming from VU's server.
It expects the argument start to be true when initializing the table and false otherwise.
*/
function fillTable(start){
    if (start === true){
        //ask all the elements from VU's server, loop through all items in the json response and fill the table
        $.ajax({
            url: 'http://localhost:8089/api',
            dataType: 'json',
            type: 'GET',
        }).done(function(data,status,xhr){
            console.log(data);
            var i;
            for ( i=0; i < data.length; i++ ) {
                var row = '<tr><td>' + data[i].brand + '</td>'
                + '<td>' + data[i].model + '</td>'
                + '<td>' + data[i].os + '</td>'
                + '<td>' + data[i].screensize + '</td>'
                + '<td><img src="' + data[i].image + '" class="phones"></td>'
                + '</tr>    ';
                console.log(row);
                $("#TopSellingModelsTable").prepend(row);
            }
        });
    } else if(start === false) {
        var data ={
            brand: $('#inputBrand').val(),
            model: $('#inputModel').val(),
            os: $('#inputOS').val(),
            screensize: $('#inputScreensize').val(),
            image: $('#inputImage').val()
        }
        var row = '<tr><td>' + data.brand + '</td>'
            + '<td>' + data.model + '</td>'
            + '<td>' + data.os + '</td>'
            + '<td>' + data.screensize + '</td>'
            + '<td><img src="' + data.image + '" class="phones"></td>'
            + '</tr>>';
        console.log(row);
        $("#TopSellingModelsTable").prepend(row);
    }
}

/*
source for function sortTable(n): https://www.w3schools.com/howto/howto_js_sort_table.asp
explanation: sorts the table using bubble sort */
function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("TopSellingModelsTable");
    switching = true;
    //Set the sorting direction to ascending:
    dir = "asc";
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
        //start by saying: no switching is done:
        switching = false;
        rows = table.getElementsByTagName("TR");
        //rows.pop();
        /*Loop through all table rows (except the
        first, which contains table headers):*/
        for (i = 1; i < (rows.length - 2); i++) {
            //start by saying there should be no switching:
            shouldSwitch = false;
            /*Get the two elements you want to compare,
            one from current row and one from the next:*/
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            /*check if the two rows should switch place,
            based on the direction, asc or desc:*/
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    //if so, mark as a switch and break the loop:
                    shouldSwitch= true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    //if so, mark as a switch and break the loop:
                    shouldSwitch= true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            /*If a switch has been marked, make the switch
            and mark that a switch has been done:*/
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            //Each time a switch is done, increase this count by 1:
            switchcount ++;
        } else {
            /*If no switching has been done AND the direction is "asc",
            set the direction to "desc" and run the while loop again.*/
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}