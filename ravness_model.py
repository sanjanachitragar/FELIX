
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#import pickle
import librosa
import pandas as pd
import numpy as np


def model_predict():
    # Load the dataset
    dataset = pd.read_csv(r"C:\Users\Chetan\Downloads\projecttt\kaggledataset\features.csv")

    # Split the dataset into features (X) and labels (y)
    X = dataset.drop('labels', axis=1)
    y = dataset['labels']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize a random forest classifier
    rf_classifier = RandomForestClassifier()

    # Train the classifier on the training data
    rf_classifier.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = rf_classifier.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    #filename="ravness model.pkl"
    #pickle.dump(rf_classifier,open(filename,"wb"))


    def extract_features(audio_file):
        audio, sr = librosa.load(audio_file)
        # Extract MFCC features
        mfcc_features = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=19)
        
        # Transpose the feature matrix
        mfcc_features = mfcc_features.T
        
        # Convert the features to a DataFrame
        df = pd.DataFrame(mfcc_features)
        
        return mfcc_features

    # Load the audio file
    audio_file = r"C:\Users\Chetan\Downloads\projecttt\hackathon\output.wav"


    features_df= extract_features(audio_file)

    flattened_features = features_df.flatten()

    reshaped_features = flattened_features.reshape(-1,)

    # Select the first 20 attributes
    selected_features = reshaped_features[:20]

    df = pd.DataFrame(selected_features)

    return rf_classifier.predict([selected_features])

    

