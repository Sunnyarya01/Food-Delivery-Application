# Appliction configuration
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'dksfhlkdsjflksjkfdijflkfjlfi'

class Constants:
    ADMIN = "admin"
    CUSTOMER = "customer"