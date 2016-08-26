from base import *
import dj_database_url



DATABASES = {
    'default': {

    }
}

CLEAR_DB_URL = os.environ.get("CLEARDB_DATABASE_URL", "")

DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)

ALLOWED_HOSTS = ['arcane-bastion-71587.herokuapp.com']
