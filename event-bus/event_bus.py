class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)
        return id(callback)

    def unsubscribe(self, subscription_id):
        for event, callbacks in self.subscribers.items():
            for callback in callbacks:
                if id(callback) == subscription_id:
                    callbacks.remove(callback)
                    return

    def publish(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)