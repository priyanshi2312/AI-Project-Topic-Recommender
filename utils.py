def print_header(title):
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def print_project(project):

    print(f"\n📌 Project Title : {project['title']}")
    print(f"📂 Domain        : {project['domain']}")
    print(f"⭐ Match Score   : {project['match_percentage']}%")
    print(f"🎓 Difficulty   : {project['difficulty']}")
    print(f"⏳ Duration      : {project['duration']}")
    print(f"🛠 Skills        : {project['skills']}")
    print(f"📝 Description   : {project['description']}")


def why_recommended(project, interests, skills, difficulty):

    print("\n💡 Why Recommended?")

    reasons = []

    if project["domain"].lower() in interests.lower():
        reasons.append(f"✔ Matches your interest in {project['domain']}")

    if project["difficulty"].lower() == difficulty.lower():
        reasons.append("✔ Matches your preferred difficulty")

    project_skills = [
        skill.strip().lower()
        for skill in project["skills"].split(",")
    ]

    user_skills = [
        skill.strip().lower()
        for skill in skills.split(",")
    ]

    for skill in user_skills:

        if skill in project_skills:

            reasons.append(f"✔ Uses your skill: {skill.title()}")

    if len(reasons) == 0:
        reasons.append("✔ Similar keywords matched using NLP")

    for reason in reasons:
        print(reason)


def skill_gap(project, skills):

    print("\n📚 Skill Gap Analysis")

    project_skills = [
        skill.strip()
        for skill in project["skills"].split(",")
    ]

    user_skills = [
        skill.strip().lower()
        for skill in skills.split(",")
    ]

    missing = []

    for skill in project_skills:

        if skill.lower() not in user_skills:
            missing.append(skill)

    if missing:

        print("Recommended skills to learn:")

        for skill in missing:
            print(f"❌ {skill}")

    else:
        print("✅ You already have all required skills!")


def learning_resources(project):

    print("\n📖 Suggested Learning Path")

    resources = {
        "Python": "Python Official Documentation",
        "Pandas": "Pandas Documentation",
        "NumPy": "NumPy Documentation",
        "Scikit-learn": "Scikit-learn Documentation",
        "TensorFlow": "TensorFlow Tutorials",
        "PyTorch": "PyTorch Tutorials",
        "OpenCV": "OpenCV Documentation",
        "NLTK": "NLTK Book",
        "spaCy": "spaCy Documentation",
        "Flask": "Flask Documentation",
        "SQL": "W3Schools SQL Tutorial"
    }

    skills = [
        skill.strip()
        for skill in project["skills"].split(",")
    ]

    for skill in skills:

        if skill in resources:
            print(f"📘 {skill} → {resources[skill]}")


def save_recommendations(
    recommendations,
    filename="recommended_projects.csv"
):

    recommendations.to_csv(
        filename,
        index=False
    )

    print(f"\n✅ Recommendations saved as '{filename}'")