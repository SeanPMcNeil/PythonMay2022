# This is to select something in the schema
# SELECT * FROM users;

# This is to create a new row in the schema
# NOW() inserts the time that the query is run
# INSERT INTO users (first_name, last_name, handle, birthday, created_at)
# VALUES ('Kevin', 'Garnett', 'trashTalk77', '1956-08-25', NOW());

# This is to update a row in the schema
#UPDATE users SET first_name = 'Chauncy', last_name = 'Billups', updated_at = NOW() WHERE id = 5;

# UPDATE users SET handle = 'denverDynamite', updated_at = NOW() WHERE id = 5;

# This is to delete a row from the schema
# DELETE FROM users WHERE id = 6;
# Need to make sure the schema settings are set to CASCADE to change when data interacts with other tables
# DELETE FROM users WHERE id = 3;
SELECT * FROM users;