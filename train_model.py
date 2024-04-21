import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import joblib

# Load the dataset
dataset = pd.read_excel("credit_rating.xls")

# Separate features (X) and target variable (y)
X = dataset.drop(columns=["Credit classification"])
y = dataset["Credit classification"]

# Identify categorical features
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

# Define preprocessing steps for categorical and numerical features
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numerical_transformer = MinMaxScaler()

# Get column indices for categorical features
categorical_indices = [X.columns.get_loc(col) for col in categorical_features]

# Get column indices for numerical features
numerical_indices = [i for i in range(len(X.columns)) if i not in categorical_indices]

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_indices),
        ('num', numerical_transformer, numerical_indices)
    ])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the classification model
classification_model = Pipeline(steps=[('preprocessor', preprocessor),
                                       ('classifier', LogisticRegression())])

# Fit the model
classification_model.fit(X_train, y_train)

# Save the trained model
joblib.dump(classification_model, "trained_model.pkl")
