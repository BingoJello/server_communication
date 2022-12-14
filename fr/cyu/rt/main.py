from business.model.Event import Event
from fr.cyu.rt.persistence.mySQLDB.EventPersistence import EventPersistence as ep_mysql
from fr.cyu.rt.persistence.influxDB.EventPersistence import EventPersistence as ep_influx
from datetime import datetime
import time
import ray

#print(EventPersistence.getEventByLabelEvent('BUTTON_PRESSED'))



event = Event(2, 1, time.time(), 0.8989)

ep_influx.insertEvent(event)

ep_influx.getEvent()

##ray.init()

# Define functions you want to execute in parallel using
# the ray.remote decorator.


# Execute func1 and func2 in parallel.
#ray.get([func1.remote(), func2.remote()])

#ret_id1 = func1.remote()
#ret_id2 = func1.remote()
#ret1, ret2 = ray.get([ret_id1, ret_id2])