
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
        pass
#Appointment management operation
    def manageAppointments(self) -> None:
        pass