''' Singleton'''
def Singleton(cls):
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

'''eventBus '''
class EventBus:
    def __init__(self):
        self.listeners = {}

    def on(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def off(self, event_name, callback):
        if event_name in self.listeners:
            self.listeners[event_name] = [cb for cb in self.listeners[event_name] if cb != callback]

    def once(self, event_name, callback):
        def wrapper(*args, **kwargs):
            callback(*args, **kwargs)
            self.off(event_name, wrapper)
        self.on(event_name, wrapper)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(*args, **kwargs)

# 测试用例
if __name__ == "__main__":
    event_bus = EventBus()

    def handle_event(data):
        print(f"Event received with data: {data}")

    event_bus.on("test_event", handle_event)
    event_bus.emit("test_event", "Hello, World!")
    event_bus.off("test_event", handle_event)
    event_bus.emit("test_event", "This should not be printed")


    