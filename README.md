## **Internet Speed Test Web App**

A simple Python Flask application that measures and displays internet speed (download, upload, and ping). This project is containerized with Docker to ensure ease of deployment across various environments.

---

## **Features**

- Displays **download speed**, **upload speed**, and **ping** using the `speedtest-cli` library.
- Simple web-based UI using Flask.
- Dockerized for easy deployment and scalability.

---

## **Getting Started**

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.12 or later
- Docker
- Git

---

## **Installation**

### **Clone the Repository**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **Option 1: Run Locally (Without Docker)**

#### 1. Create a Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Run the Application

```bash
python app.py
```

#### 4. Access the Application

Open your browser and navigate to:

```plaintext
http://localhost:80
```

---

### **Option 2: Run with Docker**

#### 1. Build the Docker Image

```bash
docker build -t internet-speed-test .
```

#### 2. Run the Docker Container

```bash
docker run -p 80:80 internet-speed-test
```

#### 3. Access the Application

Open your browser and navigate to:

```plaintext
http://<your-server-ip>:80
```

> **Note:** If running on AWS EC2 or another cloud service, ensure port 80 is open in the security group.

---

## **Project Structure**

```
/your-repo
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Instructions for containerizing the app
├── templates/           # HTML templates for the app
│   └── index.html       # Main page template
└── README.md            # Project documentation
```

---

## **Configuration**

### Update Port (Optional)

By default, the app runs on port 80 when containerized. To change this:

1. Update the `EXPOSE` command in the `Dockerfile`.
2. Modify the `docker run` command's port mapping:
   ```bash
   docker run -p <your-port>:<container-port> internet-speed-test
   ```

---

## **Dependencies**

The project uses the following dependencies:

- Flask: Web framework.
- speedtest-cli: Library for measuring internet speed.

Install these dependencies via `pip install -r requirements.txt`.

---

## **Deployment**

### **On AWS EC2**

1. Launch an EC2 instance.
2. SSH into the instance:
   ```bash
   ssh -i <your-key.pem> ubuntu@<your-instance-ip>
   ```
3. Install Docker:
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   ```
4. Clone the repository and navigate to the directory:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
5. Build and run the Docker container:
   ```bash
   docker build -t internet-speed-test .
   docker run -p 80:80 internet-speed-test
   ```

To run a Docker container in detached mode (so it runs in the background), you can use the `-d` flag with the `docker run` command.

```bash
docker run -d -p 80:80 internet-speed-test
```

You can verify that the container is running by listing all running containers:

```bash
docker ps
```

Example -

```bash
adwibha@python-app$ docker run -d -p 80:80 internet-speed-test
d6bb7fe11340e35c610ff5e22f5382d44f0579b85da24cf90875f78d52a96571

adwibha@python-app$ docker ps
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                NAMES
d6bb7fe11340   internet-speed-test   "./venv/bin/python a…"   11 seconds ago   Up 10 seconds   0.0.0.0:80->80/tcp   eloquent_chandrasekhar

adwibha@python-app$ docker images
REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
internet-speed-test   latest    297b81ab022f   10 minutes ago   230MB
```

If you need to stop the container later, you can use the `docker stop` command followed by the container ID or name:

```bash
docker stop <container-id-or-name>
```

<img width="1385" alt="Screenshot 2025-01-16 at 12 42 36 PM" src="https://github.com/user-attachments/assets/f972d721-262b-4964-892a-195b497c3f06" />

6. Ensure your security group allows inbound traffic on port 80.

---

## **Troubleshooting**

### Common Issues

1. **Port Already in Use**:
   - Stop the conflicting process or run the app on a different port.
2. **Cannot Find a Test Server**:
   - Ensure the host has internet access and retry.

### Logs

View Docker container logs for debugging:

```bash
docker logs <container-id>
```
