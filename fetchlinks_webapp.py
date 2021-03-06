# TODO: CONFIGURE LOGGING
# TODO: IMPLEMENT FLASK-BOOTSTRAP
# systemd config
# https://blog.miguelgrinberg.com/post/running-a-flask-application-as-a-service-with-systemd
# journalctl -u fetchlinks_webapp

from app import app, db
from app.models import Posts, Twitter


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Posts': Posts, 'Twitter': Twitter}
