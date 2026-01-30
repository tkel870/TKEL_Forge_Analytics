-- Question 1: Unaccompanied Homeless Youth (2018)

SELECT
  CoC_Name,
  SUM(Homeless_Unaccompanied_Youth_Under_18) AS total_unaccompanied_youth_under_18_2018
FROM
  `tk-bigquery.homelessness_data.homelessness`
WHERE
  Count_Year = 2018
GROUP BY
  CoC_Name
ORDER BY
  total_unaccompanied_youth_under_18_2018 DESC
LIMIT 3;

-- Question 2: Unsheltered Homeless Trend in Delaware

SELECT
  Count_Year,
  SUM(Unsheltered_Homeless) AS total_unsheltered_homeless
FROM
  `tk-bigquery.homelessness_data.homelessness`
WHERE
  SUBSTR(CoC_Number, 1, 2) = 'DE'
  AND Count_Year >= (
    SELECT MAX(Count_Year) - 6
    FROM `tk-bigquery.homelessness_data.homelessness`
  )
GROUP BY
  Count_Year
ORDER BY
  Count_Year;

-- Question 3a: Safe Haven locations (2018)

SELECT
  COUNT(DISTINCT CoC_Name) AS locations_with_safe_haven_2018
FROM
  `tk-bigquery.homelessness_data.homelessness`
WHERE
  Count_Year = 2018
  AND Sheltered_SH_Homeless >= 1;

-- Question 3b: Top Safe Haven locations

SELECT
  CoC_Name,
  SUM(Sheltered_SH_Homeless) AS total_sheltered_sh
FROM
  `tk-bigquery.homelessness_data.homelessness`
WHERE
  Count_Year = 2018
GROUP BY
  CoC_Name
ORDER BY
  total_sheltered_sh DESC
LIMIT 3;

-- Question 4: Top states by overall homeless population (2018)

SELECT
  SUBSTR(CoC_Number, 1, 2) AS state,
  SUM(Overall_Homeless) AS total_homeless_population
FROM
  `tk-bigquery.homelessness_data.homelessness`
WHERE
  Count_Year = 2018
GROUP BY
  state
ORDER BY
  total_homeless_population DESC
LIMIT 7;

-- Question 6: Effective shelter provision

SELECT
  CoC_Name,
  SUM(Overall_Homeless) AS overall_homeless,
  SUM(Unsheltered_Homeless) AS unsheltered_homeless
FROM
  `tk-bigquery.homelessness_data.homelessness`
WHERE
  Count_Year = 2018
GROUP BY
  CoC_Name
HAVING
  overall_homeless > 1000
  AND unsheltered_homeless < 100
ORDER BY
  overall_homeless DESC;

-- Question 6b: Unsheltered < 2%

WITH totals AS (
  SELECT
    CoC_Name,
    SUM(Overall_Homeless) AS overall_homeless,
    SUM(Unsheltered_Homeless) AS unsheltered_homeless
  FROM
    `tk-bigquery.homelessness_data.homelessness`
  WHERE
    Count_Year = 2018
  GROUP BY
    CoC_Name
)
SELECT
  CoC_Name,
  overall_homeless,
  unsheltered_homeless,
  SAFE_DIVIDE(unsheltered_homeless, overall_homeless) AS unsheltered_pct
FROM
  totals
WHERE
  overall_homeless > 1000
  AND unsheltered_homeless < 100
  AND SAFE_DIVIDE(unsheltered_homeless, overall_homeless) < 0.02
ORDER BY
  unsheltered_pct ASC, overall_homeless DESC;


