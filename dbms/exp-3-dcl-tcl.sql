create user admin1 identified by password1;
grant create session to admin1;
grant connect to admin1;

revoke create session from admin1;
revoke connect from admin1;
revoke create table from admin1;

grant connect to admin1,
revoke connect from admin1;
commit;

update movie set movie_genre="Comedy" where 
movie_title="QWERTY-1";
select * from movie;
rollback;

create table al(a_id int, a_serialno int);
insert into a1 values (1,123);
insert into a1 values (2,452);
insert into a1 values (3,526);
insert into a1 values (4,356);
savepoint a1 table;

update a1 set a_serialno=242 where a_id=2;
savepoint al_update;
drop table al;

