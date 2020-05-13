"""
# !/usr/bin/python


# sutas_dict = {'raisebugs':'yes','jiraurl':'url','jirapwd':'xxx','jirausr':'xxx','jiraaffectversion':'version',
# 'jiraenv':'env','jirawatcher':'yes','loglevel':'yes','slack':'No'}
from jinja2 import Template
from kombu import Connection, Exchange, Queue

exchange_item = Exchange("item", "direct", durable=True)
queue_item = Queue("naveen", exchange=exchange_item, routing_key="naveen")


def process_naveen(body, message):
    print(body)
    message.ack()


with Connection("amqp://naveen:naveen@10.10.1.12//") as conn:
    # Consumer
    with conn.Consumer(queue_item, callbacks=[process_naveen]) as consumer:
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
            with Connection("amqp://naveen:naveen@10.10.1.12//") as conn:
                producer = conn.Producer(serializer="json")
                producer.publish(data, exchane=self.exchange_items, routing_key=self.routing_key, declare=[self.queue_items])
                print("Publish completed")


"""

from kombu import Connection, Exchange, Queue
from jinja2 import Template


def create_dockerfile(json_data, message):
    print(json_data)
    sutas_dict = json_data
    tm = Template(open('srikanth_docker').read())
    file = tm.render(sutas_dict)
    print(file)
    doc = open('Dockerfile', 'w')
    doc.write(file)
    message.ack()


class GTAParms_Ride:
    def __init__(self):
        queue_name = "Publisher"
        self.routing_key = "Publisher"

        self.exchange_items = Exchange("items", "direct", durable=True)
        self.queue_items = Queue(queue_name, exchange=self.exchange_items, routing_key=self.routing_key)

    def param_overide(self):
        try:
            # data = ddata
            with Connection("amqp://naveen:naveen@10.10.1.12//") as conn:
                # Consumer
                with conn.Consumer(self.queue_items, callbacks=[create_dockerfile]) as consumer:
                    # process message and handle events on all channel

                    while consumer:
                        conn.drain_events()
                    print("Param override completed")
        except Exception as e:
            print("Exception occurred", str(e))
            raise e




if __name__ == '__main__':
    params = GTAParms_Ride()
    params.param_overide()
