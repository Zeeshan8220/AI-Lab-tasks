import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

file_path = r'D:\AI lab tasks\gender_submission.csv'
data = pd.read_csv(file_path)

first_rows = data.head()
dataset_info = data.info()
summary_stats = data.describe()
missing_values = data.isnull().sum()
columns = data.columns
dataset_shape = data.shape

print("First 5 rows:\n", first_rows)
print("\nDataset Information:")
print(dataset_info)
print("\nSummary Statistics:\n", summary_stats)
print("\nMissing Values:\n", missing_values)
print("\nColumns:", columns)
print("\nShape:", dataset_shape)


data = data.dropna(subset=['Survived'])

data = data.fillna(data.mean())  

data = pd.get_dummies(data, drop_first=True)

X = data.drop('Survived', axis=1)  
y = data['Survived']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm_classifier = SVC(kernel='linear')  
svm_classifier.fit(X_train, y_train)

y_pred = svm_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

