FROM python:3.8-slim 
WORKDIR /app
COPY . .
RUN pip3 install flask redis
EXPOSE 5002
CMD ["python", "app.py"]