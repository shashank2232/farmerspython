from models.user import User
from dto.user_dto import UserDTO

class UserMapper:
    @staticmethod
    def to_dto(user: User) -> UserDTO:
        return UserDTO(
            id=user.id,
            username=user.username,
            roles=user.roles,
            password_hash=user.password_hash
        )

    @staticmethod
    def to_model(user_dto: UserDTO) -> User:
        user = User(
            id=user_dto.id,
            username=user_dto.username,
            roles=user_dto.roles,
            password_hash=user_dto.password_hash
        )
        return user
