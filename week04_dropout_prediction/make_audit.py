"""Reproduce the Week 4 classroom comparison from the downloaded UCI CSV."""

import hashlib
import json
import sys
import urllib.request
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score
from sklearn.model_selection import train_test_split


HERE = Path(__file__).resolve().parent
source = HERE / "uci697_source.csv"
if not source.exists():
    urllib.request.urlretrieve(
        "https://archive.ics.uci.edu/static/public/697/data.csv", source
    )
source_bytes = source.read_bytes()
data = pd.read_csv(source)
data = data.rename(
    columns={
        "Admission grade": "admission_grade",
        "Age at enrollment": "age",
        "Scholarship holder": "scholarship",
        "Tuition fees up to date": "tuition_paid",
        "Curricular units 1st sem (enrolled)": "sem1_enrolled",
        "Curricular units 1st sem (approved)": "sem1_passed",
        "Curricular units 1st sem (grade)": "sem1_grade",
    }
)
full_columns = [
    "admission_grade",
    "age",
    "scholarship",
    "tuition_paid",
    "sem1_enrolled",
    "sem1_passed",
    "sem1_grade",
]
early_columns = full_columns[:4]
y = (data["Target"] == "Dropout").astype(int)


def evaluate(columns):
    x_train, x_new, y_train, y_new = train_test_split(
        data[columns], y, test_size=0.2, random_state=42, stratify=y
    )
    model = RandomForestClassifier(
        n_estimators=100, random_state=42, class_weight="balanced"
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_new)
    baseline = [0] * len(y_new)
    examples = []
    for i in range(10):
        row = x_new.iloc[[i]]
        risk = float(model.predict_proba(row)[0, 1])
        examples.append(
            {
                "number": i + 1,
                "source_row_zero_based": int(row.index[0]),
                "age": int(data.loc[row.index[0], "age"]),
                "sem1_enrolled": int(data.loc[row.index[0], "sem1_enrolled"]),
                "sem1_passed": int(data.loc[row.index[0], "sem1_passed"]),
                "sem1_grade": float(data.loc[row.index[0], "sem1_grade"]),
                "risk_probability": risk,
                "risk_shown_percent": round(risk * 100),
                "suggested_action": "联系咨询" if risk >= 0.5 else "暂无行动",
                "actual_dropout": bool(y_new.iloc[i]),
            }
        )
    return {
        "columns": columns,
        "train_rows": len(x_train),
        "test_rows": len(x_new),
        "train_actual_dropout": int(y_train.sum()),
        "test_actual_dropout": int(y_new.sum()),
        "selected_input_missing_values": int(data[columns].isna().sum().sum()),
        "model_accuracy": float(accuracy_score(y_new, predictions)),
        "model_dropout_recall": float(recall_score(y_new, predictions)),
        "baseline_accuracy": float(accuracy_score(y_new, baseline)),
        "baseline_dropout_recall": float(recall_score(y_new, baseline)),
        "confusion_matrix_TN_FP_FN_TP": confusion_matrix(
            y_new, predictions, labels=[0, 1]
        ).ravel().tolist(),
        "feature_importance": sorted(
            [
                {"name": name, "importance": float(importance)}
                for name, importance in zip(columns, model.feature_importances_)
            ],
            key=lambda item: item["importance"],
            reverse=True,
        ),
        "first_ten_test_examples": examples,
    }


full = evaluate(full_columns)
early = evaluate(early_columns)
assert [round(full["model_accuracy"] * 100, 1), round(full["model_dropout_recall"] * 100, 1)] == [83.1, 74.6]
assert [round(early["model_accuracy"] * 100, 1), round(early["model_dropout_recall"] * 100, 1)] == [66.2, 61.6]
assert full["baseline_accuracy"] == early["baseline_accuracy"]
assert [item["source_row_zero_based"] for item in full["first_ten_test_examples"]] == [
    item["source_row_zero_based"] for item in early["first_ten_test_examples"]
]

audit = {
    "retrieved_for_audit_utc": datetime.now(timezone.utc).isoformat(),
    "source_url": "https://archive.ics.uci.edu/static/public/697/data.csv",
    "source_dataset_url": "https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success",
    "source_doi": "10.24432/C5MC89",
    "uci_metadata_last_updated": "Mon Feb 26 2024",
    "source_csv_bytes": len(source_bytes),
    "source_csv_sha256": hashlib.sha256(source_bytes).hexdigest(),
    "data_rows": len(data),
    "data_columns": len(data.columns),
    "all_data_missing_values": int(data.isna().sum().sum()),
    "target_counts": {str(k): int(v) for k, v in data["Target"].value_counts().items()},
    "versions": {
        "python": sys.version.split()[0],
        "pandas": version("pandas"),
        "numpy": version("numpy"),
        "scikit_learn": version("scikit-learn"),
        "scipy": version("scipy"),
        "ucimlrepo": version("ucimlrepo"),
    },
    "classroom_seven_inputs": full,
    "challenge_four_inputs": early,
    "change_accuracy_percentage_points": round(
        100 * (early["model_accuracy"] - full["model_accuracy"]), 3
    ),
    "change_dropout_recall_percentage_points": round(
        100 * (early["model_dropout_recall"] - full["model_dropout_recall"]), 3
    ),
}
(HERE / "comparison.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({
    "data_rows": audit["data_rows"],
    "target_counts": audit["target_counts"],
    "csv_sha256": audit["source_csv_sha256"],
    "seven": {
        "accuracy": full["model_accuracy"],
        "dropout_recall": full["model_dropout_recall"],
    },
    "four": {
        "accuracy": early["model_accuracy"],
        "dropout_recall": early["model_dropout_recall"],
    },
}, ensure_ascii=False, indent=2))
