const positiveNumberPattern = /^\d+$/

function validateGender() { 
    if(!loanPayload.gender || loanPayload.gender.length === 0) {
        document.getElementById("toast-body").innerHTML = "Gender is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    } 
}

function validatePropertyArea() {
    if(!loanPayload.property_area || loanPayload.property_area.length === 0) {
        document.getElementById("toast-body").innerHTML = "Please select a property area"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
}

function validateSelfEmployed() {
    if(!loanPayload.self_employed || loanPayload.self_employed.length === 0) {
        document.getElementById("toast-body").innerHTML = "Employment information is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
}

function validateEducationLevel() {
    if(!loanPayload.education_level || loanPayload.education_level.length === 0) {
        document.getElementById("toast-body").innerHTML = "Educational information is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
}

function validateMarried() {
    if(!loanPayload.married || loanPayload.married.length === 0) {
        document.getElementById("toast-body").innerHTML = "Marital information is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
}

function validateDependents() {
    if(!loanPayload.dependents || loanPayload.dependents.length === 0) {
        document.getElementById("toast-body").innerHTML = "Dependents information is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
    if (positiveNumberPattern.test(loanPayload.dependents) === false) {
        document.getElementById("toast-body").innerHTML = "dependents is invalid"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("invalid input")
    }
}

function validateIncome() {
    if(!loanPayload.income || loanPayload.income.length === 0) {
        document.getElementById("toast-body").innerHTML = "Income information is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
    if (positiveNumberPattern.test(loanPayload.income) === false) {
        document.getElementById("toast-body").innerHTML = "income is invalid"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("invalid input")
    }
}

function validateCoapplicantIncome() {
    if(!loanPayload.coapplicant_income || loanPayload.coapplicant_income.length === 0) {
        document.getElementById("toast-body").innerHTML = "Coapplicant information is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
    if (positiveNumberPattern.test(loanPayload.coapplicant_income) === false) {
        document.getElementById("toast-body").innerHTML = "coapplicant income is invalid"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("invalid input")
    }
}

function validateLoanAmount() {
    if(!loanPayload.loan_amount || loanPayload.loan_amount.length === 0) {
        document.getElementById("toast-body").innerHTML = "Loan amount is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
    if (positiveNumberPattern.test(loanPayload.loan_amount) === false) {
        document.getElementById("toast-body").innerHTML = "loan amount is invalid"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("invalid input")
    }
}

function validateLoanTerm() {
    if(!loanPayload.loan_term || loanPayload.loan_term.length === 0) {
        document.getElementById("toast-body").innerHTML = "Loan term is required"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("field is required")
    }
    if (positiveNumberPattern.test(loanPayload.loan_term) === false ) {
        document.getElementById("toast-body").innerHTML = "loan term is invalid"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("invalid input")
    }
    if (parseInt(loanPayload.loan_term) < 7 || parseInt(loanPayload.loan_term) > 360) {
        document.getElementById("toast-body").innerHTML = "loan term is minimum 7 days and maximum 360 days"
        $('.toast').toast({ delay: 2500 })
        $('.toast').toast('show')
        throw new Error("invalid input")
    }
}