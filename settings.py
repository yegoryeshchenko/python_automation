from os.path import join

from dynaconf import Dynaconf

from constants import BASE_PATH


settings = Dynaconf(
    envvar_prefix="DYNACONF",  # export envvars with `export DYNACONF_FOO=bar`.
    settings_files=[join(BASE_PATH, 'base_settings.ini'), join(BASE_PATH, 'base_secrets.ini')],  # Load files in the given order.,
    load_dotenv=True,
    environments=True,  # одруківка :/
)
