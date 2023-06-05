from broker import Broker
from services import Service1, Service2

def main():
    broker = Broker()
    service1 = Service1(broker)
    service2 = Service2(broker)

    broker.publish('event', 'Hello', name='World')

if __name__ == '__main__':
    main()