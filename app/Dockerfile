# our base image
FROM python:slim

# adding environment variable uuid
ENV UUID='a87b56a4-2aa5-48dd-b0cb-6a1ecfe41d20'

# installing requirements
RUN pip install flask
RUN apt-get update && apt-get install -y procps

# copy our application code
ADD webapp /home/webapp
WORKDIR /home/webapp

# specify the port number the container should expose
EXPOSE 8000

# run the application
CMD ["python", "./webapp.py"]
