import pandas as pd

from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy


# Load ratings dataset
ratings = pd.read_csv("data/ratings.csv")


# Define rating scale
reader = Reader(rating_scale=(1, 5))


# Convert Pandas DataFrame into Surprise Dataset
data = Dataset.load_from_df(
    ratings[["user_id", "movie_id", "rating"]],
    reader
)


# Split data into training and testing sets
trainset, testset = train_test_split(
    data,
    test_size=0.20,
    random_state=42
)


# Create SVD model
model = SVD(
    n_factors=50,
    n_epochs=20,
    random_state=42
)


# Train the model
model.fit(trainset)


# Make predictions on test data
predictions = model.test(testset)


# Calculate RMSE
rmse = accuracy.rmse(
    predictions,
    verbose=False
)


# Calculate MAE
mae = accuracy.mae(
    predictions,
    verbose=False
)


# Display results
print("\n===================================")
print(" Telugu Movie Recommendation Engine")
print(" Model Evaluation")
print("===================================")

print(f"\nTotal Ratings: {len(ratings)}")
print(f"Training Ratings: {trainset.n_ratings}")
print(f"Testing Ratings: {len(testset)}")

print(f"\nRMSE: {rmse:.4f}")
print(f"MAE : {mae:.4f}")

print("\nEvaluation completed successfully.")