// @TODO: Complete the Following Steps

// Filter the top 15 cities with a population increase greater than 15,000
//  and then graph each city on the x-axis and the respective population on the y-axis.

// 1. Use the filter method to create a custom filtering function
//  that returns the cities with a population increase greater than 15,000.

function filterCities(Country ) {
    return parseInt(Country .Company_Count) > 100;
  }
  
  // 2. Use filter() to pass the function as its argument
  var filteredCities = top15Cities.filter(filterCities);
  
  //  Check to make sure your filtered your cities.
  console.log(filteredCities);
  
  // 3. Use the map method with the arrow function to return all the filtered cities.
  var Countries = filteredCities.map(Country => Country.Country);
  
  //  Check your filtered cities
  console.log(Countries);
  
  // 4. Use the map method with the arrow function to return all the filtered cities population.
  var Deal_Count = filteredCities.map(Country => Country.Deal_Count);
  
  //  Check the populations of your filtered cities
  console.log(Deal_Count);
  
  // 5. Create your trace.
  var trace1 = {
    x: Countries,
    y: Deal_Count,
    type: "bar"
  };
  
  // 6. Create the data array for our plot
  var data = [trace1];
  
  // 7. Define our plot layout
  var layout = {
    title: "Contries with more than 100 AI companies in 2018",
    xaxis: { title: "Countries" },
    yaxis: { title: "Deal Count in year 2018"}
  };
  
  // 8. Plot the chart to a div tag with id "bar-plot"
  Plotly.newPlot("bar-plot", data, layout);



  function filterCities2(Country ) {
    return parseInt(Country .Revenue) > 1000;
  }
  
  // 2. Use filter() to pass the function as its argument
  var filteredCities2 = top15Cities.filter(filterCities2);
  
  //  Check to make sure your filtered your cities.
  console.log(filteredCities2);
  
  // 3. Use the map method with the arrow function to return all the filtered cities.
  var Countries = filteredCities2.map(Country => Country.Country);
  
  //  Check your filtered cities
  console.log(Countries);
  
  // 4. Use the map method with the arrow function to return all the filtered cities population.
  var Revenue = filteredCities2.map(Country => Country.Revenue);
  
  //  Check the populations of your filtered cities
  console.log(Revenue);
  
  // 5. Create your trace.
  var trace2 = {
    x: Countries,
    y: Revenue,
    type: "bar"
  };
  
  // 6. Create the data array for our plot
  var data2 = [trace2];
  
  // 7. Define our plot layout
  var layout = {
    title: "Contries with Revenue more than 1000M with AI deals in 2018",
    xaxis: { title: "Countries" },
    yaxis: { title: "Revenue in year 2018"}
  };
  
  // 8. Plot the chart to a div tag with id "bar-plot"
  Plotly.newPlot("rev-bar-plot", data2, layout);
  
 