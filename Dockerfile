FROM python:slim

# Install system dependencies (including libpq-dev for psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to avoid issues with older versions
RUN pip install --upgrade pip

# Copy the requirements file first and install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Install other dependencies explicitly (like gunicorn, pymysql, cryptography)
RUN pip install --no-cache-dir gunicorn pymysql cryptography

# Copy the application files
COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./

# Ensure boot.sh is executable
RUN chmod a+x boot.sh

# Set environment variables for Flask
ENV FLASK_APP=microblog.py

# Optional: Compile translations if using Flask-Babel or similar (only if necessary)
RUN flask translate compile

# Expose port 5000
EXPOSE 5000

# Use the boot script to start the application
ENTRYPOINT ["./boot.sh"]
