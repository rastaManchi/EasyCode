FROM python:3.14

WORKDIR /app_dir

ENV PYTHONDONTWRITEBITECODE=1 \
    PYTHONBUFFERED=1

RUN pip install --upgrade pip    

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD python app_dir/app.py
