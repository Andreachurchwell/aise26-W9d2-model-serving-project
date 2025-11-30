import sys
import time
import pandas as pd
import joblib

MODEL_PATH = "models/baseline.joblib"

def main():
    if len(sys.argv) != 3:
        print("Usage: python batch_infer.py data/input.csv data/predictions.csv")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    start = time.time()
    print(f"📥 Reading input CSV from: {input_path}")

    df = pd.read_csv(input_path)

    # Expecting columns x1 and x2
    if not {"x1", "x2"}.issubset(df.columns):
        raise ValueError("Input CSV must contain 'x1' and 'x2' columns")

    print("📦 Loading model...")
    model = joblib.load(MODEL_PATH)

    print("🤖 Running batch predictions...")
    X = df[["x1", "x2"]]
    probs = model.predict_proba(X)[:, 1]   # probability of class 1

    df["score"] = probs

    df.to_csv(output_path, index=False)
    elapsed = time.time() - start

    print(f"✅ Wrote predictions to: {output_path}")
    print(f"Rows processed: {len(df)}")
    print(f"Time taken: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()
