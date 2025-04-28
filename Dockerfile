#1. Kavya Shivakumar (G01520934)
#2. Sehaj Gill (G01535820)
#3. Jaanaki Swaroop P(G01502869)
#4. Koushik Vasa (G01480627)
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY survey_data .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (change if different)
EXPOSE 5000

# Define environment variable (optional for Flask)
#ENV FLASK_APP=app.py

# Run the app
CMD ["python", "app.py"]