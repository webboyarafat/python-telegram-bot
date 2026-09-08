class Database:
    def __init__(self):
        self.users = {}

    def check_if_user_exists(self, user_id: int):
        return user_id in self.users

    def add_new_user(self, user_id: int, chat_id: int, username: str = "", first_name: str = "", last_name: str = ""):
        if user_id not in self.users:
            self.users[user_id] = {
                "chat_id": chat_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "last_interaction": None,
                "current_dialog_id": None,
                "current_model": "gpt-4o-mini",
                "current_chat_mode": "general",
                "n_used_tokens": {},
                "n_transcribed_seconds": 0.0,
                "n_generated_images": 0,
                "dialogs": {}
            }

    def start_new_dialog(self, user_id: int):
        if user_id in self.users:
            dialog_id = len(self.users[user_id]["dialogs"]) + 1
            self.users[user_id]["current_dialog_id"] = dialog_id
            self.users[user_id]["dialogs"][dialog_id] = []

    def get_user_attribute(self, user_id: int, key: str):
        if user_id in self.users:
            return self.users[user_id].get(key)
        return None

    def set_user_attribute(self, user_id: int, key: str, value):
        if user_id in self.users:
            self.users[user_id][key] = value

    def get_dialog_messages(self, user_id: int, dialog_id: int = None):
        if user_id in self.users:
            if dialog_id is None:
                dialog_id = self.users[user_id]["current_dialog_id"]
            return self.users[user_id]["dialogs"].get(dialog_id, [])
        return []

    def set_dialog_messages(self, user_id: int, messages: list, dialog_id: int = None):
        if user_id in self.users:
            if dialog_id is None:
                dialog_id = self.users[user_id]["current_dialog_id"]
            self.users[user_id]["dialogs"][dialog_id] = messages

    def update_n_used_tokens(self, user_id: int, model: str, n_input_tokens: int, n_output_tokens: int):
        if user_id in self.users:
            tokens_dict = self.users[user_id]["n_used_tokens"]
            if model not in tokens_dict:
                tokens_dict[model] = {"n_input_tokens": 0, "n_output_tokens": 0}
            tokens_dict[model]["n_input_tokens"] += n_input_tokens
            tokens_dict[model]["n_output_tokens"] += n_output_tokens
