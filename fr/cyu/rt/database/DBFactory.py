import mysql.connector
from influxdb_client import InfluxDBClient
from fr.cyu.rt.utils.Constant import Constant as ct


class DBFactory:
    @staticmethod
    def get_instance_influx_db():
        return InfluxDBClient(url=ct.INFLUX_DB_URL, token=ct.INFLUX_DB_TOKEN)

    @staticmethod
    def get_instance_mysql_db():
       return mysql.connector.connect(user=ct.MYSQL_DB_USER, password=ct.MYSQL_DB_PASSWORD, host=ct.MYSQL_DB_HOST,
                                      database=ct.MYSQL_DB_NAME)