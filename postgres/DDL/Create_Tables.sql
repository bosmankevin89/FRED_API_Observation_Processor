CREATE SCHEMA "FRED_OBSERVATIONS" AUTHORIZATION postgres;


CREATE TABLE "FRED_OBSERVATIONS".real_gross_domestic_product (
	series_id varchar(50) NOT NULL,
	realtime_start date NOT NULL,
	realtime_end date NOT NULL,
	observation_date date NOT NULL,
	observation_value numeric(10,3) NULL,
	CONSTRAINT pk_obsrv_rgdp PRIMARY KEY (series_id, realtime_end, observation_date)
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE "FRED_OBSERVATIONS".university_of_michigan_consumer_sentiment_index (
	series_id varchar(50) NOT NULL,
	realtime_start date NOT NULL,
	realtime_end date NOT NULL,
	observation_date date NOT NULL,
	observation_value numeric(10,3) NULL,
	CONSTRAINT pk_obsrv_umcsi PRIMARY KEY (series_id, realtime_end, observation_date)
)
WITH (
	OIDS=FALSE
) ;


CREATE TABLE "FRED_OBSERVATIONS".us_civilian_unemployment_rate (
	series_id varchar(50) NOT NULL,
	realtime_start date NOT NULL,
	realtime_end date NOT NULL,
	observation_date date NOT NULL,
	observation_value numeric(10,3) NULL,
	CONSTRAINT pk_obsrv_uscur PRIMARY KEY (series_id, realtime_end, observation_date)
)
WITH (
	OIDS=FALSE
) ;
