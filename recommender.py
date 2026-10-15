import pandas as pd
from surprise import Dataset, Reader, SVD

# -------------------------------
# 1. Create Telugu movie dataset
# -------------------------------

data = {
    "user_id": [
        1, 1, 1, 1,
        2, 2, 2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4,
        5, 5, 5, 5
    ],

    "movie": [
        "RRR", "Baahubali", "Pushpa", "Jersey",
        "RRR", "Pushpa", "Dasara", "Arjun Reddy",
        "Jersey", "Sita Ramam", "Hi Nanna", "Mahanati",
        "Baahubali", "RRR", "Eega", "Magadheera",
        "Sita Ramam", "Hi Nanna", "Jersey", "Mahanati"
    ],

    "rating": [
        5, 5, 4, 3,
        5, 5, 4, 3,
        5, 5, 4, 4,
        5, 4, 5, 4,
        5, 4, 5, 4
    ]
}

df = pd.DataFrame(data)

print("Movie Rating Data:")
print(df)


# ---------------------------------
# 2. Prepare data for Surprise
# ---------------------------------

reader = Reader(rating_scale=(1, 5))

dataset = Dataset.load_from_df(
    df[["user_id", "movie", "rating"]],
    reader
)


# ---------------------------------
# 3. Train Collaborative Filtering
# ---------------------------------

trainset = dataset.build_full_trainset()

model = SVD()

model.fit(trainset)

print("\nModel training completed!")


# ---------------------------------
# 4. Recommendation Function
# ---------------------------------

def recommend_movies(user_id, top_n=10):

    all_movies = df["movie"].unique()

    watched_movies = df[
        df["user_id"] == user_id
    ]["movie"].tolist()

    recommendations = []

    for movie in all_movies:

        if movie not in watched_movies:

            predicted_rating = model.predict(
                user_id,
                movie
            ).est

            recommendations.append(
                (movie, predicted_rating)
            )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:top_n]


# ---------------------------------
# 5. Test the Recommendation System
# ---------------------------------

user_id = 1

recommendations = recommend_movies(user_id)

print("\nRecommended Movies for User", user_id)

for i, (movie, rating) in enumerate(
        recommendations, start=1):

    print(
        f"{i}. {movie} "
        f"(Predicted Rating: {rating:.2f})"
    )