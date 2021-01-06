#!/bin/bash
cd $(dirname $0)
sudo python3 devicestatusmqodsname.py
sudo python3 DeviceStatusSinkRedis.py
sudo python3 etl-compute-mon.py
sudo python3 etl-compute.py
sudo python3 etl-excel-transf.py
sudo python3 etl-mon.py
sudo python3 flink_dws_extra.py
sudo python3 flink_dws.py
sudo python3 flink_oee_dwd_dws.py
sudo python3 ipqcstream.py
sudo python3 RabbitMQ2KafkaMain9455748790208.py
sudo python3 RabbitMQ2KafkaMain9455767169472.py
sudo python3 RabbitMQ2KafkaMain9481401510880.py
sudo python3 RabbitMQ2KafkaMain338930859769856.py