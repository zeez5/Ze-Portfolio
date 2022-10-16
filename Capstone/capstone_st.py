import streamlit as st
import pandas as pd
import pickle

# # Opening Intro text
st.write("# Predict Bike Rentals 🚴🏼‍♀️")
st.write("### Determine the scenario :")

# Specify if the day is a holiday
holiday = st.slider('Is the day a holiday? 🏖', min_value = 0, max_value = 1, value = 0, step = 1)

# Specify if the day is a working day
working_day =  st.slider('Is the day a work day? 💻 ', min_value = 0, max_value =1, value = 0, step = 1)

# Temperature of the day
temperature = st.slider('What is the temperature of the day in degree Celcius? 🔥 ', min_value = -8, max_value = 39, value = -8, step = 1)

# Temperature feeling of the day
temperature_feeling = st.slider("What is the 'feels like' temperature of the day in degree Celcius? 🌪", min_value=-16, max_value = 50, value = -16, step = 1)

# Humidity
humidity = st.slider("What is the humidity of the day? 💦", min_value = 0, max_value = 100, value = 0,  step = 1)

# Windspeed
windspeed = st.slider("What is the windspeed in mph? 💨 ", min_value = 1, max_value = 35, value = 1, step = 1)

# Season
season = st.selectbox("What is the season? (1: Spring, 2: Summer, 3: Fall, 4: Winter) 🌈", ('1','2','3','4'))

# Weather Situation
weather_sit = st.selectbox("What is the weather situation? (1: Clear, Few clouds, Partly cloudy; 2: Mist + Cloudy, Mist; 3: Light Snow, Light Rain + Scattered clouds 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog) ⛅️"
                        , ('1','2','3','4'))

# Creating a dataframe for user input values
my_dict = {
    "holiday" : holiday,
    "workingday": working_day,
    "temp": (temperature +8)/(39+8) ,
    "atemp": (temperature_feeling+16)/(50+16),
    "hum": humidity/100,
    "windspeed": windspeed/67,
    "season": season,
    "weathersit": weather_sit
        }

df = pd.DataFrame.from_dict([my_dict])
df = pd.get_dummies(df, columns= ['season','weathersit']).reindex(columns = ['holiday', 'workingday', 'temp', 'atemp', 'hum', 'windspeed',
       'season_1', 'season_2', 'season_3', 'season_4', 'weathersit_1','weathersit_2', 'weathersit_3'], fill_value = 0)

# button
if st.button("Click to Predict"):

    #load the model
    loaded_model = pickle.load(open('lm_model_prediction_capstone.sav','rb'))

    #Make Predictions for number of bike rentals
    pred = loaded_model.predict(df)[0]

    st.write(f"Predicted Bike Rentals: {pred:,.0f} units ")



                        

