import ktrain

predictor = ktrain.load_predictor('distillbert')



def get_prediction(x):
    sent = predictor.predict([x])
    return sent[0]