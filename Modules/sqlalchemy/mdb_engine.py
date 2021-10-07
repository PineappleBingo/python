from sqlalchemy import create_engine

# default
# engine = create_engine("mariadb://root:little5@localhost:3306/k2")

# pymysql
engine = create_engine("mysql+pymysql://root:little5@localhost:3306/k2")

# MySQL-connector-python
# engine = create_engine("mysql+mysqlconnector://root:little5@localhost:3306/k2")

# Syntax Reference
# dialect+driver://username:password@host:port/database
