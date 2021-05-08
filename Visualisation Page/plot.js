// 1. Create fileter
function filterData1(Country ) {
    return parseInt(Country .Company_Count) > 100;
  }
  
  // 2. Use filter() to pass the function as its argument
  var filteredData1 = AIDeal.filter(filterData1);
  
  //  Check to make sure 
  // console.log(filteredData1);
  
  // 3. Use the map method with the arrow function to return all the filtered data
  var Countries = filteredData1.map(Country => Country.Country);
  
  //  Check 
  // console.log(Countries);
  
  // 4. Use the map method with the arrow function to return all the filtered data
  var Deal_Count = filteredData1.map(Country => Country.Deal_Count);
  
  //  Check 
  // console.log(Deal_Count);
  
  // 5. Create  trace.
  var trace1 = {
    x: Countries,
    y: Deal_Count,
    type: "bar",
    name: "AI Deals"
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

/////////////////////////////////////////////////////////////

// ////////////////////////////////////////////////////////////

  function filterCities2(Country) {
    return parseInt(Country .Revenue) > 1000;
  }
  
  // 2. Use filter() to pass the function as its argument
  var filteredCities2 = AIDeal.filter(filterCities2);
  
  // 3. Use the map method with the arrow function to return all the filtered data
  var Countries = filteredCities2.map(Country => Country.Country);
 
  // 4. Use the map method with the arrow function to return all the filtered data
  var Revenue = filteredCities2.map(Country => Country.Revenue);
  
  // 5. Create your trace.
  var trace2 = {
    x: Countries,
    y: Revenue,
    type: "bar",
    name: "Revenue AI Companies"
  };
  
  // 6. Create the data array for our plot
  var data2 = [trace2];
  
  // 7. Define our plot layout
  var layout = {
    title: "Countries with more than 1000M Revenue",
    xaxis: { title: "Countries" },
    yaxis: { title: "Revenue " }
  };
  
  // 8. Plot the chart to a div tag with id "bar-plot"
  Plotly.newPlot("rev-bar-plot", data2, layout);

//////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////

  // Create the Comparison data array for our plot
  var data3 = [trace1, trace2];
  
  //  Define our plot layout
  var layout = {
    title: "Comparison of Rev and Deal Count",
    xaxis: { title: "Countries" },
    yaxis: { title: "Revenue and Deals" }
  };
  
  // Plot the chart to a div tag with id "bar-plot"
  Plotly.newPlot("Comp-bar-plot", data3, layout);


  /////////////////////////////////////////////////////////////

// ////////////////////////////////////////////////////////////


// 1. Create fileter
function filterData11(Country ) {
  return parseInt(Country .Company_Count) > 4000;
}

// 2. Use filter() to pass the function as its argument
var filteredData11 = TDeal.filter(filterData11);

//  Check to make sure 
// console.log(filteredData1);

// 3. Use the map method with the arrow function to return all the filtered data
var Countries = filteredData11.map(Country => Country.Country);

//  Check 
// console.log(Countries);

// 4. Use the map method with the arrow function to return all the filtered data
var Deal_Count = filteredData11.map(Country => Country.Deal_Count);

//  Check 
// console.log(Deal_Count);

// 5. Create  trace.
var trace11 = {
  x: Countries,
  y: Deal_Count,
  type: "bar",
  name: "Tech Deals"
};

// 6. Create the data array for our plot
var data11 = [trace11];

// 7. Define our plot layout
var layout = {
  title: "Contries with more than 4000 Tech companies",
  xaxis: { title: "Countries" },
  yaxis: { title: "Tech Deal Count"}
};

// 8. Plot the chart to a div tag with id "bar-plot"
Plotly.newPlot("Tbar-plot", data11, layout);

/////////////////////////////////////////////////////////////

// ////////////////////////////////////////////////////////////

function filterCities22(Country) {
  return parseInt(Country .Revenue) > 40000;
}

// 2. Use filter() to pass the function as its argument
var filteredCities22 = TDeal.filter(filterCities22);

// 3. Use the map method with the arrow function to return all the filtered data
var Countries = filteredCities22.map(Country => Country.Country);

// 4. Use the map method with the arrow function to return all the filtered data
var Revenue = filteredCities22.map(Country => Country.Revenue);

// 5. Create your trace.
var trace22 = {
  x: Countries,
  y: Revenue,
  type: "bar",
  name: "Revenue Tech Companies"
};

// 6. Create the data array for our plot
var data22 = [trace22];

// 7. Define our plot layout
var layout = { 
  title: "Countries with more than 4000M Revenue",
  xaxis: { title: "Countries" },
  yaxis: { title: "Revenue " }
};

// 8. Plot the chart to a div tag with id "bar-plot"
//Plotly.newPlot("Trev-bar-plot", data22, layout);

//////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////

// Create the Comparison data array for our plot
var data33 = [trace11, trace1];

//  Define our plot layout
var layout = {
  title: "Comparison Deal Count ",
  xaxis: { title: "Countries" },
  yaxis: { title: "No of Deals" }
};

// Plot the chart to a div tag with id "bar-plot"
Plotly.newPlot("TComp-bar-plot", data33, layout);


/////////////////////////////////////////////////////////////

// ////////////////////////////////////////////////////////////


// Create the Comparison data array for our plot
var data44 = [trace22, trace2];

//  Define our plot layout
var layout = {
  title: "Comparison of Revenue",
  xaxis: { title: "Countries" },
  yaxis: { title: "Revenue" }
};

// Plot the chart to a div tag with id "bar-plot"
Plotly.newPlot("TComp2-bar-plot", data44, layout);


/////////////////////////////////////////////////////////////

// ////////////////////////////////////////////////////////////