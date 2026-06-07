import json
import os

class Database:
    def __init__(self, db_path='data/config.json'):
        self.db_path = db_path
        self.data = self._load_db()

    def _load_db(self):
        if not os.path.exists(self.db_path):
            return {"users": [], "trunks": [], "ivr": {}, "settings": {}}
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def save(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_user(self, extension):
        for user in self.data.get('users', []):
            if user['extension'] == extension:
                return user
        return None

    def add_user(self, extension, password, name):
        if self.get_user(extension):
            return False
        self.data['users'].append({"extension": extension, "password": password, "name": name})
        self.save()
        return True

    def get_ivr_config(self):
        return self.data.get('ivr', {})

    def get_settings(self):
        return self.data.get('settings', {})
