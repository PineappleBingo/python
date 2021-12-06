import psycopg2
from sqlalchemy import create_engine

# default
# engine = create_engine("mariadb://root:little5@localhost:3306/k2")

# pymysql
engine = create_engine("postgresql+psycopg2://postgres:0564@localhost:5432/TEST_DB")

# Syntax Reference
# dialect+driver://username:password@host:port/database

# PostgresSql Reference
# postgresql+psycopg2://user:password@host:port/dbname
