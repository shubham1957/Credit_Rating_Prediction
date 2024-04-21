from flask import render_template, request
from app import app
from .forms import CreditForm
from .model import load_model, predict_credit_classification

# Load the trained model
model = load_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CreditForm()
    if form.validate_on_submit():
        data = {
            'CHK_ACCT': form.CHK_ACCT.data,
            'Duration': form.Duration.data,
            'History': form.History.data,
            'Purpose_of_credit': form.Purpose_of_credit.data,
            'Credit_Amount': form.Credit_Amount.data,
            'Balance_in_Savings_A_C': form.Balance_in_Savings_A_C.data,
            'Employment': form.Employment.data,
            'Install_rate': form.Install_rate.data,
            'Marital_status': form.Marital_status.data,
            'Co_applicant': form.Co_applicant.data,
            'Present_Resident': form.Present_Resident.data,
            'Real_Estate': form.Real_Estate.data,
            'Age': form.Age.data,
            'Other_installment': form.Other_installment.data,
            'Residence': form.Residence.data,
            'Num_Credits': form.Num_Credits.data,
            'Job': form.Job.data,
            'No_dependents': form.No_dependents.data,
            'Phone': form.Phone.data,
            'Foreign': form.Foreign.data
        }
        # Perform prediction using the loaded model and input data
        prediction = predict_credit_classification(model, [list(data.values())])
        return render_template('result.html', prediction=prediction)
    return render_template('index.html', form=form)