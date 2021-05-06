-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/Iq5Mp2
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE AIDB (
    Country VARCHAR(255)   NOT NULL,
    City VARCHAR(255)   NOT NULL,
    Name VARCHAR(255)   NOT NULL,
    Cat VARCHAR(255)   NOT NULL,
    Website VARCHAR(255)   NOT NULL,
    CONSTRAINT pk_AIDB PRIMARY KEY (
        Country
     )
);

CREATE TABLE AI_Companies_Deals (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_AI_Companies_Deals PRIMARY KEY (
        Country
     )
);

CREATE TABLE AICD_Company (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_AICD_Company PRIMARY KEY (
        Company_Count
     )
);


CREATE TABLE AICD_Deals (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_AICD_Deals PRIMARY KEY (
        Deal_Count
     )
);

CREATE TABLE AICD_Capital (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_AICD_Capital PRIMARY KEY (
        Capital_Invested
     )
);

CREATE TABLE AICD_Revenue (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_AICD_Revenue PRIMARY KEY (
        Revenue
     )
);

CREATE TABLE Tech_Companies_Deals (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_Tech_Companies_Deals PRIMARY KEY (
        Country
     )
);

CREATE TABLE TCD_Company (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_TCD_Company PRIMARY KEY (
        Company_Count
     )
);


CREATE TABLE TCD_Deals (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_TCD_Deals PRIMARY KEY (
        Deal_Count
     )
);



CREATE TABLE TCD_Capital (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_TCD_Capital PRIMARY KEY (
        Capital_Invested
     )
);

CREATE TABLE TCD_Revenue (
    Country VARCHAR(255)   NOT NULL,
    Company_Count INT   NOT NULL,
    Deal_Count INT   NOT NULL,
    Capital_Invested INT   NOT NULL,
    Revenue INT   NOT NULL,
    CONSTRAINT pk_TCD_Revenue PRIMARY KEY (
        Revenue
     )
);


