# Use Python
FROM python:3.13.3

# Create & enter /app folder
WORKDIR /app

# Copy files
COPY . .

# Install libraries
RUN pip install -r requirements.txt

EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
