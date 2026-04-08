Copy

FROM python:3.10
 
WORKDIR /app
 
COPY . .
 
RUN pip install --no-cache-dir openai pydantic fastapi uvicorn
 
EXPOSE 8000
 
CMD ["python", "server.py"]
