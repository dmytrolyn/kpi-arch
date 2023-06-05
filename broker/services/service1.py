class Service1:
    def __init__(self, broker):
        self.broker = broker
        self.broker.subscribe('event', self.handle_event)

    def handle_event(self, *args, **kwargs):
        print('Service 1 processing:', args, kwargs)