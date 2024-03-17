class RequestForServer:
    def __init__(self, req):
        self.req = req

    @property
    def message_id(self):
        return self.req.get('message_id')

    @property
    def client_id(self):
        return self.req.get('client_id')

    @property
    def action(self):
        return self.req.get('action')

    @property
    def login(self):
        return self.req.get('login')

    @property
    def password(self):
        return self.req.get('password')

    @property
    def permissions(self):
        return self.req.get('permissions')

    @property
    def other_data(self):
        return self.req.get('other_data')


class ResponseForServer:
    def __init__(self, res):
        self.res = res

    @property
    def client_id(self):
        return self.res.get("client_id")

    @property
    def message_id(self):
        return self.res.get("message_id")

    @message_id.setter
    def message_id(self, x):
        self.res["message_id"] = x

    @property
    def action(self):
        return self.res.get("action")

    @property
    def status(self):
        return self.res.get("status")

    @status.setter
    def status(self, x):
        self.res["status"] = x

    @property
    def permissions(self):
        return self.res.get("permissions")

    @permissions.setter
    def permissions(self, x):
        self.res["permissions"] = x

    @property
    def other_data(self):
        return self.res.get("other_data")

    @other_data.setter
    def other_data(self, x):
        self.res["other_data"] = x
