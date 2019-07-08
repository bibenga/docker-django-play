
echo Тут еще один магичиский код который ждёт БД

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "handler-db" -U "rds" -c '\q'; do
  >&2 echo "handler-db is unavailable - sleeping"
  sleep 1
done

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "sensor-db" -U "rds" -c '\q'; do
  >&2 echo "sensor-db is unavailable - sleeping"
  sleep 1
done

echo А тут нету магии которая проверит что таблицы в sensor-db уже созданы

/opt/venv/bin/python /opt/app/manage.py migrate
/opt/venv/bin/python /opt/app/manage.py clearsessions
/opt/venv/bin/python /opt/app/manage.py collectstatic -c --noinput

/opt/venv/bin/python /opt/app/manage.py devadmin

#/opt/venv/bin/uwsgi /opt/app/uwsgi.ini
/usr/bin/supervisord -c /opt/app/supervisor.conf
