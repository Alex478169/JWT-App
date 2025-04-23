#At the end of the installation process, apt displays an error due to installing a downloaded package.
#You can ignore this error message.
#N: Download is performed unsandboxed as root, as file '/home/user/Downloads/docker-desktop.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)
#install docker engine
#add docker's official GPG key:
	sudo apt-get update;
        sudo dpkg --configure -a
	sudo apt-get install ca-certificates;

	sudo install -m 0755 -d /ect/apt/keyrings
	sudo curl -k -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
	sudo chmod a+r /etc/apt/keyrings/docker.asc;


#add the repository to Apt sources
	echo \
  	  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  	  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  	  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	  sudo apt-get update;


#Install the docker packages
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin;

#verify that the installation is successful by running the hello-world image
	if which docker > /dev/null; then
  	   sudo docker run hello-world;
	fi

curl -k -o docker-desktop.deb "https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb?utm_source=docker&utm_med>"

sudo apt-get update && sudo apt-get install ./docker-desktop.deb

systemctl --user start docker-desktop;

docker compose version;
docker --version;
docker version;


#To enable Docker Desktop to start on sign in, from the Docker menu, select Settings > General > Start Docker Desktop when you sign in to your computer.

#Alternatively, open a terminal and run:


 systemctl --user enable docker-desktop;
