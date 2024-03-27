--Lists all the cities of Carlifonia that can be found in the database of hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
