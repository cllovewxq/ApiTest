# -*- coding: utf-8 -*-
# 数据库ORM连接类
# 作者: 三石
# 时间: 2021-06-08

import pymysql
from urllib import parse
from sqlalchemy.exc import ProgrammingError, OperationalError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from work.utils import UtilsLog

pymysql.install_as_MySQLdb()


class UtilsDB:
    def __init__(self):
        self.logger = UtilsLog()
        self.logger.info("调用基础数据库连接类")
        self.logger.info(self.__class__)
        self.errors = ProgrammingError, OperationalError, MultipleResultsFound, NoResultFound, AttributeError

    def conn_base(self, db):
        """
        pgsql数据库连接方法
        :param db: 数据库信息
        :return: 游标session
        """
        try:
            engine = create_engine(db, encoding="utf-8")
            db_session = sessionmaker(bind=engine, expire_on_commit=False)
            session = db_session()
            self.logger.debug("数据库请求地址:")
            self.logger.debug(db)
            self.logger.debug(db_session)
            self.logger.debug(session)
            return session
        except self.errors as e:
            self.logger.error("异常:")
            self.logger.error(e)
            return False

    def conn_pgsql(self, db_json):
        """
        pgsql数据库连接方法
        :param db_json: 数据库json信息
        :return:
        """
        db_host = db_json["host"]
        db_port = db_json["port"]
        db_user = db_json["username"]
        db_pw = parse.quote_plus(db_json["password"])
        db_base = db_json["name"]

        db = "postgresql://%s:%s@%s:%s/%s" % (db_user, db_pw, db_host, db_port, db_base)
        session = self.conn_base(db=db)
        return session

    def conn_mysql(self, db_json):
        """
        mysql数据库连接方法
        :param db_json: 数据库json信息
        :return:
        """
        db_host = db_json["host"]
        db_port = db_json["port"]
        db_user = db_json["username"]
        db_pw = db_json["password"]
        db_base = db_json["name"]

        db = "mysql://%s:%s@%s:%s/%s?charset=utf8" % (db_user, db_pw, db_host, db_port, db_base)
        session = self.conn_base(db=db)
        return session
