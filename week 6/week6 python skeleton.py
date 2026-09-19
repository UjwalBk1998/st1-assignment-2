class Patient:

    def __init__(self, patientID, name, contactDetails):
        self.patientID = patientID
        self.name = name
        self.contactDetails = contactDetails
    def requestAppointment(self):
        pass
    def cancelAppointment(self):
        pass
class Practitioner:
    def __init__(self, practitionerID, name, availability):
        self.practitionerID = practitionerID
        self.name = name
        self.availability = availability
    def provideAvailability(self):
        pass
    def manageAppointment(self):
        pass
class Appointment:
    def __init__(self, appointmentID, dateTime, status):
        self.appointmentID = appointmentID
        self.dateTime = dateTime
        self.status = status
    def createBooking(self):
        pass
    def checkStatus(self):
        pass
    def cancel(self):
        pass
