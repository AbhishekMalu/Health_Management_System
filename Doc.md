# **Run this project :**
First, clone the repository to your local machine:

```bash
  git clone https://github.com/AbhishekMalu/Health_Management_System
```
Go to the project directory

```bash
  cd Health_Management_System
```

Create the virtual Environment
```bash
  virtualenv env
```
Activate your environment
```bash
  ./env/Scripts/activate
```
Then Install the required Dependencies. And update requirements.txt file
```bash
  pip freeze > requirements.txt
```
To Download Required Package
```bash
  pip install -r requirements.txt
```

command to run the streamlit app: 
```bash
  streamlit run {your_app}.py
```
command to run the FastAPI 
```bash
  uvicorn {your_app}:app --host 0.0.0.0 --port 8000
```