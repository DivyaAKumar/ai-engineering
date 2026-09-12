import pickle 
import pandas as pd

#import ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)
#getting class labels from model
class_labels = model.classes_.tolist()

#ML FLOW MODEL ADJUSTRY
MODEL_VERSION = '1.0,0'
def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])
    #predicted class
    predicted_class = model.predict(df)[0]

    #getting probabs for all the classes
    probab = model.predict_proba(df)[0]
    confidence = max(probab)

    #create mapping: {class_name:probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probab)))

    return{
        'predicted category': predicted_class,
        'confidence': round(confidence,4),
        'class_probability': class_probs
    }
    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]
    return output