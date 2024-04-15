FROM python:3.11.4
ENV PYTHONUNBUFFERED=1
WORKDIR /technical_test_project
COPY requirements.txt /technical_test_project/
RUN pip install -r requirements.txt
COPY . /technical_test_project/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

