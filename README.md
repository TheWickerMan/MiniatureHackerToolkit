# MiniatureSecurityToolkit

**SecuHed**:  *Usage: [-h], [-t]*

Identifies missing security headers from a list of URL's and outputs a table to a CSV file.
Note:
  - CSV delimiter is ","


**BasicAuthCredGen.py**:  *Usage: [-h], [-u], [-uf], [-p], [-pf], [-o], [-s]*


Generates a list of Basic Auth credentials from a list of usernames and passwords for convenient brute-forcing.

**E-Manipulator.py**:  *Usage: [-h], [-i], [-o], [-Generate], [-Filter], [-s]*


*[-Generate]* Allows the generation of email addresses from a list of names.


*[-Filter]* Allows the filtration of email addresses by domain from a list. (Useful for sorting through email dumps)

**PwnedCheck.py**:  *Usage: [-h], [-email], [-file], [-output], [-delay]*


Checks email addresses against HaveIBeenPwned (https://haveibeenpwned.com) using its API and retrieves information pertaining to any data breaches the email addresses feature in.

**Iterator.py**:  *Usage: [-i], [-n]*

Iteratively generates a list up upper/lower string combinations from a provided list.  Useful for stuff, EG: File extensions for file upload validation, etc.

**Web-POC**

Contains various concepts for web-based attacks.
 - CORS.html - Tests for misconfigured Cross-Origin Resource Sharing functionality.
