class UserDTO:
    def __init__(self, username: str, id: int, password_hash: str, roles: list):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.roles = roles

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hash":self.password_hash,
            "roles": self.roles,
        }
