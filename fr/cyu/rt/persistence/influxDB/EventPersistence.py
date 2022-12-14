from influxdb_client.client import write_api
import mysql.connector
from datetime import datetime
from fr.cyu.rt.database.DBFactory import DBFactory
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from fr.cyu.rt.utils.Constant import Constant as ct
from fr.cyu.rt.business.model.Event import Event

class EventPersistence:
    @staticmethod
    def insertEvent(event:Event):
        client = DBFactory.get_instance_influx_db()

        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = Point("log") \
            .tag("id_event", event.getEventTypeID()) \
            .tag("label_event", event.getEventTypeLabel()) \
            .tag("id_sensor", event.getSensorTypeID()) \
            .tag("label_sensor", event.getSensorTypeLabel()) \
            .field("measure", event.getMeasure()) \
            .time(datetime.utcfromtimestamp(event.getTimestamp()), WritePrecision.NS)
            #.time(datetime.utcnow(), WritePrecision.NS)

        write_api.write(ct.INFLUX_DB_BUCKET, ct.INFLUX_DB_ORG, point)

    @staticmethod
    def getEvent():
        client = DBFactory.get_instance_influx_db()
        query_api = client.query_api()
        query = 'from(bucket:"atelier_rt")\
        |> range(start: -1h)\
        |> range(end: -10m)\
        |> filter(fn:(r) => r._measurement == "log")\
        |> filter(fn:(r) => r.id_event== "5")'

        result = query_api.query(org=ct.INFLUX_DB_ORG, query=query)

        results = []
        for table in result :
            for record in table.records :
                results.append((record.tagsrecord.get_time().strftime("%m/%d/%Y, %H:%M:%S.%f%z"), record.get_measurement(), record.get_field(), record.get_value()))

        print(results)


