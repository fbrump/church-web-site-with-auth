from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


SECRET_KEY = "3409eedfe8abc39c02a5ce80816b4dca22832b5976fffc0af215efb104f69a88"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Scope:
    ACCOUNT_READ = "account:read"
    ACCOUNT_WRITE = "account:write"
    SMALL_GROUP_READ = "small-group:read"
    SMALL_GROUP_WRITE = "small-group:write"
    ADDRESS_READ = "address:read"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/accounts/token",
    scopes={
        Scope.ACCOUNT_READ: "Read information of the current user.",
        Scope.ACCOUNT_WRITE: "Register or update a new user.",
        Scope.SMALL_GROUP_READ: "Read small groups information.",
        Scope.SMALL_GROUP_WRITE: "Register or update small group.",
        Scope.ADDRESS_READ: "Read addresses information.",
    },
)
