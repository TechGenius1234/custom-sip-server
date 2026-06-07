class IVREngine:
    def __init__(self, db):
        self.db = db
        self.config = db.get_ivr_config()

    def handle_digit(self, digit):
        menu = self.config.get('menu', {})
        if digit in menu:
            action = menu[digit]
            return action
        return {"action": "invalid"}

    def get_welcome_message(self):
        return self.config.get('welcome_message', 'welcome.wav')
