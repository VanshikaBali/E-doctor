import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('savedModels/Diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open('savedModels/Heart.sav', 'rb'))
parkinsons_model = pickle.load(open('savedModels/Parkinsons.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                          icons=['activity', 'heart', 'person'],
                          default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value='0')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    # Validate input data
    try:
        Pregnancies = float(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)
    except ValueError:
        st.error("Please enter valid numeric values for all fields.")
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        with st.spinner('Processing...'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        
        st.success(diab_diagnosis)
    
    # Diabetes Parameter Table - Only shown on Diabetes page
    st.markdown("""
    <h3 style="color: red;">Parameter Information Guide</h3>
    <table style="width: 100%; border-collapse: collapse;">
       <thead>
            <tr className="bg-orange-600">
              <th className="border border-orange-400 p-3 text-white text-left">Parameter</th>
              <th className="border border-orange-400 p-3 text-white text-left">Full Form</th>
              <th className="border border-orange-400 p-3 text-white text-left">Normal Range</th>
              <th className="border border-orange-400 p-3 text-white text-left">Description</th>
            </tr>
          </thead>
          <tbody>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Pregnancies</td>
              <td className="border border-orange-400 p-3 text-white">Number of Pregnancies</td>
              <td className="border border-orange-400 p-3 text-white">0-20</td>
              <td className="border border-orange-400 p-3 text-white">Number of times pregnant</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Glucose</td>
              <td className="border border-orange-400 p-3 text-white">Plasma Glucose Concentration</td>
              <td className="border border-orange-400 p-3 text-white">0-200 mg/dL</td>
              <td className="border border-orange-400 p-3 text-white">Blood glucose level after 2 hours in oral glucose tolerance test</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Blood Pressure</td>
              <td className="border border-orange-400 p-3 text-white">Diastolic Blood Pressure</td>
              <td className="border border-orange-400 p-3 text-white">0-125 mm Hg</td>
              <td className="border border-orange-400 p-3 text-white">Diastolic blood pressure (mm Hg)</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Skin Thickness</td>
              <td className="border border-orange-400 p-3 text-white">Triceps Skin Fold Thickness</td>
              <td className="border border-orange-400 p-3 text-white">0.1-100 mm</td>
              <td className="border border-orange-400 p-3 text-white">Triceps skin fold thickness (mm)</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Insulin</td>
              <td className="border border-orange-400 p-3 text-white">2-Hour Serum Insulin</td>
              <td className="border border-orange-400 p-3 text-white">16-866 mU/L</td>
              <td className="border border-orange-400 p-3 text-white">2-Hour serum insulin (mu U/ml)</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">BMI</td>
              <td className="border border-orange-400 p-3 text-white">Body Mass Index</td>
              <td className="border border-orange-400 p-3 text-white">10.5-74.9</td>
              <td className="border border-orange-400 p-3 text-white">Weight in kg/(height in m)²</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">DPF</td>
              <td className="border border-orange-400 p-3 text-white">Diabetes Pedigree Function</td>
              <td className="border border-orange-400 p-3 text-white">0.078-3.00</td>
              <td className="border border-orange-400 p-3 text-white">Diabetes pedigree function (hereditary factor)</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Age</td>
              <td className="border border-orange-400 p-3 text-white">Age in Years</td>
              <td className="border border-orange-400 p-3 text-white">18-81</td>
              <td className="border border-orange-400 p-3 text-white">Age of the person in years</td>
            </tr>
          </tbody>
    </table>
    """, unsafe_allow_html=True)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Gender')
    
    with col3:
        cp = st.text_input('Chest Pain types')
    
    with col1:
        trestbps = st.text_input('Resting BP')
    
    with col2:
        chol = st.text_input('Serum Choles.')
    
    with col3:
        fbs = st.text_input('FBS')
    
    with col1:
        restecg = st.text_input('Restecg')
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    
    with col3:
        exang = st.text_input('EIA')
    
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    
    with col3:
        ca = st.text_input('Major vessels of Fourosopy')
    
    with col1:
        thal = st.text_input('Thal')
        
    # Validate input data
    try:
        age = float(age)
        sex = int(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = int(ca)
        thal = int(thal)
    except ValueError:
        st.error("Please fill the values according to your Stress test, Blood Panel test, and Coronary Angiography test to get valid output ")
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        with st.spinner('Processing...'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
            
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'
        
        st.success(heart_diagnosis)
        
    # Heart Disease Parameter Table - Only shown on Heart Disease page
    st.markdown("""
    <h3 style="color: red;">Heart Disease Parameter Information Guide</h3>
    <table style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr className="bg-orange-600">
              <th className="border border-orange-400 p-3 text-white text-left">Parameter</th>
              <th className="border border-orange-400 p-3 text-white text-left">Full Form</th>
              <th className="border border-orange-400 p-3 text-white text-left">Normal Range</th>
              <th className="border border-orange-400 p-3 text-white text-left">Description</th>
            </tr>
        </thead>
        <tbody>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Age</td>
              <td className="border border-orange-400 p-3 text-white">Age in Years</td>
              <td className="border border-orange-400 p-3 text-white">18-81</td>
              <td className="border border-orange-400 p-3 text-white">Age of the person in years</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Gender</td>
              <td className="border border-orange-400 p-3 text-white">Gender (1 = Male, 0 = Female)</td>
              <td className="border border-orange-400 p-3 text-white">1 or 0</td>
              <td className="border border-orange-400 p-3 text-white">Gender of the person (Male or Female)</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">CP</td>
              <td className="border border-orange-400 p-3 text-white">Chest Pain Types</td>
              <td className="border border-orange-400 p-3 text-white">0-3</td>
              <td className="border border-orange-400 p-3 text-white">Type of chest pain experienced</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Trestbps</td>
              <td className="border border-orange-400 p-3 text-white">Resting Blood Pressure</td>
              <td className="border border-orange-400 p-3 text-white">90-180 mm Hg</td>
              <td className="border border-orange-400 p-3 text-white">Resting blood pressure in mm Hg</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Chol</td>
              <td className="border border-orange-400 p-3 text-white">Serum Cholesterol</td>
              <td className="border border-orange-400 p-3 text-white">125-564 mg/dl</td>
              <td className="border border-orange-400 p-3 text-white">Cholesterol in mg/dl</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Fbs</td>
              <td className="border border-orange-400 p-3 text-white">Fasting Blood Sugar</td>
              <td className="border border-orange-400 p-3 text-white">&gt; 120 mg/dl</td>
              <td className="border border-orange-400 p-3 text-white">1 = true, 0 = false</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Restecg</td>
              <td className="border border-orange-400 p-3 text-white">Resting Electrocardiographic results</td>
              <<td className="border border-orange-400 p-3 text-white">0-2</td>
              <td className="border border-orange-400 p-3 text-white">Electrocardiographic results (0 = normal, 1 = having ST-T wave abnormality)</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Thalach</td>
              <td className="border border-orange-400 p-3 text-white">Maximum Heart Rate Achieved</td>
              <td className="border border-orange-400 p-3 text-white">71-202 bpm</td>
              <td className="border border-orange-400 p-3 text-white">Maximum heart rate in beats per minute</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Exang</td>
              <td className="border border-orange-400 p-3 text-white">Exercise Induced Angina</td>
              <td className="border border-orange-400 p-3 text-white">1 = yes, 0 = no</td>
              <td className="border border-orange-400 p-3 text-white">Exercise-induced chest pain</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">Oldpeak</td>
              <td className="border border-orange-400 p-3 text-white">ST depression induced by exercise relative to rest</td>
              <td className="border border-orange-400 p-3 text-white">0-6.2</td>
              <td className="border border-orange-400 p-3 text-white">ST depression during exercise</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Slope</td>
              <td className="border border-orange-400 p-3 text-white">Slope of the peak exercise ST segment</td>
              <td className="border border-orange-400 p-3 text-white">0-2</td>
              <td className="border border-orange-400 p-3 text-white">Slope of the ST segment during peak exercise</td>
            </tr>
            <tr className="bg-gray-800">
              <td className="border border-orange-400 p-3 text-white">CA</td>
              <td className="border border-orange-400 p-3 text-white">Major vessels colored by fluoroscopy</td>
              <td className="border border-orange-400 p-3 text-white">0-3</td>
              <td className="border border-orange-400 p-3 text-white">Number of major vessels (0-3) colored by fluoroscopy</td>
            </tr>
            <tr className="bg-gray-900">
              <td className="border border-orange-400 p-3 text-white">Thal</td>
              <td className="border border-orange-400 p-3 text-white">Thalassemia</td>
              <td className="border border-orange-400 p-3 text-white">0 = normal, 1 = fixed defect, 2 = reversible defect</td>
              <td className="border border-orange-400 p-3 text-white">Thalassemia type</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

# Parkinson's Prediction Page
if (selected == 'Parkinsons Prediction'):
    # page title
    st.title('Parkinsons Prediction using ML')
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col3:
        RAP = st.text_input('MDVP:RAP')
        
    with col1:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col2:
        DDP = st.text_input('Jitter:DDP')
        
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA = st.text_input('Shimmer:DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col1:
        spread1 = st.text_input('spread1')
        
    with col2:
        spread2 = st.text_input('spread2')
        
    with col3:
        D2 = st.text_input('D2')
        
    with col1:
        PPE = st.text_input('PPE')
        
    # Validate input data
    try:
        features = [float(val) for val in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, 
                                         Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, 
                                         RPDE, DFA, spread1, spread2, D2, PPE]]
    except ValueError:
        st.error("Please fill all numerical vlaues according to your MDVP test, Speech signal processing test, Pitch Spread test to get valid outputs.")
        features = None
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        with st.spinner('Processing...'):
            if features:
                parkinsons_prediction = parkinsons_model.predict([features])
                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"
                
                st.success(parkinsons_diagnosis)
            else:
                st.error("Please fill all numerical vlaues")
    
    st.markdown("""
<h3 style="color: red;">Parkinson's Disease Parameter Information Guide</h3>
<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr className="bg-orange-600">
          <th className="border border-orange-400 p-3 text-white text-left">Parameter</th>
          <th className="border border-orange-400 p-3 text-white text-left">Full Form</th>
          <th className="border border-orange-400 p-3 text-white text-left">Normal Range</th>
          <th className="border border-orange-400 p-3 text-white text-left">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr className="bg-gray-900">
          <td className="border border-orange-400 p-3 text-white">MDVP:Fo(Hz)</td>
          <td className="border border-orange-400 p-3 text-white">Average Vocal Fundamental Frequency</td>
          <td className="border border-orange-400 p-3 text-white">85–255 Hz</td>
          <td className="border border-orange-400 p-3 text-white">Average frequency of vocal cord vibration</td>
        </tr>
        <tr className="bg-gray-800">
          <td className="border border-orange-400 p-3 text-white">MDVP:Fhi(Hz)</td>
          <td className="border border-orange-400 p-3 text-white">Maximum Vocal Fundamental Frequency</td>
          <td className="border border-orange-400 p-3 text-white">110–300 Hz</td>
          <td className="border border-orange-400 p-3 text-white">Highest frequency of vocal cord vibration</td>
        </tr>
        <tr className="bg-gray-900">
          <td className="border border-orange-400 p-3 text-white">MDVP:Flo(Hz)</td>
          <td className="border border-orange-400 p-3 text-white">Minimum Vocal Fundamental Frequency</td>
          <td className="border border-orange-400 p-3 text-white">75–200 Hz</td>
          <td className="border border-orange-400 p-3 text-white">Lowest frequency of vocal cord vibration</td>
        </tr>
        <tr className="bg-gray-800">
          <td className="border border-orange-400 p-3 text-white">MDVP:Jitter(%)</td>
          <td className="border border-orange-400 p-3 text-white">Frequency Perturbation Percentage</td>
          <td className="border border-orange-400 p-3 text-white">0.01–1.5%</td>
          <td className="border border-orange-400 p-3 text-white">Variation in fundamental frequency</td>
        </tr>
        <tr className="bg-gray-800">
        <td className="border border-orange-400 p-3 text-white">Jitter(ABS)</td>
        <td className="border border-orange-400 p-3 text-white">Absolute variation in pitch from period to period</td>
        <td className="border border-orange-400 p-3 text-white">0.01–0.2 Hz</td>
        <td className="border border-orange-400 p-3 text-white">A measure of the frequency instability of the signal</td>
        </tr>
        <tr className="bg-gray-800">
        <td className="border border-orange-400 p-3 text-white">RAP</td>
        <td className="border border-orange-400 p-3 text-white">Relative Average Perturbation</td>
        <td className="border border-orange-400 p-3 text-white">0.01–0.5%</td>
        <td className="border border-orange-400 p-3 text-white">Measures the variation in pitch between consecutive periods relative to the average pitch</td>
        </tr>
        <tr className="bg-gray-800">
        <td className="border border-orange-400 p-3 text-white">PPQ</td>
        <td className="border border-orange-400 p-3 text-white">Period Perturbation Quotient</td>
        <td className="border border-orange-400 p-3 text-white">0.01–0.6%</td>
        <td className="border border-orange-400 p-3 text-white">Measures the variation in the period (time duration) between consecutive speech cycles</td>
        </tr>
        <tr className="bg-gray-800">
        <td className="border border-orange-400 p-3 text-white">DDP</td>
        <td className="border border-orange-400 p-3 text-white">Differential Duration Perturbation</td>
        <td className="border border-orange-400 p-3 text-white">0.02–1.0%</td>
        <td className="border border-orange-400 p-3 text-white">Measures the variation in duration between consecutive speech cycles</td>
        </tr>
        <!-- Add similar rows for each parameter with relevant normal ranges -->
        <tr className="bg-gray-900">
          <td className="border border-orange-400 p-3 text-white">PPE</td>
          <td className="border border-orange-400 p-3 text-white">Pitch Period Entropy</td>
          <td className="border border-orange-400 p-3 text-white">0–2.5</td>
          <td className="border border-orange-400 p-3 text-white">Measure of fundamental frequency variation</td>
        </tr>
    </tbody>
</table>
""", unsafe_allow_html=True)

