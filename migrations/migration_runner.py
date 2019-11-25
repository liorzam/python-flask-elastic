import importlib.util
import glob
import os
import time

from elasticsearch import Elasticsearch


# TODO: Take each migration one-by-one by timestamp (Unix time) contained in the file-name and run them (in order)
# Ensure that the database is up-to-date with the migrations. Also, it should "checkpoint" the state so it doesn't
# repeat itself. Each migration task should run once


def run_migrations(es_object):
    all_files = glob.glob('./*es-migration.py')
    print(all_files)

    print('Sleeping for 25 seconds')
    time.sleep(25)

    all_modules = []
    for i, file in enumerate(all_files):
        spec = importlib.util.spec_from_file_location(f'module{i}', os.path.realpath(file))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        all_modules.append(module)

    migration_modules = [module for module in all_modules if 'Migration' in dir(module)]
    # TODO: run only the migrations that have not been run
    for module in migration_modules:
        migration_obj = module.Migration(es_object)
        migration_obj.execute()
        # TODO: save the state of the migration (it has been run successfully)


if __name__ == '__main__':
    es = Elasticsearch([{"host": "elasticsearch1", "port": 9200}])
    run_migrations(es)
