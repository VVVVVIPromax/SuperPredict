import numpy as np
import pandas as pd
import os

# --- Constants ---
DATA_FILE = "EuroHistory.csv"
NUMBER_COLUMNS = ["A", "B", "C", "D", "E", "F", "G"]
LOOK_BACK = 200
MAX_HISTORY_SIZE = 3000

history_data = []

def load_history():
    global history_data
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE, usecols=NUMBER_COLUMNS)
        df.iloc[:, :5] = np.sort(df.iloc[:, :5].values, axis=1)
        df.iloc[:, 5:] = np.sort(df.iloc[:, 5:].values, axis=1)
        history_data = df.values.tolist()
        print(f"Loaded {len(history_data)} historical draws from '{DATA_FILE}'.")
    else:
        history_data = []
        print(f"File '{DATA_FILE}' not found.")

def save_history():
    df = pd.DataFrame(history_data, columns=NUMBER_COLUMNS)
    df.iloc[:, :5] = np.sort(df.iloc[:, :5].values, axis=1)
    df.iloc[:, 5:] = np.sort(df.iloc[:, 5:].values, axis=1)
    df.to_csv(DATA_FILE, index=False)
    print(f"Historical data saved to '{DATA_FILE}'.")

# --- MODEL TRAINING PLACEHOLDER ---
def train_models_in_parallel():
    # Intellectual Property - TOP SECRET
    print("Model training is restricted and not available in this public version.")
    return True

# --- MODEL PREDICTION PLACEHOLDER ---
def generate_numbers():
    # Intellectual Property - TOP SECRET
    print("Prediction logic is restricted in this public release.")
    return [0, 0, 0, 0, 0], [0, 0], [0, 0, 0, 0, 0], [0, 0]  # Dummy values

def main():
    load_history()

    if not train_models_in_parallel():
        print("Model training failed. Terminating program.")
        return

    predicted_main, predicted_stars, cdm_main, cdm_stars = generate_numbers()
    if predicted_main is None:
        print("Could not generate predictions.")
        return

    print("\n--- XGBoost Ensemble Prediction Results (Dummy) ---")
    print(f"XGBoost Predicted Main: {predicted_main}")
    print(f"XGBoost Predicted Stars: {predicted_stars}")
    print(f"[CDM Fallback Main ]: {cdm_main}")
    print(f"[CDM Fallback Stars]: {cdm_stars}")

    while True:
        try:
            user_input = input("Enter the actual results (5 Main + 2 Stars, separated by spaces): ")
            true_result = list(map(int, user_input.strip().split()))
            if len(true_result) != 7:
                print("⚠️ Please enter exactly 7 numbers (5 main, 2 stars). Try again.\n")
                continue
            break
        except ValueError:
            print("⚠️ Invalid input. Please enter only integers separated by spaces.\n")

    true_main = sorted(true_result[:5])
    true_stars = sorted(true_result[5:])

    xgb_main_matches = len(set(predicted_main).intersection(set(true_main)))
    xgb_star_matches = len(set(predicted_stars).intersection(set(true_stars)))
    cdm_main_matches = len(set(cdm_main).intersection(set(true_main)))
    cdm_star_matches = len(set(cdm_stars).intersection(set(true_stars)))

    print("\n--- Hit Count for This Draw ---")
    print(f"(XGBoost) Main matched: {xgb_main_matches} / 5")
    print(f"(XGBoost) Stars matched: {xgb_star_matches} / 2")
    print(f"(CDM) Main matched: {cdm_main_matches} / 5")
    print(f"(CDM) Stars matched: {cdm_star_matches} / 2")

    history_data.append(true_main + true_stars)
    if len(history_data) > MAX_HISTORY_SIZE:
        history_data.pop(0)
    save_history()

if __name__ == "__main__":
    main()
