import random
from events import ApplicationAcceptedEvent, ApplicationRejectedEvent, EnrollmentConfirmedEvent
from communication_queue import CommunicationQueue

class University:
    def __init__(self, name):
        self.name = name
        self.communication_queue = CommunicationQueue()
        self.enrolled_students = []

    def process_application(self, event):
        if random.choice([True, False]):
            acceptance_event = ApplicationAcceptedEvent(
                event.payload['student_name'], 
                event.payload['program']
            )
            self.communication_queue.add_event(acceptance_event)
            
            enrollment_event = EnrollmentConfirmedEvent(
                event.payload['student_name'], 
                event.payload['program']
            )
            self.communication_queue.add_event(enrollment_event)
        else:
            rejection_event = ApplicationRejectedEvent(
                event.payload['student_name'], 
                event.payload['program']
            )
            self.communication_queue.add_event(rejection_event)
