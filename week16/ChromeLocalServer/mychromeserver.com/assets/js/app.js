// @TODO: YOUR CODE HERE!


// When you application loads, meaning the browsers loads the index.html file
// this file is called NOTE: this 

// before our application can start we need to get the data from teh csv file 

d3.csv('./assests/data/data.csv').then(data => {
        console.log(data);
}); 