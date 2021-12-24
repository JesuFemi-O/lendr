from logging import log
import pickle
import numpy as np
from loguru import logger
import random

from custom_server.core.schemas import LoanModelPayload, LoanPredictionResult

class LoanService(object):
    def __init__(self, path) -> None:
        self.path = path
        self._load_local_model()
    
    def _load_local_model(self):
        self.model = pickle.load(open(self.path, 'rb'))
    
    def _pre_process(self, payload:LoanModelPayload):
        logger.info(f"Pre processing payload: {payload.dict()}")
        payload_dict = payload.dict()
        return self._generate_vectors(payload_dict)
    
    def _generate_vectors(self, payload:dict)-> np.array:
        logger.info("Generating Prediction Vectors...")
        property_area = payload.get('property_area')
        self_employed = payload.get('self_employed')
        education_level = payload.get('education_level')
        dependents = payload.get('dependents')
        married = payload.get('married')
        gender = payload.get('gender')
        credit_history = payload.get('credit_history')
        income = payload.get('income')
        coapplicant_income = payload.get('coapplicant_income')
        loan_amount = payload.get('loan_amount')
        loan_term = payload.get('loan_term')
        
        total_income = income + coapplicant_income
        EMI = loan_amount / loan_term
        Balance_Income = total_income - (EMI * 1000)
        Gender_Female = int(gender.lower()=="female")
        Gender_Male = int(gender.lower()=="male")
        Married_No = int(married.lower()=="no")
        Married_Yes = int(married.lower()=="yes")
        Dependents_3 = int(dependents>=3)
        Dependents_0 = int(dependents==0)
        Dependents_1 = int(dependents==1)
        Dependents_2 = int(dependents==2)
        Education_Graduate = int(education_level.lower()=="yes")
        Education_Not_Graduate = int(education_level.lower()=="no")
        Self_Employed_No = int(self_employed.lower()=="no")
        Self_Employed_Yes = int(self_employed.lower()=="yes")
        Property_Area_Rural = int(property_area.lower()=="rural")
        Property_Area_Semiurban = int(property_area.lower()=="semiurban")
        Property_Area_Urban = int(property_area.lower()=="urban")
        
        # generate Cresit history
        seed = random.uniform(0, 1)
        
        if seed >= 0.86:
            Credit_History = 1.0
        else:
            Credit_History = 0.0
        
        logger.info(f"Credit History set to {Credit_History}")
            
        #create payload array:
        return np.array([[Credit_History, Gender_Female, Gender_Male, Married_No,
        Married_Yes, Dependents_3, Dependents_0, Dependents_1,
        Dependents_2, Education_Graduate, Education_Not_Graduate,
        Self_Employed_No, Self_Employed_Yes, Property_Area_Rural,
        Property_Area_Semiurban, Property_Area_Urban, EMI,
        Balance_Income]])


    def _predict(self, features:np.array) -> str:
        logger.info(f"Making prediction for vector: {features}")
        prediction_result = self.model.predict(features).tolist()[0]
        return prediction_result
    
    def predict(self, payload: LoanModelPayload) -> LoanPredictionResult:
        vectors = self._pre_process(payload)
        result = self._predict(vectors)
        if result == 1:
            logger.info("Applicant Loan application approved")
            return LoanPredictionResult(Eligible="Yes")
        else:
            logger.info("Applicant Loan application rejected")
            return LoanPredictionResult(Eligible="No")