-- order a country by the number of bands
SELECT origin, Sum(fans) nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
