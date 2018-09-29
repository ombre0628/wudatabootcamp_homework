var tbody = d3.select("tbody");



// from data.js
var tableData = data;

tableData.forEach(function(UFOReport) {
    var row = tbody.append("tr");
    Object.entries(UFOReport).forEach(([key, value]) => {
        var cell = tbody.append("td");
        cell.text(value);
    });
});

console.log("test01");
// Select the submit button
var submit = d3.select("#filter-btn");
submit.on("click", function() {
    
    old_table = d3.select("tbody");
    old_table.remove();
    new_table = d3.select("#ufo-table");
    new_table.insert("tbody");

    var tbody = d3.select("tbody");
    
    console.log("click start");

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var inputElement_date = d3.select("#datetime");
    var inputElement_city = d3.select("#city");
    var inputElement_state = d3.select("#state");
    var inputElement_country = d3.select("#country");
    var inputElement_shape = d3.select("#shape");

    // Get the value property of the input element
    var inputValue_date = inputElement_date.property("value");
    var inputValue_city = inputElement_city.property("value");
    var inputValue_state = inputElement_state.property("value");
    var inputValue_country = inputElement_country.property("value");
    var inputValue_shape = inputElement_shape.property("value");

    // Set input value with default if there is no input value
    // date
    if (inputValue_date === ''){
        filteredData = tableData;
    } else {
        var filteredData = tableData.filter(tableData => tableData.datetime === inputValue_date);
    }

    //city
    if (inputValue_city === ''){
        filteredData = filteredData;
    } else {
        var filteredData = filteredData.filter(tableData => tableData.city === inputValue_city);
    }

    //state
    if (inputValue_state === ''){
        filteredData = filteredData;
    } else {
        var filteredData = filteredData.filter(tableData => tableData.state === inputValue_state);
    }

    //country
    if (inputValue_country === ''){
        filteredData = filteredData;
    } else {
        var filteredData = filteredData.filter(tableData => tableData.country === inputValue_country);
    }

    //shape
    if (inputValue_shape === ''){
        filteredData = filteredData;
    } else {
        var filteredData = filteredData.filter(tableData => tableData.shape === inputValue_shape);
    }



    if (filteredData.length === 0 ){
        console.log('No Data');
    }
    else {
        console.log("filtered data start");
        filteredData.forEach(function(UFOReport) {
            
            var row = tbody.append("tr");
            Object.entries(UFOReport).forEach(([key, value]) => {
                var cell = tbody.append("td");
                cell.text(value);
            });
        });
    }

});


