# Oracle
Note: Oracle databases need .sys before table names. EG: `sys.users` or `sys.passwords`

Show the db version
`select * from v$version;`

Show the db user
`SELECT * FROM user_users;`
`SELECT * FROM all_users ORDER BY created;`

Show available databases - does it by searching through the different user's access
`select owner from all_tables group by owner;`

Show available tables in a database
`SELECT owner, TABLENAME FROM all_tables;`

Show values in a specific table
`select * from TABLENAME;`
# MySQL
Select the DB version
`select version();`

Select the DB user
`select current_user();`

Show available databases
`select table_schema from information_schema.tables group by table_schema; show databases;`

Show available tables in a database
`select table_name from information_schema.tables where table_schema = 'DATABASENAME';`

Show columns in a specific table
`select column_name, data_type from information_schema.columns where table_schema = 'DATABASENAME' and table_name = 'TABLENAME';`

Useful command for causing errors
`extractvalue('',concat('>',version()))`

# MSSQL
Note: `sa` is the default admin account

Show the db version
`select @@version;`

Show the db user
`SELECT SYSTEM_USER;`

Show available databases
`SELECT name FROM sys.databases;`

Show available tables in a database
`select * from DATABASENAME.information_schema.tables;`

Show values in a specific table
`select COLUMN_NAME, DATA_TYPE from DATABASENAME.information_schema.columns where TABLE_NAME = 'TABLENAME';`

Select database values
`select * from DATABASENAME.dbo.TABLENAME`

Useful command for causing errors
`cast(@@version as integer)`

# PostgreSQL
Show the db version
`select version();`

Show the db user
`select current_user;`

Show available databases
`select datname from pg_database;`

Show available tables in a database
`select table_name from DATABASENAME.information_schema.tables where table_schema = 'public';`

Show values in a specific table
`select * from TABLENAME;`