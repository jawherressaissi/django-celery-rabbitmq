from celery import Celery

app = Celery('dkrapp',
             broker='amqp://guest:guest@localhost:5672//',
             backend='rpc://',
             include=['dkrapp.tasks'])

app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule = {
    'print-hello': {
        'task': 'hello',
        'schedule': 5.0,
        'args': ()
    },
}
app.conf.timezone = 'CET'

if __name__ == '__main__':
    app.start()