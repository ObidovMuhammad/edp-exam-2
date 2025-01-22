class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class ApplicationSubmittedEvent(Event):
    def __init__(self, student_name, program):
        super().__init__("application_submitted", {
            "student_name": student_name, 
            "program": program
        })

class ApplicationRejectedEvent(Event):
    def __init__(self, student_name, program):
        super().__init__("application_rejected", {
            "student_name": student_name, 
            "program": program
        })

class ApplicationAcceptedEvent(Event):
    def __init__(self, student_name, program):
        super().__init__("application_accepted", {
            "student_name": student_name, 
            "program": program
        })

class EnrollmentConfirmedEvent(Event):
    def __init__(self, student_name, program):
        super().__init__("enrollment_confirmed", {
            "student_name": student_name, 
            "program": program
        })
