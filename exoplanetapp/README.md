This folder is the flask app version of the command line tool
It shows the output on the server port 5000

use virtual env
python3 -m pip install --user virtualenv
python3 -m venv env

Docker:
use the Dockerfile to spin up a process with the app
Docker image located on repo -- docker pull maddoc81/exoplanet-app


Kubernetes deployment steps:
--install kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl

--make the binary downloaded executable
chmod +x ./kubectl

--move the binary to path
sudo mv ./kubectl /usr/local/bin/kubectl

--test version
kubectl version --client


Deploy app-
kubectl create -f exoplanetapp.deployment.yml $ kubectl create -f exoplanetapp.service.yml
