import streamlit as st
import pickle as pk

st.set_page_config(
    page_title="Loan Acceptance Prediction App",
    page_icon="🏦📑",
    layout="centered",
    initial_sidebar_state="expanded",
)


# Use caching to load model and scaler only once
@st.cache_resource
def load_model_and_scaler():
    model_path = 'loan_classifier_model.pkl'
    scaler_path = 'scaler.pkl'
    try:
        with open(scaler_path, 'rb') as file:
            scaler = pk.load(file)
        with open(model_path, 'rb') as file:
            model = pk.load(file)
        return model, scaler
    except FileNotFoundError as e:
        st.error(f"Error loading model or scaler: {e}")
        st.stop()

model, scaler = load_model_and_scaler()


def prediction(model, scaler, input_data):
    """
    Predicts whether a loan application will be approved based on input data.

    Args:
        model: A trained classification model used to make the prediction.
        scaler: A fitted scaler object used to normalize input features.
        input_data (list): A list of numeric input features representing a loan application.

    Returns:
        str: 'Approved' if the model predicts loan approval, otherwise 'Rejected'.
    """
    input_scaled = scaler.transform([input_data])
    pred = model.predict(input_scaled)
    return 'Approved' if pred[0] == 1 else 'Rejected'


# Web interface using Streamlit
def main():
    # Sidebar with title and description
    st.sidebar.title("Loan Acceptance Prediction App")
    st.sidebar.markdown(
        """
        This app predicts whether your loan will be approved based on the financial information you provide.
        """
    )

    st.sidebar.markdown("### Enter the following information:")


    # Input fields in sidebar
    total_rec_prncp = st.sidebar.number_input(
        "📥 Total Principal Received (total_rec_prncp)",
        min_value=0.0,
        step=100.0,
        format="%.2f",
        value=0.0
    )
    funded_amnt = st.sidebar.number_input(
        "💵 Funded Amount (funded_amnt)",
        min_value=0.0,
        step=100.0,
        format="%.2f",
        value=0.0
    )
    last_pymnt_amnt = st.sidebar.number_input(
        "💰 Last Payment Amount (last_pymnt_amnt)",
        min_value=0.0,
        step=100.0,
        format="%.2f",
        value=0.0
    )
    

    # Prediction button
    if st.sidebar.button("🔮 Predict"):
        user_input = [
            total_rec_prncp,
            funded_amnt,
            last_pymnt_amnt
        ]

        if any(val < 0 for val in user_input):
            st.sidebar.error("Values cannot be negative. Please check your inputs.")
        else:
            result = prediction(model, scaler, user_input)
            if result == 'Approved':
                st.success(f'🎉 **Your loan has been {result}**')
                st.balloons()
            else:
                st.error(f'❌ **Your loan has been {result}**')
                st.warning("Unfortunately, your loan application is likely to be rejected.")


    # Main content
    st.markdown(
        """
        <div style="background-color:#f0f8ff;padding:20px;border-radius:10px">
            <h1 style="color:#003366;text-align:center;">🏦📑 Loan Approval Prediction App</h1>
            <p style="color:#555555;text-align:center;">
                Predict whether your loan will be approved based on the information provided.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


    # Footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f0f8ff;
            color: #555555;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            <p>© 2025 Loan Acceptance Prediction App. All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    main()