import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")
import pickle


def generateRandomData():
    np.random.seed(8965)
    # intializaing empty dataframe
    df = pd.DataFrame()
    # generating random data on the basis of Features defined above
    df['fever'] = np.random.uniform(98,104, (10000))
    df['fever'] = [round(x, 1) for x in df['fever']]
    df['bodyPain'] = np.random.randint(0,2, (10000))
    df['age'] = np.random.randint(1,100, (10000))
    df['runnyNose'] = np.random.randint(0,2, (10000))
    df['diffBreath'] = np.random.randint(-1,2, (10000))
    df['infectionProb'] = np.random.randint(0,2, (10000))
    return df

df = generateRandomData()

def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train, test = data_split(df, 0.2)
X_train = train[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()
X_test = train[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreath']].to_numpy()
Y_train = train[['infectionProb']].to_numpy().reshape(8000, -1)
Y_test = train[['infectionProb']].to_numpy().reshape(2000, -1)
clf = LogisticRegression()
clf.fit(X_train, Y_train)

file = open('model.pkl', 'wb')
pickle.dump(clf, file)



if __name__ == '__main__':
    pass
