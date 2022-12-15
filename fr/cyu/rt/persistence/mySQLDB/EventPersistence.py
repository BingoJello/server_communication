from fr.cyu.rt.business.model.Event import Event
import mysql.connector
from datetime import datetime
from fr.cyu.rt.database.DBFactory import DBFactory


class EventPersistence:
    @staticmethod
    def insertEvent(event : Event):
        try:
            db = DBFactory.get_instance_mysql_db()
            cursor = db.cursor()
            print(event.getImg())
            if event.getImg() is not None or event.getImg() != "None":
                sql = "INSERT INTO event(id_event, id_sensor, label_event, label_sensor, timestamp_event_insert, " \
                      "timestamp_event_receive, measurement, img) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (event.getEventTypeID(), event.getSensorTypeID(), event.getEventTypeLabel(), event.getSensorTypeLabel(),
                       datetime.now().isoformat(), event.getDateTime().isoformat(), event.getMeasure(), event.getImg())
            else:
                sql = "INSERT INTO event(id_event, id_sensor, label_event, label_sensor, timestamp_event_insert, " \
                      "timestamp_event_receive, measurement) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                val = (event.getEventTypeID(), event.getSensorTypeID(), event.getEventTypeLabel(), event.getSensorTypeLabel(),
                       datetime.now().isoformat(), event.getDateTime().isoformat(), event.getMeasure())

            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    @staticmethod
    def getEventByRangeDate(datetime_start) :
        try :
            db = DBFactory.get_instance_mysql_db()
            cursor = db.cursor()

            sql = "SELECT * FROM event AS e WHERE e.timestamp_event_receive > %s"
            cursor.execute(sql, (datetime_start,))
            event = cursor.fetchone()
            db.commit()
            cursor.close()
            db.close()
            return event
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))