# Olympiacos FC 2023–2024: From Group Stage Struggles to Conference League Champions

👉 Full analysis available in:
- notebooks/analysis.ipynb
- notebooks/players_analysis.ipynb

---

## 📊 Project Overview

In this project, I analyzed Olympiacos’ 2023–2024 season, focusing on their Conference League-winning campaign.

The goal was to understand how the team performed across domestic and European competitions, how performance evolved during the season, and which players played a key role in the team’s success.

---

## 🎯 What I wanted to find out

- How does performance differ between Greece and Europe?
- How important is home advantage?
- Did the team improve in knockout matches?
- Was there a key turning point in the season?
- Which players had the biggest impact?

---

## 🛠️ Tools I used

- Python (pandas, matplotlib)
- Jupyter Notebook
- Git & GitHub

---

## 📂 Dataset

The project uses two main datasets:

### Match Data
- Super League Greece matches
- UEFA Conference League matches  
Includes:
- date, competition, opponent
- venue (home/away)
- goals scored and conceded
- match stage

### Player Data
- UEFA List A squad (knockout phase)
- Includes:
  - appearances
  - minutes played
  - goals
  - assists

Player stats are simplified and used to support high-level analysis of contributions.

---

## 📈 Key Analysis

### Greece vs Europe

- Olympiacos achieved the same win rate (66.7%) in both competitions.
- The team scored more goals domestically.
- Defensive performance was stronger in Greece.
- European matches were more challenging and less predictable.

---

### Home vs Away

- Strong home performance in both competitions.
- European away matches were the most difficult.
- Domestic away performance remained relatively stable.

---

### Group Stage vs Knockout

- Group stage was inconsistent (50% win rate).
- Knockout phase showed clear improvement (75% win rate).
- The team became more defensively solid and efficient.
- Best performances occurred in later stages of the competition.

---

### Key Match (Turning Point)

- The 6–1 win against Maccabi Tel Aviv was the turning point.
- After losing 4–1 in the first leg, Olympiacos made a major comeback.
- This result shifted momentum and confidence.
- The team continued with strong performances and won the final.

---

### Player Analysis

- El Kaabi was the standout player, leading in goals and overall contribution.
- Fortounis combined scoring and creativity through goals and assists.
- Podence contributed consistently in attack.
- Player contribution was concentrated among a small core group.

---

### Key Players by Position

| Position   | Player      | Role |
|-----------|------------|------|
| Goalkeeper | Tzolakis   | Stability and key saves in knockout matches |
| Defender   | Rodinei    | Defensive consistency and attacking support |
| Midfielder | Fortounis  | Creativity, goals and assists |
| Forward    | El Kaabi   | Top scorer and decisive performances |

---

## 🧠 Key Takeaways

- Olympiacos achieved equal success in Greece and Europe, but in different ways.
- Domestic matches were more stable and defensively strong.
- European matches required adaptability and resilience.
- Performance improved significantly in knockout stages.
- Success was driven by both team structure and key individual performances.

---

## 📌 Final Thoughts

This season shows how a team can combine domestic consistency with European resilience.

Olympiacos improved over time, adapted to stronger competition, and delivered in key moments — ultimately winning the Conference League.

---

## 📎 Project Structure

olympiacos-greece-vs-europe-analysis/
│
├── data/
│   ├── raw/
│   │   ├── olympiacos_matches_raw.csv
│   │   └── olympiacos_players_2023_2024.csv
│   └── cleaned/
│       └── olympiacos_matches_clean.csv
│
├── notebooks/
│   ├── analysis.ipynb
│   └── players_analysis.ipynb
│
├── src/
│   └── build_dataset.py
│
├── README.md
└── requirements.txt

---

## 🚀 Future Improvements

- Extend analysis to multiple seasons
- Include Greek Cup matches
- Add more detailed player statistics
- Build an interactive dashboard (Tableau / Power BI)

---

## 👤 Author

Christos Patitis
