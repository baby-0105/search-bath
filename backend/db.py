from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from config import DBConfig

DB = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    DBConfig.MYSQL_USER,
    DBConfig.MYSQL_PASSWORD,
    DBConfig.MYSQL_HOST,
    DBConfig.MYSQL_DATABASE,
)

ENGINE = create_engine(
    DB,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
