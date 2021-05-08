# Project-2-AI-Market

<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>AI Market Analysis and Database Search</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/superhero/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
  <link rel="stylesheet" href="static/css/style.css">
</head>

<body>
  <div class="wrapper">
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <!-- <a class="navbar-brand" href="index.html"> -->
            <img loading="lazy" class="wp-image-1422 avia_image" src="static/images/AI.jpeg"   height="400" width="1400" itemprop="thumbnailUrl">
          </a>
        </div>
      </div>
    </nav>
    <div class="hero text-center">
      <h1>AI Market Analysis </h1>
      <p>AI Companies and market trend</p>
    </div>
    <div class="container">
      <div class="row margin-top-50">
        <div class="col-md-12">
          <aside class="filters">
            <div class="panel panel-default">
              <div class="panel-heading">Search AI Database</div>
              <div class="panel-body">
                <div class="form-group">
                  <ul class="list-group" id="filters">
                    <li class="filter list-group-item">
                      <label for="date">Enter Country name</label>
                      <input class="form-control" id="Country" type="text" placeholder="Australia">
                    </li>
                    <li class="filter list-group-item">
                      <label for="city">Enter a City name</label>
                      <input class="form-control" id="City" type="text" placeholder="Sydney">
                    </li>
                    <li class="filter list-group-item">
                      <label for="state">Enter Company Name</label>
                      <input class="form-control" id="Name" type="text" placeholder="3DLOOK">
                    </li>
                    <li class="filter list-group-item">
                      <label for="country">Enter a Catergory</label>
                      <input class="form-control" id="Category" type="text" placeholder="Core AI Automation Fintech">
                    </li>
                    <li class="filter list-group-item">
                      <label for="shape">Enter a website</label>
                      <input class="form-control" id="Website" type="text" placeholder="https://www.hummingbird.ai/">
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </aside>
        </div>
        <div class="col-md-8">
          <div id="table-area" class="">
            <h1 class="text-center loader" id="loader">AI Companies Database</h1>
            <table id="ufo-table" class="table table-striped">
              <thead>
                <tr>
                  <th class="table-head">Country</th>
                  <th class="table-head">City</th>
                  <th class="table-head">Company</th>
                  <th class="table-head">Category</th>
                  <th class="table-head">Website</th>
                </tr>
              </thead>
              <tbody></tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <footer class="footer">
      <span class="bottom">Project 2</span>
    </footer>
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.11.0/d3.js"></script>
  <script src="static/js/data.js"></script>
  <script src="static/js/app.js"></script>
</body>
</html>

AI Market Analysis

Abstract: 
Artificial Intelligence market is developing rapidly in tec industry. Its market share is increasing since 2001. The prospects are very promising with role of AI increasing in every field of business and technology. In this project a dataset has been explore the database of existing AI companies and AI market comparison is also done within tech industry. A website with database search option is created and some visualization of comparison is also attempted.

Data Source: https://data.world/henritechcity/ai-world-mapping

Scope: 2008 to 2018

Project Requirement Fulfilled:
1.    Python, Flask-API, HTML, CSS, JavaScript, Postgres
2.    Plotly
3.    – tried but not successful
4.    DataSet of 3500+ record
5.    User Interaction -> User Input to search data
6.    Visualizations using bar plots of comparison of data

Database Used: Postgres

File Formats: csv, jpynb, py, Jason, Js, html

Methodology:
Dataset was searched from multiple sources and finally decided to use data set from data.world. The reliable data source and not too old data is rational of choosing this dataset. This dataset compares the market analysis of Artificial Intelligence Industry and technical industry. It also provides a timeline % growth overview of last two decades. Database of existing companies in world till 2018 is also given separately. 

Data was downloaded from data.world website in form of excel files. These files were converted into csv files to be used by Python notebook, where relevant columns were extracted and data transformation was completed by cleaning the dataframes. Using QuickDBD Schema was developed and used to created tables in Postgress. These tables were populated with data by creating engine connection to Postgres and pushing data into tables through notebook. Total 11 tables were created in database.
Next step was to read required data from database and convert it into JSON format (key value pairs). Flask API was created to deliver JSON to d3.jason call but this process was not entirely successful.
On frontend a web page was created along with JavaScript and Json data files and d3 plotly function was used to create simple but comparable bar graphs. Another web page was also developed which showcased the AI companies database in tabular form with option of user input to search data based on different criteria.

Limitations:
Some errors in data were found and need further investigation. 
Detail visualization for comparison was postponed due to time limitations.



Project 2 of DS bootcamp

AI - World Mapping - dataset by henritechcity
henritechcity is using data.world to share AI - World Mapping data with the world

DATASET BY HENRI EGLE SOROTOS
https://data.world/henritechcity/ai-world-mapping


Literature Review Ref:

Literature Review

1. Defination: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-825-techniques-in-artificial-intelligence-sma-5504-fall-2002/lecture-notes/Lecture1Final.pdf
2. Asgard, global AI audit - https://asgard.vc/global-ai/
3. PwC global AI audit - https://www.pwc.com/gx/en/issues/analytics/assets/pwc-ai-analysis-sizing-the-prize-report.pdf
4. McKinsey China AI audit with landscape mapping - https://www.mckinsey.com/~/media/McKinsey/Featured Insights/China/Artificial intelligence Implications for China/MGI-Artificial-intelligence-implications-for-China.ashx

Refernce: https://data.world/henritechcity/ai-world-mapping


