# -*- coding: utf-8 -*-
# 通用公共类
# 作者: 三石
# 时间: 2021-06-02

from work.utils import UtilsRsa, UtilsRequest, UtilsCheck, UtilsResponse, UtilsLog, UtilsYaml, UtilsDB


class BasePublic(object):
    def __init__(self):
        self.logger = UtilsLog()
        self.logger.info("调用通用公共类")

    def open_session_pgsql(self, db_json):
        """
        打开连接-pgsql
        :param db_json: db连接信息json
        :return:
        """
        self.logger.info("打开连接-pgsql")
        db = UtilsDB()
        session = db.conn_pgsql(db_json=db_json)
        return session

    def close_session(self, session):
        """
        关闭连接
        :param session:
        :return:
        """
        self.logger.info("关闭连接...")
        session.close()

    def clear_data_pgsql(self, db_json, db_table, id_field, where_field, field_value):
        """
        初始化测试数据-pgsql
        :param db_json: db连接信息json
        :param db_table: 表
        :param id_field: id字段
        :param where_field: 查询字段
        :param field_value: 查询字段值
        :return:
        """
        session = self.open_session_pgsql(db_json=db_json)

        sql_select = "select {} from {} where {} like '{}%'".format(id_field, db_table, where_field, field_value)
        self.logger.info("执行查询sql: {}".format(sql_select))

        resp_select = session.execute(sql_select)
        ids = []
        for x, y in enumerate(resp_select):
            ids.append(y[0])

        self.logger.info("查询ids结果: {}".format(ids))

        if not ids:
            self.logger.info("无测试数据,无须执行")
        elif len(ids) == 1:
            sql_delete = "delete from {} where {} = '{}'".format(db_table, id_field, ids[0])
            self.logger.info("执行删除sql: {}".format(sql_delete))

            session.execute(sql_delete)
            session.commit()
        else:
            sql_delete = "delete from {} where {} in {}".format(db_table, id_field, tuple(ids))
            self.logger.info("执行删除sql: {}".format(sql_delete))

            session.execute(sql_delete)
            session.commit()

        self.close_session(session=session)
