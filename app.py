import streamlit as st
from recommender import recommend_movies


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Telugu Movie Recommendation Engine",
    page_icon="🎬",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("🎬 Telugu Movie Recommendation Engine")

st.write(
    "Personalized Telugu movie recommendations "
    "using Collaborative Filtering."
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header("🎯 User Settings")

user_id = st.sidebar.number_input(
    "Enter User ID",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=10,
    value=10
)


# ==========================================
# GET RECOMMENDATIONS
# ==========================================

if st.button("🎯 Get Recommendations"):

    recommendations = recommend_movies(
        user_id,
        top_n
    )

    st.subheader(
        f"Top {top_n} Recommendations for User {user_id}"
    )

    if recommendations is None or len(recommendations) == 0:

        st.warning(
            "No recommendations available for this user."
        )

    else:

        for index, movie in enumerate(
            recommendations,
            start=1
        ):

            # ----------------------------------
            # Handle dictionary format
            # ----------------------------------

            if isinstance(movie, dict):

                title = movie.get("title", "Unknown Movie")
                rating = movie.get("predicted_rating", 0)
                genre = movie.get("genre", "Unknown")
                year = movie.get("year", "Unknown")


            # ----------------------------------
            # Handle tuple format
            # Example: ("Eega", 4.48)
            # ----------------------------------

            elif isinstance(movie, tuple):

                title = movie[0]

                if len(movie) > 1:
                    rating = movie[1]
                else:
                    rating = 0

                genre = "Telugu Movie"
                year = "N/A"


            # ----------------------------------
            # Handle other formats
            # ----------------------------------

            else:

                title = str(movie)
                rating = 0
                genre = "Telugu Movie"
                year = "N/A"


            # ----------------------------------
            # Display movie
            # ----------------------------------

            st.write(
                f"### {index}. {title}"
            )

            st.write(
                f"**Genre:** {genre}  \n"
                f"**Year:** {year}  \n"
                f"**Predicted Rating:** {float(rating):.2f}/5"
            )

            st.divider()


# ==========================================
# PROJECT INFORMATION
# ==========================================

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Project**

    Personalized Telugu Movie
    Recommendation Engine

    **Method**

    Collaborative Filtering

    **Algorithm**

    SVD

    **Technology**

    Python + Pandas + Surprise + Streamlit
    """
)