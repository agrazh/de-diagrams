# PostgreSQL cheat sheet

Describe table:

```sql
select column_name, data_type, character_maximum_length, column_default, is_nullable
from INFORMATION_SCHEMA.COLUMNS
where table_name = '<name of table>';
```

or psql: `=# \d+ tablename`

## Window functions
Some aggregate functions such as `AVG()`, `MIN()`, `MAX()`, `SUM()` and `COUNT()` can be also used as window functions

```sql
select product, category,
  avg(price) over (partition by category)
from products
```

<br/>

`ROW_NUMBER()` assigns a sequential number to each row in each partition

`RANK()` assigns ranking within an ordered partition. If rows have the same values, function assigns the same rank, with the next ranking(s) skipped

`DENSE_RANK()` assigns a rank to each row within an ordered partition, but the ranks have no gap. the same ranks are assigned to multiple rows and no ranks are skipped

```sql
select product, category, price,
  dense_rank() over (
    partition by p.category,
    order by p.price
  ) 
from products as p
```

<br/>

`FIRST_VALUE(col)` returns a value evaluated against the first row in partition

`LAST_VALUE(col)` returns a value evaluated against the last row in partition

```sql
(tbd)
```

<br/>

`LAG(col [,offset] [,default])` access data from the one of the previous rows

`LEAD(col [,offset] [,default])` access data from one of the next rows
```sql
(tbd)
```

<br/>

`CUME_DIST()` returns the relative rank (`0 < rank ≤ 1`) of the current row. Calculates the cumulative distribution of a value within a set of values. Returns the relative position of a value in a set of values (`0 < CUME_DIST() <= 1`) - percentile for each value (e.g. find that 80% of sales employees have sales less than or equal to 150K in 2018)

<br/>

`PERCENT_RANK()` returns the percent of values less than the current value (`0 ≤ pr < 1`). Similar `CUME_DIST()` which returns the actual position of the value (`0 < pr ≤ 1`)

<br/>

`NTILE(n)` divides partitions into n buckets of equal size and assigns each row the corresponding bucket number starting from 1

<br/>

`NTH_VALUE()` returns a value from the n-th row in an ordered partition of a result set.

<br/>

## Tiny datasets for testing

<details>
<summary>Products</summary>

```sql
CREATE TABLE product_groups (
	group_id serial PRIMARY KEY,
	group_name VARCHAR (255) NOT NULL
);

CREATE TABLE products (
	product_id serial PRIMARY KEY,
	product_name VARCHAR (255) NOT NULL,
	price DECIMAL (11, 2),
	group_id INT NOT NULL,
	FOREIGN KEY (group_id) REFERENCES product_groups (group_id)
);
```

```sql
INSERT INTO product_groups (group_name)
VALUES
	('Smartphone'),
	('Laptop'),
	('Tablet');

INSERT INTO products (product_name, group_id,price)
VALUES
	('Microsoft Lumia', 1, 200),
	('HTC One', 1, 400),
	('Nexus', 1, 500),
	('iPhone', 1, 900),
	('HP Elite', 2, 1200),
	('Lenovo Thinkpad', 2, 700),
	('Sony VAIO', 2, 700),
	('Dell Vostro', 2, 800),
	('iPad', 3, 700),
	('Kindle Fire', 3, 150),
	('Samsung Galaxy Tab', 3, 200);
```

</details>




## References

:link: psql meta-commands ([postgresql.org](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS))

:link: System catalogs ([postgresql.org](https://www.postgresql.org/docs/current/catalogs.html))

:link: Window functions ([postgresql.org](https://www.postgresql.org/docs/current/tutorial-window.html))
