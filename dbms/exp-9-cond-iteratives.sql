DECLARE x number := 10;
BEGIN
LOOP
dbms_output.put_line(x);
x := x + 10;
IF x > 50 THEN
exit;
END IF;
END LOOP;
-- after exit, control resumes here
dbms_output.put_line('After Exit x is: ' || x);
END;

DECLARE x number := 10;
BEGIN
LOOP
dbms_output.put_line(x);
x := x + 10;
Exit WHEN x > 50;
END LOOP;
-- after exit, control resumes here
dbms_output.put_line('After Exit x is: ' || x);
END;

DECLARE a number(2) := 10;
BEGIN
WHILE a < 20 LOOP
dbms_output.put_line('value of a: ' || a);
a := a + 1;
END LOOP;
END;

DECLARE a number(2);
BEGIN
FOR a in 10 .. 20 LOOP
dbms_output.put_line('value of a: ' || a);
END LOOP;
END;

DECLARE i number(3);
j number(3);
BEGIN
i := 2;
LOOP
j:= 2;
LOOP
exit WHEN ((mod(i, j) = 0) or (j = i));
j := j +1;
END LOOP;
IF (j = i ) THEN dbms_output.put_line(i || ' is prime');
END IF; i := i + 1;
exit WHEN i = 50;
END LOOP;
END;

