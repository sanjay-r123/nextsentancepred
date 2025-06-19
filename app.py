import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key and project ID from environment
API_KEY = os.getenv("IBM_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")

# Function to get IAM access token
def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        st.error("Failed to get IAM token.")
        return None

# Streamlit UI
st.title("🧠 Next Sentence Prediction using IBM Watsonx")

user_input = st.text_input("Enter an incomplete sentence:")

if st.button("Generate Next Sentence"):
    if user_input.strip():
        token = get_iam_token(API_KEY)
        if token is None:
            st.stop()

        # Few-shot prompt
        prompt = f"""Input: Complete this sentence: I went to the market to
Output: buy fresh fruits and vegetables.

Input: I opened the fridge to
Output: grab a cold drink.

Input: Tomorrow, we will
Output: go hiking if the weather is good.

Input: {user_input.strip()}
Output:"""

        url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        body = {
            "input": prompt,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 200,
                "min_new_tokens": 0,
                "repetition_penalty": 1
            },
            "model_id": "ibm/granite-3-8b-instruct",
            "project_id": PROJECT_ID,
            "moderations": {
                "hap": {"input": {"enabled": True}, "output": {"enabled": True}},
                "pii": {"input": {"enabled": True}, "output": {"enabled": True}},
                "granite_guardian": {"input": {"threshold": 1}}
            }
        }

        response = requests.post(url, headers=headers, json=body)

        if response.status_code == 200:
            result = response.json().get("results", [{}])[0].get("generated_text", "No output")
            st.success(result)
        else:
            st.error("API Error: " + response.text)
    else:
        st.warning("Please enter a sentence.")
