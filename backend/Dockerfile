FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install gunicorn==20.1.0

COPY requirements.txt .
RUN ls -l /app && cat /app/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Command to run the application
#MD ["python", "manage.py", "runserver", "0:8000"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
