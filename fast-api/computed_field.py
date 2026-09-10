from typing import Annotated

from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field


class Patient(BaseModel):
    # Defining ideal schema

    name: Annotated[
        str,
        Field(
            min_length=1,
            max_length=50,
            title="Name of the patient",
            json_schema_extra={"example": "Divya"},
        ),
    ]

    email: EmailStr

    age: int = Field(gt=0, lt=120, description="Age must be between 1 and 119")

    LinkedIn: AnyUrl | None = None

    weight: float = Field(..., gt=0, description="Weight must be a positive number")

    height: float = Field(
        ..., gt=0, description="Height must be a positive number in meters"
    )

    married: bool = False

    allergies: list[str] | None = None

    contact: dict[str, str]

    # -----------------------------
    # COMPUTED FIELD
    # -----------------------------

    @computed_field
    @property
    def bmi(self) -> float:

        bmi = round(self.weight / (self.height**2), 2)
        return bmi


patient_info = {
    "name": "div",
    "age": 33,
    "weight": 70.5,
    "height": 1.75,
    "email": "div@hdfc.com",
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact": {"phone": "123-456-7890"},
}


# Creating Patient object
patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)

    print("Data inserted successfully")


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print("bmi is:", patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)

    print("Data updated successfully")


update_patient_data(patient1)
