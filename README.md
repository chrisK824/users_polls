#####  Simple project for a book reviews system

#####  Stack 
* fastAPI web framework
* postgreSQL database

##### Docker installation and run the server
* `docker build -t users-polls .`
* `docker run -d -p 9999:9999 users-polls`
* Docker container will deploy the web app
* Access the API at `localhost:9999/v1/`
* Access the API documentation at `localhost:9999/v1/documentation`


#####  Native installation and run the server
* Use an environment with `python3` installed
* Open a terminal and navigate to project's main folder
* Create a python virtual environment by running the following command:
`python3.9 -m venv python_venv`
* Activate the python virtual environment by running the command:
`source python_venv/bin/activate`
* Install requirements of app by running the following command:
`pip3 install -r requirements.txt`
*  Run the server `python3 src/main.py`
*  Access the API at `localhost:9999/v1`
*  Access the API documentation at `localhost:9999/v1/documentation`

#
#####  Who do I talk to  
* christos.karvouniaris247@gmail.com