# open-ssh linux server creation and tunneling through cloudflare quick free tunnel
	- Currently only supports quick free tunnels from cloudflare
	- sshd_config parameters can be changed as required
	- run `make build-whl pip-install` to build and install the package
	- run `make launch_server` on linux server to start the server tunnel
	- connect to the tunneled server from either windows or linux ssh client through the domain assigned

Dependencies on server side: python>=3.8, pip, python-apt, make

##pip installation
```
pip install CFsshTunnel==0.2
```

Using it directly from python notebook/script
```
import CFsshTunnel

#Run either with all default parameters or update as needed
CFsshTunnel.cloud_ssh_tunnel()	
```
##Uninstallation
```
pip uninstall CFsshTunnel
```

execute as root/sudo user since python-apt, /etc/ssh/sshd_config and ~/.ssh/config require that access
In case of runtime error due to failure to acquire cloudflare tunnel, just restart the server, should work in a try or two
ssh Port designation is set to random between `49153 to 65534` unless specified
cloudflare logging should be available as ./cloudflared.log
cloudflare metrics will be on ssh://localhost:ssh_port+1

Successful server tunneling will give a similar terminal output with details for client config and connection
![image](https://user-images.githubusercontent.com/19603746/148923523-39d9f492-388d-4251-8b88-c3247ff809eb.png)



