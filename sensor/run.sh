
echo Тут магичиский код который ждёт БД

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "sensor-db" -U "rds" -c '\q'; do
  >&2 echo "sensor-db is unavailable - sleeping"
  sleep 1
done

/opt/venv/bin/python /opt/app/manage.py migrate
/opt/venv/bin/python /opt/app/manage.py clearsessions
/opt/venv/bin/python /opt/app/manage.py collectstatic -c --noinput

/opt/venv/bin/python /opt/app/manage.py devadmin

/opt/venv/bin/uwsgi /opt/app/uwsgi.ini
