def generate_account_summary(row):
    summary = f"""
Account Summary for {row['account_name']}

{row['account_name']} is currently rated as {row['risk_level']} renewal risk.

Key health indicators:
- ARR: ${row['arr']:,}
- Renewal in: {row['days_to_renewal']} days
- License utilization: {row['license_utilization_percent']}%
- Support tickets (last 90 days): {row['support_tickets_last_90_days']}
- High severity tickets: {row['high_severity_tickets_last_90_days']}
- NPS score: {row['nps_score']}
- Login frequency score: {row['login_frequency_score']}
- Training completion: {row['training_completion_percent']}%
- Open escalations: {row['open_escalations']}

Primary risk drivers:
{row['risk_reasons']}

Recommended next steps:
{generate_next_best_actions(row)}
"""
    return summary.strip()


def generate_next_best_actions(row):
    actions = []

    if row["license_utilization_percent"] < 50:
        actions.append("- Schedule a product adoption review to improve utilization.")

    if row["support_tickets_last_90_days"] > 10:
        actions.append("- Review support case trends and unresolved issues with Support leadership.")

    if row["high_severity_tickets_last_90_days"] > 2:
        actions.append("- Escalate product stability concerns and confirm mitigation plan.")

    if row["nps_score"] <= 5:
        actions.append("- Conduct a customer sentiment check-in with the account team.")

    if row["days_to_renewal"] < 60:
        actions.append("- Launch a renewal readiness plan immediately.")

    if row["training_completion_percent"] < 30:
        actions.append("- Recommend targeted training to improve user adoption.")

    if row["open_escalations"] > 2:
        actions.append("- Resolve active escalations before renewal discussions.")

    if not actions:
        actions.append("- Maintain current engagement cadence and monitor account health.")

    return "\n".join(actions)


def generate_email_draft(row):
    return f"""
Subject: Partnership Check-In and Next Steps

Hi team,

I wanted to reach out regarding your account and upcoming renewal timeline.

Based on recent activity, we would like to schedule time to review your current usage, discuss any open challenges, and ensure your team is getting full value from the platform.

Here are a few areas we’d like to cover:
- Current product utilization
- Open support items
- Adoption and training opportunities
- Renewal planning

Please let us know a good time to connect over the next week.

Best,  
{row['csm_name']}
""".strip()
