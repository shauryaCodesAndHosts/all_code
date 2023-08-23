/*A cursor is a pointer to this context area. PL/SQL controls the context area through a cursor. A
cursor holds the rows (one or more) returned by a SQL statement. The set of rows the cursor
holds is referred to as the active set.
There are two types of cursors −
➢ Implicit cursors
➢ Explicit cursors
1. Declaring the Cursor
Declaring the cursor defines the cursor with a name and the associated SELECT
statement.
For example −
CURSOR c_customers IS SELECT id, name, address FROM customers;
2. Opening the Cursor
Opening the cursor allocates the memory for the cursor and makes it ready for
fetching the rows returned by the SQL statement into it. For example, we will
open the above defined cursor as follows −
OPEN c_customers;
3. Fetching the Cursor
Fetching the cursor involves accessing one row at a time. For example, we will
fetch rows from the above-opened cursor as follows −
FETCH c_customers INTO c_id, c_name, c_addr;
4. Closing the Cursor
Closing the cursor means releasing the allocated memory. For example, we will close the
above-opened cursor as follows −
CLOSE c_customers;
*/

DECLARE
total_rows number(2);
BEGIN
UPDATE customers
SET salary = salary + 500;
IF sql%notfound THEN
dbms_output.put_line('no customers selected');
ELSIF sql%found THEN
total_rows := sql%rowcount;
dbms_output.put_line( total_rows || ' customers selected ');
END IF;
END;

DECLARE
c_id customers.id%type;
c_name customers.name%type;
c_addr customers.address%type;
CURSOR c_customers is
SELECT id, name, address FROM customers;
BEGIN
OPEN c_customers;
LOOP
FETCH c_customers into c_id, c_name, c_addr;
EXIT WHEN c_customers%notfound;
dbms_output.put_line(c_id || ' ' || c_name || ' ' || c_addr);
END LOOP;
CLOSE c_customers;
END;

