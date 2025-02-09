-- Visualizzare l'elenco dei NOMI degli AEROPORTI di PARTENZA che NON SONO MAI AEROPORTI di ARRIVO
SELECT DISTINCT a.name, departure 
FROM flights 
JOIN airports a
ON departure = a.code
WHERE departure NOT IN (SELECT DISTINCT arrival from flights)

-- Visualizzare gli ID, il NOME e il NUMERO totale di VOLI delle COMPAGNIE AEREE che gestiscono PIÙ DI 2 VOLI
SELECT a.airline_id, a.name, COUNT(f.flight_id) AS voli_totali
FROM airlines a
INNER JOIN flights f
ON a.airline_id = f.airline_id
GROUP BY a.airline_id, a.name
HAVING COUNT(f.flight_id) > 2
ORDER BY voli_totali ASC

-- Visualizzare gli ID, il NOME e il NUMERO totale di VOLI delle COMPAGNIE AEREE che gestiscono MENO DI 2 VOLI
SELECT a.airline_id, a.name, COUNT(f.flight_id) AS voli_totali
FROM airlines a
INNER JOIN flights f
ON a.airline_id = f.airline_id
GROUP BY a.airline_id, a.name
HAVING COUNT(f.flight_id) < 2
ORDER BY voli_totali ASC