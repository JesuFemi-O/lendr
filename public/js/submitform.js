let loanPayload = {}

function setGender(gender) {
    loanPayload.gender = gender
}

function setPropertyArea(property_area) {
    loanPayload.property_area = property_area
}

function setSelfEmployed(self_employed) {
    loanPayload.self_employed = self_employed
}

function setEducationLevel(education_level) {
    loanPayload.education_level = education_level
}

function setMarried(married) {
    loanPayload.married = married
}

function setDependents() {
    let dependents = document.getElementById("dependents").value
    loanPayload.dependents = dependents
}

function setIncome() {
    let income = document.getElementById("income").value
    loanPayload.income = income
}

function setCoapplicantIncome(){
    let coapplicant_income = document.getElementById('coapplicant_income').value
    loanPayload.coapplicant_income = coapplicant_income
}

function setLoanAmount() {
    let loan_amount = document.getElementById("loan_amount").value
    loanPayload.loan_amount = loan_amount
}

function setLoanTerm() {
    let loan_term = document.getElementById("loan_term").value
    loanPayload.loan_term = loan_term
}

async function submitLoanPayLoad() {
    $('#dvLoading').show()
    const res = await axios.post("//fireloans-oarj5mfxkq-uc.a.run.app/api/model/predict/", loanPayload, {headers:{"token": "d8527109-7f36-41cf-8316-53d36916461c"}})
    if (res.data.Eligible == "Yes") {
        location.href = "/Eligible.html"
    }
    else if (res.data.Eligible == "No") {
        location.href = "/NotEligible.html"
    }
}