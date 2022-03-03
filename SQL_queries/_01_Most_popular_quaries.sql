--# first highest salary
select id, name, max(salary) from emp;

--# seconds highest salary
select id, name, max(salary) from emp where salary not in (select max(salary) from emp);

--// for any nth highest salary from emp;;;; //

select id, name, salary from emp e1 where n -1=(select count(distinct salary) from emp e2 where e2.salary > e1.salary);

--# example 4th highest salary

select id, name, salary from emp e1 where 4-1 = (select count(distinct salary) from emp e2 where e2.salary > e1.salary);

-- # To find the Duplicate record in table
select * from emp out where (select count(*) from emp inr where inr.emp_id = out.emp_id) > 1

--# get the employee who salary is greater than the his manager salary

select id, name, salary from emp e, emp m where e.manager_id = m.emp_id and e.salary > m.salary;

--# list out the workers in a deportment in decreasing order from

select deportment, count(workers_id) no_of_workers from workers group by deportment order by no_of_workers DESC;

--# difference between the UNION and UNION ALL

--union--> will remove any duplicates from date table
--union all --> will not remove any duplicates from date table

drop table hotel;
create table hotel(ssn int not null, cname text not null, address text null,
             start_date date not null, end_date date null,room_type char(9) null);



insert into hotel values(12,'Naveen','kurnool','01-02-2019','01-03-2019','A/c');
insert into hotel values(13,'Sai','kurnool','01-02-2019','31-12-2019','Normal');
insert into hotel values(14,'Ram','Tirupati','01-02-2019','01-03-2020','A/c');
insert into hotel values(12,'Sam','Hyderabad','01-04-2019');
insert into hotel values(12,'John','Bangalore','01-05-2019');

select * from hotel;
select count(end_date-start_date) from hotel;

update hotel set end_date = '2020-05-13' where end_date is null;

select sum(extract(year from age(end_date,start_date))) years,
sum(extract(month from age(end_date,start_date))) months,
sum(extract(day from age(end_date,start_date))) days from hotel;


select sum(extract(year from age(end_date,start_date)))*1200000 amount_years,
sum(extract(month from age(end_date,start_date)))*100000 amount_months,
sum(extract(day from age(end_date,start_date)))*3300 amount_days from hotel;

select (sum(extract(year from age(end_date,start_date)))*1200000 +
sum(extract(month from age(end_date,start_date)))*100000 +
sum(extract(day from age(end_date,start_date)))*3300) total_amount from hotel;

################################################################################################################
create schema postgres_prac;
set search_path to postgres_prac;

CREATE TABLE dept (
    deptno          int NOT NULL CONSTRAINT dept_pk PRIMARY KEY,
    dname           VARCHAR(14) CONSTRAINT dept_dname_uq UNIQUE,
    loc             VARCHAR(13));


CREATE TABLE emp (
    empno           int NOT NULL CONSTRAINT emp_pk PRIMARY KEY,
    ename           VARCHAR(10),
    job             VARCHAR(9),
    mgr            int,
    hiredate        DATE,
    sal             decimal(7,2) CONSTRAINT emp_sal_ck CHECK (sal > 0),
    comm            decimal(7,2),
    deptno          int CONSTRAINT emp_ref_dept_fk
                        REFERENCES dept(deptno)
);

INSERT INTO dept VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO dept VALUES (20,'RESEARCH','DALLAS');
INSERT INTO dept VALUES (30,'SALES','CHICAGO');
INSERT INTO dept VALUES (40,'OPERATIONS','BOSTON');

select * from dept;

INSERT INTO emp VALUES (7369,'SMITH','CLERK',7902,'17-DEC-80',800,NULL,20);
INSERT INTO emp VALUES (7499,'ALLEN','SALESMAN',7698,'20-FEB-81',1600,300,30);
INSERT INTO emp VALUES (7521,'WARD','SALESMAN',7698,'22-FEB-81',1250,500,30);
INSERT INTO emp VALUES (7566,'JONES','MANAGER',7839,'02-APR-81',2975,NULL,20);
INSERT INTO emp VALUES (7654,'MARTIN','SALESMAN',7698,'28-SEP-81',1250,1400,30);
INSERT INTO emp VALUES (7698,'BLAKE','MANAGER',7839,'01-MAY-81',2850,NULL,30);
INSERT INTO emp VALUES (7782,'CLARK','MANAGER',7839,'09-JUN-81',2450,NULL,10);
INSERT INTO emp VALUES (7788,'SCOTT','ANALYST',7566,'19-APR-87',3000,NULL,20);
INSERT INTO emp VALUES (7839,'KING','PRESIDENT',NULL,'17-NOV-81',5000,NULL,10);
INSERT INTO emp VALUES (7844,'TURNER','SALESMAN',7698,'08-SEP-81',1500,0,30);
INSERT INTO emp VALUES (7876,'ADAMS','CLERK',7788,'23-MAY-87',1100,NULL,20);
INSERT INTO emp VALUES (7900,'JAMES','CLERK',7698,'03-DEC-81',950,NULL,30);
INSERT INTO emp VALUES (7902,'FORD','ANALYST',7566,'03-DEC-81',3000,NULL,20);
INSERT INTO emp VALUES (7934,'MILLER','CLERK',7782,'23-JAN-82',1300,NULL,10);

select sum(sal) from emp;

select empno,ename,max(sal) from emp group by empno;

select empno,ename,sal from emp e1 where 0 = (select count(distinct sal) from emp e2 where
											 e2.sal > e1.sal);
select e.empno, e.ename, e.sal, m.mgr, m.ename mgr_name, m.sal mgr_sal from emp e,emp m where e.mgr = m.empno
and e.sal > m.sal;

select e.deptno, count(e.empno) no_of_employee from emp e group by e.deptno
order by no_of_employee DESC;


CREATE TABLE PLAYER (
ID INT,  
FIRST VARCHAR(25),
YEAR INT  
);

INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (1, "Santo", 1977);
INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (2, "Santo", 1978);
INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (3, "Santo", 1979);
INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (4, "Santo", 1980);
INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (5, "Santo", 1993);
INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (6, "Santo", 1994);
INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (7, "Santo", 1994);


INSERT INTO PLAYER (ID, FIRST, YEAR) VALUES (12, "sa", 1992);

SELECT * FROM PLAYER 

select DISTINCT(FIRST) from player where FIRST 
IN (select p1.first from player p1 
inner join player p2 on p1.year = p2.year+1 
inner join player p3 on p2.year = p3.year+1 and p1.first = p2.first and p2.first=p3.first);


