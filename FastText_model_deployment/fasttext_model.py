import ktrain

predictor = ktrain.load_predictor('toxic_fasttext')



def get_prediction(x):
    pred = predictor.predict([x])
    return pred[0]