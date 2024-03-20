class Protocol:
    def __init__(self, dict_json):
        self.dict_json = dict_json

    @property
    def client_id(self):
        return self.dict_json.get("client_id")

    @client_id.setter
    def client_id(self, x):
        self.dict_json["client_id"] = x

    @property
    def message_id(self):
        return self.dict_json.get("message_id")

    @message_id.setter
    def message_id(self, x):
        self.dict_json["message_id"] = x

    @property
    def ip(self):
        return self.dict_json.get("ip")

    @ip.setter
    def ip(self, x):
        self.dict_json["ip"] = x

    @property
    def login(self):
        return self.dict_json.get('login')

    @login.setter
    def login(self, x):
        self.dict_json["login"] = x

    @property
    def password(self):
        return self.dict_json.get('password')

    @password.setter
    def password(self, x):
        self.dict_json["password"] = x

    @property
    def action(self):
        return self.dict_json.get("action")

    @action.setter
    def action(self, x):
        self.dict_json["action"] = x

    @property
    def status(self):
        return self.dict_json.get("status")

    @status.setter
    def status(self, x):
        self.dict_json["status"] = x

    @property
    def ip_blocked(self):
        return self.dict_json.get("ip_blocked")

    @ip_blocked.setter
    def ip_blocked(self, x):
        self.dict_json["ip_blocked"] = x

    @property
    def is_admin(self):
        return self.dict_json.get("is_admin")

    @is_admin.setter
    def is_admin(self, x):
        self.dict_json["is_admin"] = x

    @property
    def other_data(self):
        return self.dict_json.get("other_data")

    @other_data.setter
    def other_data(self, x):
        self.dict_json["other_data"] = x
