-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/Iq5Mp2
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


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
CREATE TABLE AIDB (
    Country VARCHAR(255)   NOT NULL,
    City VARCHAR(255)   NOT NULL,
    Company_Name VARCHAR(255)   NOT NULL,
    Category VARCHAR(255)   NOT NULL,
    Website VARCHAR(255)   NOT NULL,
    CONSTRAINT pk_AIDB PRIMARY KEY (
        Category
     )
);

ALTER TABLE AIDB ADD CONSTRAINT fk_AIDB_Country FOREIGN KEY(Country)
REFERENCES Tech_Companies_Deals (Country);

