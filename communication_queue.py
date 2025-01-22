class CommunicationQueue:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def process_events(self):
        while self.events:
            event = self.events.pop(0)
            print(f"Processing event: {event.name}")
            print(f"Payload: {event.payload}")
