/*
 * Question: What was the average rate of unemployment for each year starting with 1980 and going up to 2015?
 * 
 * Assumptions/Notes:
 * 
 * 	- The query should return the data from the latest available realtime_end date.  This represents the latest set
 * of data.  The realtime_start and realtime_end dates could be used for ­temporal data queries.
 * 
 *  - Partial year averages have been allowed, but noted by the complete_year field.
 * 
 */


select to_char(extract(year from observation_date), '9999D') as year
	, case when count(*) = 12 then 'Y' else 'N' end as complete_year
	, round((SUM(observation_value) / COUNT(*)), 3) as unemployment_percentage
from "FRED_OBSERVATIONS".us_civilian_unemployment_rate
where 1=1
	-- Filter down the latest data available by default.
	and realtime_end = (
		select max(realtime_end)
		from "FRED_OBSERVATIONS".us_civilian_unemployment_rate
	)
group by to_char(extract(year from observation_date), '9999D')
order by to_char(extract(year from observation_date), '9999D') desc;
