--  script that lists all bands with Glam rock as their main
SELECT
    band_name,
    (formed - split) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
