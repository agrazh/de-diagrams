# PostgreSQL cheat sheet

Describe table:

```sql
select column_name, data_type, character_maximum_length, column_default, is_nullable
from INFORMATION_SCHEMA.COLUMNS
where table_name = '<name of table>';
```

or psql: `=# \d+ tablename`

<details>
<summary>Links</summary>

🔗 psql meta-commands ([postgresql.org](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS))

🔗 System catalogs ([postgresql.org](https://www.postgresql.org/docs/current/catalogs.html))

</details>