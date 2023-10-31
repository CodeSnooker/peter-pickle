
import numpy as np
from flask import Flask, request, render_template
import pickle

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('./model19x11y.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()] 
    prediction = model.predict([data])
   #ok result_dict = {'A': round(prediction[0][0],2), 'B': round(prediction[0][1],2)}
    result_dict = {'CaSO4': round(prediction[0][0],2), 'CaCO3': round(prediction[0][1],2)\
                   , 'BaSO4': round(prediction[0][2],2), 'CaCO32': round(prediction[0][3],2)\
                       , 'SrSO4': round(prediction[0][4],2), 'CaSO4:2H2O': round(prediction[0][5],2)\
                           ,'FeS': round(prediction[0][6],2)\
                           , 'NaCl': round(prediction[0][7],2), 'SiO2': round(prediction[0][8],2)\
                               , 'FeCO3': round(prediction[0][9],2), 'ZnS': round(prediction[0][10],2)}

    return render_template('index.html', prediction_text=result_dict)
										


  #ok  return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(prediction))

 #   int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
 #   features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
 #   prediction = model.predict([features])  # features Must be in the form [[a, b]]

#    output = round(prediction[0], 2)

 #   return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output))
 #   

    


 #ok   data = [int(x) for x in request.form.values()] #Convert string inputs to float.
 
 #ok   prediction = model.predict([data])  # features Must be in the form [[a, b]]
 #ok   output = round(prediction[0], 2)
 #   results = prediction.tolist()

#ok    return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output))

   # results = prediction.tolist()  # Convert the prediction to a list

  #  return render_template('index.html', results=results)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)