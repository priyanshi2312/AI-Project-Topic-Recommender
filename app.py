from recommender import ProjectTopicRecommender
from utils import (
    print_header,
    print_project,
    why_recommended,
    skill_gap,
    learning_resources,
    save_recommendations
)


def main():

    print_header("🤖 AI PROJECT TOPIC RECOMMENDER")

    print("\nWelcome! Let's find the best AI project for you.\n")

    # ------------------------------
    # Basic Details
    # ------------------------------

    name = input("👤 Enter your Name: ").strip()
    branch = input("🏫 Enter your Branch (CSE/IT/ECE etc.): ").strip()
    year = input("📚 Enter your Year (1st/2nd/3rd/4th): ").strip()

    # ------------------------------
    # Interest Selection
    # ------------------------------

    interest_options = [
        "Artificial Intelligence",
        "Machine Learning",
        "Natural Language Processing",
        "Computer Vision",
        "Data Science",
        "Healthcare",
        "Finance",
        "Education",
        "Agriculture",
        "Cybersecurity",
        "Generative AI",
        "IoT"
    ]

    print("\n❤️ Select Your Interests")

    for i, option in enumerate(interest_options, start=1):
        print(f"{i}. {option}")

    choices = input("\nEnter numbers separated by commas: ")

    selected_interests = []

    for choice in choices.split(","):

        choice = choice.strip()

        if choice.isdigit():

            index = int(choice) - 1

            if 0 <= index < len(interest_options):
                selected_interests.append(interest_options[index])

    interests = ", ".join(selected_interests)

    # ------------------------------
    # Skills Selection
    # ------------------------------

    skill_options = [
        "Python",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "OpenCV",
        "NLTK",
        "spaCy",
        "Flask",
        "SQL"
    ]

    print("\n💻 Select Your Skills")

    for i, skill in enumerate(skill_options, start=1):
        print(f"{i}. {skill}")

    choices = input("\nEnter numbers separated by commas: ")

    selected_skills = []

    for choice in choices.split(","):

        choice = choice.strip()

        if choice.isdigit():

            index = int(choice) - 1

            if 0 <= index < len(skill_options):
                selected_skills.append(skill_options[index])

    skills = ", ".join(selected_skills)

    # ------------------------------
    # Domain
    # ------------------------------

    domain_options = [
        "Machine Learning",
        "Natural Language Processing",
        "Computer Vision",
        "Healthcare",
        "Finance",
        "Education",
        "Agriculture",
        "Cybersecurity",
        "Generative AI",
        "IoT"
    ]

    print("\n🌍 Preferred Domain")

    for i, option in enumerate(domain_options, start=1):
        print(f"{i}. {option}")

    while True:

        choice = input("\nEnter your choice: ")

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(domain_options):
                domain = domain_options[choice - 1]
                break

        print("❌ Invalid Choice. Try Again.")

    # ------------------------------
    # Difficulty
    # ------------------------------

    difficulty_options = [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

    print("\n🎯 Difficulty Level")

    for i, option in enumerate(difficulty_options, start=1):
        print(f"{i}. {option}")

    while True:

        choice = input("\nEnter your choice: ")

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(difficulty_options):
                difficulty = difficulty_options[choice - 1]
                break

        print("❌ Invalid Choice. Try Again.")

    # ------------------------------
    # Recommendation Engine
    # ------------------------------

    recommender = ProjectTopicRecommender(
        "dataset/project_topics.csv"
    )

    recommendations = recommender.recommend_projects(
        interests=interests,
        skills=skills,
        domain=domain,
        difficulty=difficulty,
        top_n=5
    )

    # ------------------------------
    # Results
    # ------------------------------

    print_header(f"🎯 Top AI Project Recommendations for {name}")

    if recommendations.empty:

        print("\n❌ No matching projects found.")
        return

    for i, (_, project) in enumerate(
        recommendations.iterrows(),
        start=1
    ):

        print("\n" + "=" * 70)
        print(f"Recommendation #{i}")
        print("=" * 70)

        print_project(project)

        why_recommended(
            project,
            interests,
            skills,
            difficulty
        )

        skill_gap(
            project,
            skills
        )

        learning_resources(
            project
        )

    # ------------------------------
    # Save Recommendations
    # ------------------------------

    choice = input(
        "\n💾 Save recommendations to CSV? (yes/no): "
    ).strip().lower()

    if choice == "yes":

        save_recommendations(recommendations)

    print("\n🎉 Thank you for using AI Project Topic Recommender!")
    print("🚀 Best of luck with your AI journey!")


if __name__ == "__main__":
    main()