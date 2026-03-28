# Customer Health & Renewal Risk AI Assistant

AI-powered assistant designed to help Customer Success Managers (CSMs) analyze account health, predict renewal risk, and take proactive action to reduce churn and drive expansion.

---

## 🚀 Overview

Enterprise customer success teams manage hundreds of accounts, but lack scalable ways to identify which customers are at risk and what actions to take.

This project simulates an AI-driven system that:

- Aggregates customer health signals
- Identifies renewal risk
- Explains *why* an account is at risk
- Recommends next best actions
- Generates customer-ready outreach

---

## 🎯 Problem

CSMs today rely on fragmented data across systems (CRM, support, product usage, NPS), making it difficult to:

- Prioritize high-risk accounts
- Understand root causes of churn risk
- Take timely, informed action before renewal

This results in:
- Missed renewal risks
- Reactive engagement
- Lost expansion opportunities

---

## 💡 Solution

This assistant combines structured customer data with AI to:

1. Evaluate account health using key signals
2. Identify renewal risk levels (Low / Medium / High)
3. Generate human-readable summaries of account status
4. Recommend targeted actions for CSMs
5. Draft customer outreach and internal briefs

---

## 🧩 Key Features (Planned)

- 📊 Customer Health Scoring Engine  
- ⚠️ Renewal Risk Classification  
- 🧠 AI-Generated Account Summaries  
- 🎯 Next Best Action Recommendations  
- ✉️ AI-Generated Email Drafts  
- 📈 Signal-based insights (usage, support, engagement, NPS)

---

## 🏗️ System Design (High-Level)

Inputs:
- Account data (ARR, renewal timing, usage, support activity)
- Customer engagement signals
- Product adoption metrics

Processing:
- Rule-based risk scoring
- AI summarization and reasoning

Outputs:
- Risk level (Low / Medium / High)
- Key risk drivers
- Recommended actions
- Generated communication drafts

---

## 📊 Example Signals Used

- Days to renewal
- License utilization %
- Support ticket volume (last 90 days)
- High severity support cases
- Product adoption score
- NPS / customer sentiment
- Login frequency / engagement
- Training completion %

---

## 🧠 Role of AI

AI is used to:

- Translate structured data into clear insights
- Explain risk in natural language
- Recommend actions based on patterns
- Generate customer-facing communication

---

## 📏 Success Metrics

- Reduction in at-risk renewals
- Increased proactive engagement by CSMs
- Improved customer health scores
- Reduction in time to identify risk
- Increased expansion / upsell opportunities

---

## ⚠️ Risks & Considerations

- False positives in risk classification
- Incomplete or stale data inputs
- Over-reliance on AI recommendations
- Need for human validation before outreach

---

## 🔮 Future Enhancements

- Integration with CRM (Salesforce, HubSpot)
- Real-time data ingestion
- Multi-agent workflows (CSM + Sales + Support)
- Predictive modeling for churn probability
- Dashboard + portfolio-level insights

---

## 🛠️ Tech Stack (Planned)

- Python (data processing)
- Pandas (data handling)
- Streamlit (UI)
- OpenAI API (AI generation)
- CSV / mock dataset (initial version)

---

## 📌 Status

🚧 In Progress — Initial version focused on building core workflow with mock data and AI-generated insights.
