# BREACH Vulnerability indicator


Not 100% foolproof, but a good indicator:

Run:

```openssl s_client -connect TARGET-URL-HERE:PORT-NUMBER-HERE.```

Enter:


```
GET / HTTP/1.1
Host: TARGET-URL-HERE
Accept-Encoding: compress, gzip
 
```

If the response is encoded, that's potentially evidence that it is present.


# JQuery

To quickly display the version of JQuery in use - enter this into the browser inspect-elements console.



```jQuery().jquery```



Alternatively, you can use:



```alert(jQuery.fn.jquery);```
