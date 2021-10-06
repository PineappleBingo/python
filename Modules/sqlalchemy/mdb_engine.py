from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://root:little5@localhost:3306/k2")
# dialect+driver://username:password@host:port/database
