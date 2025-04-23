wget -O- "https://desktop.docker.com/win/main/amd64/187762/Docker%20Desktop%20Installer.exe"
"Docker Desktop Installer.exe" install
Start-Process 'Docker Desktop Installer.exe' -Wait -ArgumentList 'install', '--accept-license'

#If your admin account is different to your user account, you must add the user to the docker-users group:

net localgroup docker-users <user> /add
