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
        self.patientID = patientID #Patient id is stored
        self.name = name #patient name is stored
        self.contactDetails = contactDetails #patient contact details is stored
    def requestAppointment(self) -> None:
        pass
    def cancelAppointment(self) ->None:
        pass


