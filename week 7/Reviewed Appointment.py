from enum import Enum

class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"

class Appointment:
    def __init__(self,appointmentID: str,dateTime: str,status: AppointmentStatus):

        if not appointmentID:
            raise ValueError("Appointment ID cannot be empty")

        if not dateTime:
            raise ValueError("Appointment date and time cannot be empty")

        self.appointmentID = appointmentID
        self.dateTime = dateTime
        self.status = status

    def createBooking(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError(
                "A cancelled appointment cannot be booked"
            )

    def checkStatus(self) -> AppointmentStatus:
        return self.status

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError(
                "Appointment is already cancelled"
            )

        self.status = AppointmentStatus.CANCELLED