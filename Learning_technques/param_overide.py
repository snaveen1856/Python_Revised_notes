"""
# !/usr/bin/python


# sutas_dict = {'raisebugs':'yes','jiraurl':'url','jirapwd':'xxx','jirausr':'xxx','jiraaffectversion':'version',
# 'jiraenv':'env','jirawatcher':'yes','loglevel':'yes','slack':'No'}
from jinja2 import Template
from kombu import Connection, Exchange, Queue

exchange_item = Exchange("item", "direct", durable=True)
queue_item = Queue("Ram", exchange=exchange_item, routing_key="Ram")


def process_Ram(body, message):
    print(body)
    message.ack()


with Connection("amqp://Ram:Ram@10.10.1.12//") as conn:
    # Consumer
    with conn.Consumer(queue_item, callbacks=[process_Ram]) as consumer:
        # process message and handle events on all channel

        while True:
            conn.drain_events()

sutas_dict = {"jiraurl": "https://github.com/srikanth0327", "Teams": "No"}
tm = Template(open('srikanth_docker').read())

file = tm.render(sutas_dict)

print(file)

doc = open('Dockerfile', 'w')
doc.write(file)


class GTAProducer:
    def __init__(self):
        queue_name = "Publisher"
        self.routing_key = "Publisher"

        self.exchange_items = Exchange("items", "direct", durable=True)
        self.queue_items = Queue(queue_name,exchange=self.exchange_items, routing_key=self.routing_key)
    def publish(self, ddata):
        try:
            data = ddata
            with Connection("amqp://Ram:Ram@10.10.1.12//") as conn:
                producer = conn.Producer(serializer="json")
                producer.publish(data, exchange=self.exchange_items, routing_key=self.routing_key,
                declare=[self.queue_items])
                print("Publish completed")

import json
from kombu import Connection, Exchange, Queue

class GTAProducer:
    def __init__(self):
        queue_name = "Publisher"
        self.routing_key = "Publisher"
        self.exchange_items = Exchange("items", "direct", durable=True)
        self.queue_items = Queue(queue_name,exchange=self.exchange_items, routing_key=self.routing_key)
        def publish(self, ddata):
        try:
            data = ddata
            with Connection("amqp://Ram:Ram@10.10.1.12//") as conn:
            producer = conn.Producer(serializer="json")
            producer.publish(data, exchange=self.exchange_items, routing_key=self.routing_key,
            declare=[self.queue_items])
            print("Publish completed")
        except Exception as e:
            print("Exception occurred",str(e))
            raise e
if __name__ == '__main__':
    gpub = GTAProducer()
    d={"a1":1,"b1":2} # actual data you can pass like job_id and routing_key
    gpub.publish(d) # publish data
    gpub1 = GTAProducer()
    gpub1.publish({"c1": 3, "d1": 4})


"""

from kombu import Connection, Exchange, Queue
from jinja2 import Template


def create_dockerfile(json_data, message):
    """
    method which will read docker file
    :param json_data:
    :param message:
    :return:
    """
    print(json_data)
    sutas_dict = json_data
    tm = Template(open('gss_docker').read())
    file = tm.render(sutas_dict)
    print(file)
    doc = open('Dockerfile', 'w')
    doc.write(file)
    message.ack()


class GTAparmsRide:

    def __init__(self):
        queue_name = "Publisher"
        self.routing_key = "Publisher"

        self.exchange_items = Exchange("items", "direct", durable=True)
        self.queue_items = Queue(queue_name, exchange=self.exchange_items, routing_key=self.routing_key)

    def param_overide(self):
        try:
            # data = ddata
            with Connection("amqp://Ram:Ram@10.10.1.12//") as conn:
                # Consumer
                with conn.Consumer(self.queue_items, callbacks=[create_dockerfile]) as consumer:
                    # process message and handle events on all channel

                    while consumer:
                        conn.drain_events()
                    print("Param override completed")
        except Exception as e:
            print("Exception occurred", str(e))
            raise


if __name__ == '__main__':
    params = GTAparmsRide()
    params.param_overide()
