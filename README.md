<include a CircleCI status badge, here>

## Project Overview

In this project, you will apply the skills you have acquired in this course to operationalize a Machine Learning Microservice API.

You are given a pre-trained, `sklearn` model that has been trained to predict housing prices in Boston according to several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and so on. You can read more about the data, which was initially taken from Kaggle, on [the data source site](https://www.kaggle.com/c/boston-housing). This project tests your ability to operationalize a Python flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This project could be extended to any pre-trained machine learning model, such as those for image recognition and data labeling.

### Project Tasks

Your project goal is to operationalize this working, machine learning microservice using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project you will:
* Test your project code using linting
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker and make a prediction
* Improve the log statements in the source code for this application
* Configure Kubernetes and create a Kubernetes cluster
* Deploy a container using Kubernetes and make a prediction
* Upload a complete Github repo with CircleCI to indicate that your code has been tested

You can find a detailed [project rubric, here](https://review.udacity.com/#!/rubrics/2576/view).

**The final implementation of the project will showcase your abilities to operationalize production microservices.**

---

## Setup the Environment

* Create a virtualenv with Python 3.7 and activate it. Refer to this link for help on specifying the Python version in the virtualenv.
```bash
python3 -m pip install --user virtualenv
# You should have Python 3.7 available in your host.
# Check the Python path using `which python3`
# Use a command similar to this one:
python3 -m virtualenv --python=<path-to-Python3.7> .devops
source .devops/bin/activate
```
* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Run via kubectl

### Python CircleCI 2.0 configuration file

Check [link](https://circleci.com/docs/language-python/) for more details


## Project Setup

### 1- Create EC2 instance with the following specs

- OS [Ubuntu 18.4 LTS (HVM)]
- Instance Type [t3.small]
- Keypair [Required (**.pem**)]
- Security Group [Default]
- Storage [20 GiB-gp2]

### 2- Connect to it using [Remote Explorer]

```
ssh -VT ubuntu@[EC2 External IP Address]
```

### 3- clone the project repository, and navigate to the project folder

```
git clone https://github.com/udacity/DevOps_Microservices.git
cd DevOps_Microservices/project-ml-microservice-kubernetes
```

### 4- Update packages

```
sudo apr-get update
```

```
sudp apt-get upgrade python3
```

```
sudo apt-get install python3-venv
```
### 5- Create (and activate) a new environment, named .devops with Python 3. If prompted to proceed with the install (Proceed [y]/n) type y

```
python3 -m venv ~/.devops
source ~/.devops/bin/activate
```

### 6- Install make

```
sudo apt install make
```

### 7- Installing dependencies via project Makefile

```
make install
```

### 8- create a free docker account

- you can create it from this [link](https://hub.docker.com/signup)
- you’ll choose a unique username and link your email to a docker account. Your username is your unique docker ID.

- To install the latest version of docker, choose the Community Edition (CE) for your operating system, on [How To Install and Use Docker on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04).
- It is also recommended that you install the latest, stable release

### 9- Docker install and Configure

### Step 1 — Installing Docker

1. Update your existing list of packages

```
sudo apt update
```

2. Install a few prerequisite packages which let apt use packages over HTTPS

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

3. Then add the GPG key for the official Docker repository to your system

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

4. Add the Docker repository to APT sources

```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
```

5. Update the package database with the Docker packages from the newly added repo

```
sudo apt update
```

6. Make sure you are about to install from the Docker repo instead of the default Ubuntu repo

```
apt-cache policy docker-ce
```

> You’ll see output like this, although the version number for Docker may be different

**Output of apt-cache policy docker-ce**
```
docker-ce:
  Installed: (none)
  Candidate: 18.03.1~ce~3-0~ubuntu
  Version table:
     18.03.1~ce~3-0~ubuntu 500
        500 https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages
```

> Notice that docker-ce is not installed, but the candidate for installation is from the Docker repository for Ubuntu 18.04 (bionic).

7. install Docker

```
sudo apt install docker-ce
```

8. Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it’s running

```
sudo systemctl status docker
```

- After installation, you can verify that you’ve successfully installed docker by printing its version in your terminal
```
docker --version
```

### Step 2 — Executing the Docker Command Without Sudo (Optional)

1. Switch user
```
sudo su
```

2. Reboot
```
reboot now
```

3. Create a password

```
sudo passwd ubuntu
```

4. If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group

```
sudo usermod -aG docker ${USER}
```

5. To apply the new group membership, log out of the server and back in, or type the following

```
su - ${USER}
```

> You will be prompted to enter your user’s password to continue.

6. To confirm that docker is running

```
docker ps
```

### 10- Run Lint Checks

1. Install hadolint following the instructions (inside the instance itself not the venv)

```
sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 && sudo chmod +x /bin/hadolint
```

2. Retuen to the project folder

```
ubuntu@ip-172-31-2-67:~/project-ml-microservice-kubernetes
```

```
source ~/.devops/bin/activate
cd project-ml-microservice-kubernetes
```

3. Run this command to see if hadolint catches any errors in your Dockerfile

```
make lint
```

> If you faced a problem you should [Comment] pylint --disable=R,C,W1203,W1202 app.py in the [Makefile]

4. Ensure Everything is file with Dockerfile

```
hadolint Dockerfile
```

### 11- Install minikube

1. Go to this [link](https://minikube.sigs.k8s.io/docs/start/) and choose [**linux** as your OS]
2. Install minikube

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

3. Ensure it works

```
minikube version
```

### 12- Install kubectl

1. Go to this [link](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

2. Install kubectl binary with curl on Linux

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

3. Install kubectl

```
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

4. Test to ensure the version you installed is up-to-date

```
kubectl version --client

```

```
kubectl version --output yaml
```

5. Start your minikube

```
minikube start
```

> If you faced an issue starting your minikube fo that

```
sudo usermod -aG docker ${USER}
su - ${USER}
```

> Ensure that you are inside your venv and then

```
minikube status
```

```
kubectl version --output yaml
```

### 12- Start to edit your [**Dockerfile**]

### 13- Start to edit your [**run_docker.sh**]

### Step 1: Build image and add a descriptive tag

```
docker build --tag=mlproject .
```

### Step 2: List docker images

```
docker image ls
```

### Step 3: Run flask app

```
docker run -p 8000:80 mlproject
```

> You can interact now with localhost using

```
curl localhost:8000 <h3>Sklearn Prediction Home</h3>
```

```
curl localhost:8000
```

> Ensure that you are inside your venv and your docker container is up and running

### NOTE

- You can always [**STOP**] it by press [**CTRL + C**

- You can rerun it by executing [run_docker.sh]

```
./run_docker.sh
```

### 14- Make Predictions

- Ensure docker is running and in the anther terminal run [make_predictions.sh]

```
./make_predictions.sh
```

### 15- TO DO:  Log the output prediction value

- Add this line of code

```
LOG.info(f"output prediction: {prediction}")
```

### 15- Make Predictions again

- Ensure docker is running and in the anther terminal run [make_predictions.sh]

```
./make_predictions.sh
```

### 16- Edit [upload_docker.sh]

### 17- Run [upload_docker.sh]

```
./upload_docker.sh
```

### 18- Edit [run_kubernetes.sh]

### 19- Run [run_kubernetes.sh]

1. At first you will need to start minikube

```
minikube start
```

2. Check that you have one cluster running

```
kubectl config view
```

> you should see at least one cluster with a certificate-authority and server.

3. Execute [run_kubernetes.sh]

```
./run_kubernetes.sh
```

4. stop minikube

```
minikube stop
```

## 20- Save the output logs of both [run_kubernetes.sh & run_kubernetes.sh]

# Thanks