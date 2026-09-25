
#Enumeration allows us to create a fixedd set of allowed values.
from enum import Enum
class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"

# Class Appointment is created
class Appointment:
    #The constructor --init-- will run automatically when we create an appointment object.
    def __init__(self,appointmentID: str,dateTime: str,status: AppointmentStatus):
        #need to validate. appointment Id and date and time cannot be empty.
        if not appointmentID:
            raise ValueError("Appointment ID cannot be empty")

        if not dateTime:
            raise ValueError("Appointment date and time cannot be empty")
# storing appointment Id, dateTime and status
        self.appointmentID = appointmentID
        self.dateTime = dateTime
        self.status = status
#if the appointment is cancelled it wont return to schedule unless an explicit business rule allows it.
    def createBooking(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError(
                "A cancelled appointment cannot be booked"
            )
#this method helps to check the status of the Appointment.
    def checkStatus(self) -> AppointmentStatus:
        return self.status
#so this will allow us to stop from cancelling the appointment that has already been canceled.
    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError(
                "Appointment is already cancelled"
            )

        self.status = AppointmentStatus.CANCELLED