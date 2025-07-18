# db_router.py
class AdminstartorRouter:
    def db_for_read(self, model, **hints):
        if model.__name__ == 'Adminstartor':
            return 'secondary'
        return None

    def db_for_write(self, model, **hints):
        if model.__name__ == 'Adminstartor':
            return 'secondary'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True  # or implement logic if needed

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'adminstartor':
            return db == 'secondary'
        return db == 'default'
