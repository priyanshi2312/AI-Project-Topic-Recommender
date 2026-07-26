import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import preprocess_text


class ProjectTopicRecommender:

    def __init__(self, dataset_path):

        # Load dataset
        self.df = pd.read_csv(dataset_path)

        # Fill missing values
        self.df.fillna("", inplace=True)

        # Create one text column
        self.df["combined_text"] = (
            self.df["title"] + " " +
            self.df["domain"] + " " +
            self.df["skills"] + " " +
            self.df["interests"] + " " +
            self.df["description"]
        )

        # Clean text
        self.df["clean_text"] = self.df["combined_text"].apply(preprocess_text)

        # TF-IDF
        self.vectorizer = TfidfVectorizer(stop_words="english")

        self.project_vectors = self.vectorizer.fit_transform(
            self.df["clean_text"]
        )

    def recommend_projects(
            self,
            interests,
            skills,
            domain,
            difficulty,
            top_n=5):

        # Create student profile
        student_profile = (
            interests + " " +
            skills + " " +
            domain + " " +
            difficulty
        )

        clean_profile = preprocess_text(student_profile)

        profile_vector = self.vectorizer.transform([clean_profile])

        similarity = cosine_similarity(
            profile_vector,
            self.project_vectors
        ).flatten()

        recommendations = self.df.copy()

        recommendations["match_score"] = similarity

        # -------------------------
        # Give Bonus Score
        # -------------------------

        for index, row in recommendations.iterrows():

            bonus = 0

            # Preferred Domain Match
            if row["domain"].lower() == domain.lower():
                bonus += 0.15

            # Difficulty Match
            if row["difficulty"].lower() == difficulty.lower():
                bonus += 0.10

            # Skill Match
            project_skills = row["skills"].lower()

            user_skills = [
                skill.strip().lower()
                for skill in skills.split(",")
            ]

            for skill in user_skills:
                if skill in project_skills:
                    bonus += 0.05

            recommendations.at[index, "match_score"] += bonus

        # Maximum score = 100%
        recommendations["match_score"] = recommendations[
            "match_score"
        ].clip(upper=1)

        recommendations["match_percentage"] = (
            recommendations["match_score"] * 100
        ).round(2)

        recommendations = recommendations.sort_values(
            by="match_score",
            ascending=False
        )

        return recommendations.head(top_n)