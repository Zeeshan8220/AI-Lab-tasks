import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

file_path_train = r'D:\AI lab tasks\titanic\train.csv'
file_path_test = r'D:\AI lab tasks\titanic\test.csv'

train_data = pd.read_csv(file_path_train)
test_data = pd.read_csv(file_path_test)

print(train_data.head())
print(train_data.info())
print(train_data.describe())

imputer = SimpleImputer(strategy='mean')
train_data['Age'] = imputer.fit_transform(train_data[['Age']])
test_data['Age'] = imputer.transform(test_data[['Age']])

train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

label_encoder = LabelEncoder()
train_data['Sex'] = label_encoder.fit_transform(train_data['Sex'])
test_data['Sex'] = label_encoder.transform(test_data['Sex'])

train_data['Fare'] = train_data['Fare'].astype(float)
test_data['Fare'] = test_data['Fare'].astype(float)

X_train = train_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y_train = train_data['Survived']

X_test = test_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]

X_train_split, X_valid_split, y_train_split, y_valid_split = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_split = scaler.fit_transform(X_train_split)
X_valid_split = scaler.transform(X_valid_split)

log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train_split, y_train_split)
y_pred_log_reg = log_reg.predict(X_valid_split)
log_reg_accuracy = accuracy_score(y_valid_split, y_pred_log_reg)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_split, y_train_split)
y_pred_rf = rf_classifier.predict(X_valid_split)
rf_accuracy = accuracy_score(y_valid_split, y_pred_rf)

svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_split, y_train_split)
y_pred_svm = svm_classifier.predict(X_valid_split)
svm_accuracy = accuracy_score(y_valid_split, y_pred_svm)

print("\nLogistic Regression Accuracy:", log_reg_accuracy)
print("Random Forest Accuracy:", rf_accuracy)
print("SVM Accuracy:", svm_accuracy)

best_model = rf_classifier

X_test_scaled = scaler.transform(X_test)
y_test_pred = best_model.predict(X_test_scaled)

submission = pd.DataFrame({
    'PassengerId': test_data['PassengerId'],
    'Survived': y_test_pred
})

submission_file_path = r'D:\AI lab tasks\titanic\submission.csv'
submission.to_csv(submission_file_path, index=False)

print("\nSubmission file created successfully.")
