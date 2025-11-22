import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from utils import load_model, predict_emotion, get_prediction_proba, EMOTIONS_EMOJI_DICT

def main():
    st.set_page_config(page_title="Emotion Detector", page_icon="🎭", layout="wide")
    
    st.title("🎭 Text Emotion Detection")
    st.subheader("Analyze the emotional tone of your text")

    # Sidebar
    with st.sidebar:
        st.header("About")
        st.info("This application uses a Machine Learning model to detect emotions from text.")
        st.markdown("### Supported Emotions:")
        st.markdown(", ".join([f"{emoji} {emotion.capitalize()}" for emotion, emoji in EMOTIONS_EMOJI_DICT.items()]))
        st.markdown("---")
        st.text("Built with Streamlit")

    # Load Model
    try:
        pipe_lr = load_model()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # Main Form
    with st.form(key='my_form'):
        col1, col2 = st.columns([3, 1])
        with col1:
            raw_text = st.text_area("Enter text here:", height=150, placeholder="Type something like: 'I am feeling great today!'")
        with col2:
            st.write("") # Spacer
            st.write("") # Spacer
            submit_text = st.form_submit_button(label='Analyze Emotion', use_container_width=True)

    if submit_text and raw_text:
        col1, col2 = st.columns(2)

        prediction = predict_emotion(raw_text, pipe_lr)
        probability = get_prediction_proba(raw_text, pipe_lr)

        with col1:
            st.success("Prediction Result")
            emoji_icon = EMOTIONS_EMOJI_DICT.get(prediction, "🤔")
            st.markdown(f"### {prediction.capitalize()} {emoji_icon}")
            
            confidence = np.max(probability)
            st.metric(label="Confidence Score", value=f"{confidence:.2%}")
            
            st.info(f"Original Text: {raw_text}")

        with col2:
            st.success("Prediction Probabilities")
            proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
            proba_df_clean = proba_df.T.reset_index()
            proba_df_clean.columns = ["emotions", "probability"]

            # Sort by probability for better visualization
            proba_df_clean = proba_df_clean.sort_values(by="probability", ascending=False)

            fig = alt.Chart(proba_df_clean).mark_bar().encode(
                x=alt.X('probability', axis=alt.Axis(format='%')),
                y=alt.Y('emotions', sort='-x'),
                color='emotions',
                tooltip=['emotions', alt.Tooltip('probability', format='.2%')]
            ).properties(height=400)
            
            st.altair_chart(fig, use_container_width=True)

    elif submit_text and not raw_text:
        st.warning("Please enter some text to analyze.")

if __name__ == '__main__':
    main()