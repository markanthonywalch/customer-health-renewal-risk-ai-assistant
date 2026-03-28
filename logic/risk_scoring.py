import pandas as pd

def calculate_risk(row):
    risk_score = 0
    reasons = []

    # Renewal proximity
    if row["days_to_renewal"] < 60:
        risk_score += 2
        reasons.append("Renewal is approaching")

    # Low utilization
    if row["license_utilization_percent"] < 50:
        risk_score += 2
        reasons.append("Low product utilization")

    # High support volume
    if row["support_tickets_last_90_days"] > 10:
        risk_score += 1
        reasons.append("High support ticket volume")

    # High severity issues
    if row["high_severity_tickets_last_90_days"] > 2:
        risk_score += 2
        reasons.append("Multiple high severity issues")

    # Low NPS
    if row["nps_score"] <= 5:
        risk_score += 2
        reasons.append("Low customer satisfaction (NPS)")

    # Low engagement
    if row["login_frequency_score"] < 40:
        risk_score += 1
        reasons.append("Low platform engagement")

    # Low training completion
    if row["training_completion_percent"] < 30:
        risk_score += 1
        reasons.append("Low training completion")

    # Open escalations
    if row["open_escalations"] > 2:
        risk_score += 2
        reasons.append("Active escalations")

    # Determine risk level
    if risk_score >= 7:
        risk_level = "High"
    elif risk_score >= 4:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return risk_level, ", ".join(reasons)


def run_risk_analysis(file_path):
    df = pd.read_csv(file_path)

    df[["risk_level", "risk_reasons"]] = df.apply(
        lambda row: pd.Series(calculate_risk(row)), axis=1
    )

    return df


if __name__ == "__main__":
    df = run_risk_analysis("sample_data/customer_health_data.csv")
    print(df[["account_name", "risk_level", "risk_reasons"]])
