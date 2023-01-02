FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Copy the rest of the source code
COPY . .

# Run the app
CMD ["streamlit", "run", "pdf-reader.py"]
