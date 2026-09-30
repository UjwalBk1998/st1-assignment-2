class Patient:
    #str is used as the type of the data.
    def __init__(self, patientID: str, name: str, contactDetails: str):
        #Creating basic validation prevents empty patient information
        if not patientID:
            raise ValueError("PatientId cannot be empty")
        if not name:
            raise ValueError("PatientName cannot be empty")
        if not contactDetails:
            raise ValueError("PatientContactDetails cannot be empty")
        #storing patient information
        self.patientID = patientID #Patient id is stored
        self.name = name #patient name is stored
        self.contactDetails = contactDetails #patient contact details is stored
    def requestAppointment(self) -> None:
        print(f"{self.name} requested appointment")
    def cancelAppointment(self, appointment) ->None:
        appointment.cancel()



class Practitioner:
    def __init__(self,practitionerID: str,name: str,availability: str):
        if not practitionerID:
            raise ValueError("Practitioner ID cannot be empty")
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        if not availability:
            raise ValueError("Practitioner availability cannot be empty")
#storing practitioner Id, name and availability
        self.practitionerID = practitionerID
        self.name = name
        self.availability = availability
#Providing availability
    def provideAvailability(self) -> None:
        print(f"{self.name} is available:" f"{self.availability}")
#Appointment management operation
    def manageAppointments(self) -> None:
        print(f"{self.name} is managing apppointments:")

from enum import Enum

class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"

class Appointment:
    bookedSlots = []
    def __init__(self,appointmentID: str,dateTime: str,status: AppointmentStatus, patient: Patient, practitioner: Practitioner):

        if not appointmentID:
            raise ValueError("Appointment ID cannot be empty")

        if not dateTime:
            raise ValueError("Appointment date and time cannot be empty")

        if not isinstance(status,AppointmentStatus):
            raise ValueError("Invalid appointment status")

        if not isinstance(patient,Patient):
            raise ValueError("Invalid patient")

        if not isinstance(practitioner,Practitioner):
            raise ValueError("Invalid practitioner")

        self.appointmentID = appointmentID
        self.dateTime = dateTime
        self.status = status

        self.patient = patient
        self.practitioner = practitioner

    def createBooking(self) -> None:

        booking_Slot = (self.practitioner.practitionerID, self.dateTime)

        if booking_Slot in Appointment.bookedSlots:
            raise ValueError("This practitioner is already booked at this time")

        Appointment.bookedSlots.append(booking_Slot)

        print (f"Appointment {self.appointmentID} " f"has been booked.")

    def checkStatus(self) -> AppointmentStatus:
        return self.status

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")

        booking_Slot = (self.practitioner.practitionerID, self.dateTime)
        if booking_Slot in Appointment.bookedSlots: Appointment.bookedSlots.remove(booking_Slot)

        self.status = AppointmentStatus.CANCELLED

        print(f"Appointment{self.appointmentID} " f"has been cancelled.")

#Testing

patient1 = Patient("P001", "Ujwal BK", "0822222222")
practitioner1 = Practitioner("PR001", "Dr Smith","Monday to Friday, 9am to 5pm")
appointment1 = Appointment("A001","30/09/2026 10:00 AM", AppointmentStatus.SCHEDULED, patient1, practitioner1)
patient1.requestAppointment()
practitioner1.provideAvailability()
practitioner1.manageAppointments()
appointment1.createBooking()
print("Appointment status", appointment1.checkStatus().value)

#Duplicate booking test
print("Duplicate Booking Test")
patient2 = Patient ("P002", "John Smith", "0822272222")
appointment2 = Appointment ("A002", "30/09/2026 10:00 AM", AppointmentStatus.SCHEDULED, patient2, practitioner1)
try: appointment2.createBooking()
except ValueError as e:
    print("Duplicate booking test passed:",e)

#Cancellation Test
print("cancellation test")
patient1.cancelAppointment(appointment1)
print("Appointment status", appointment1.checkStatus().value)

#Slot available after cancellation
print("slot available after cancellation")
appointment3= Appointment("A003", "30/09/2026 10:00 AM", AppointmentStatus.SCHEDULED, patient2, practitioner1)
try: appointment3.createBooking()
except ValueError as e:
    print("slot availability test failed",e)


#Invalid input test
print("invalid input test")
try: Patient("","John","0023453545")
except ValueError as e:
    print("Patient validation test passed:", e)

try: Practitioner("PR002","","Monday to Friday")
except ValueError as e:
    print("Practitioner validation test passed:", e)

try: Appointment("","30/09/2026 11:00AM", AppointmentStatus.SCHEDULED, patient1, practitioner1)
except ValueError as e:
    print("Appointment validation test passed:", e)


#Double cancellation test
try:patient1.cancelAppointment(appointment1)
except ValueError as e:
    print("Double cancellation test passed:",e)


