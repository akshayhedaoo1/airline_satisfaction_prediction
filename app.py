from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('home.html')  

@app.route("/predict", methods=['POST', 'GET'])
def predict():
     model = joblib.load('DecisionTree.pkl')
     if request.method=='POST':
          travel_class = request.form.get('travel_class')
          inflight_wifi = int(request.form.get('inflight_wifi'))
          time_convenient = int(request.form.get('time_convenient'))  
          online_booking =  int(request.form.get('online_booking'))
          online_boarding = int(request.form.get('online_boarding'))
          inflight_entertain =  int(request.form.get('inflight_entertain'))
          onboard_service =  int(request.form.get('onboard_service'))
          leg_room_service =  int(request.form.get('leg_room_service'))
          checkin_service =  int(request.form.get('checkin_service'))
          cleanliness =  int(request.form.get('cleanliness'))
          
          travel_class_ = 0
          if travel_class =='eco':
               travel_class_ = 0.0
          elif travel_class == 'eco_plus' :
               travel_class_ = 1.0
          elif travel_class == 'business':
               travel_class_ = 2.0


    
          arr1= np.array([travel_class_, inflight_wifi, time_convenient, online_booking, online_boarding, inflight_entertain, 
                    onboard_service, leg_room_service, checkin_service, cleanliness])
          pred = int(model.predict([arr1]))
          if pred == 0:       
               return render_template('home.html', prediction_text= 'Customer is Satisfied with our Service')
          else:
               return render_template('home.html', prediction_text= 'Customer is not Satisfied with our Service')
     return render_template('home.html')



if __name__ == "__main__":
    app.run()  
      