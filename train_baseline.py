from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import joblib

# Make sure models/ folder exists
Path("models").mkdir(exist_ok=True)

# Generate a tiny synthetic binary classification dataset
X, y = make_classification(
    n_samples=500,
    n_features=2,       # we only want x1 and x2
    n_informative=2,    # both features are informative
    n_redundant=0,
    n_repeated=0,
    random_state=42
)

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "models/baseline.joblib")
print("✅ Saved baseline model to models/baseline.joblib")