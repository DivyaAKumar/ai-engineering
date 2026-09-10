from typing import Annotated

from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator


class Patient(BaseModel):

    # Defining ideal schema

    name: Annotated[
        str,
        Field(
            min_length=1,
            max_length=50,
            title="Name of the patient",
            json_schema_extra={"example": "Divya"}
        )
    ]

    email: EmailStr

    age: int = Field(
        gt=0,
        lt=120,
        description="Age must be between 1 and 119"
    )

    LinkedIn: AnyUrl | None = None

    weight: float = Field(
        ...,
        gt=0,
        description="Weight must be a positive number"
    )

    married: bool = False

    allergies: list[str] | None = None

    contact: dict[str, str]

    # -----------------------------
    # MODEL VALIDATOR
    # -----------------------------

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):

        if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError("Emergency contact is required for patients above 60 years old")
        else:
            return model 


patient_info = {
    "name": "div",
    "age": 33,
    "weight": 70.5,
    "email": "div@hdfc.com",
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact": {
        "phone": "123-456-7890"
    }
}


# Creating Patient object
patient1 = Patient(**patient_info)


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)

    print("Data inserted successfully")


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)

    print("Data updated successfully")


insert_patient_data(patient1)
update_patient_data(patient1)