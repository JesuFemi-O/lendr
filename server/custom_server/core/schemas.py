from pydantic import BaseModel

class HearbeatResult(BaseModel):
    is_alive: bool

class LoanModelPayload(BaseModel):
    property_area: str
    self_employed: str
    education_level: str
    dependents: int
    married: str
    gender: str
    income: int
    coapplicant_income: int
    loan_amount: int
    loan_term: int

class LoanPredictionResult(BaseModel):
    Eligible: str = "No"