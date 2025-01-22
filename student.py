import random
from events import ApplicationSubmittedEvent

class Student:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def apply_to_university(self, university, program):
        event = ApplicationSubmittedEvent(
            f"{self.first_name} {self.last_name}", 
            program
        )
        university.communication_queue.add_event(event)
        university.process_application(event)
