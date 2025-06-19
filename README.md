# 🧠 Next Sentence Prediction using IBM Watsonx

This project demonstrates how to build a **Generative AI application** that predicts the **next sentence** based on a user’s partial input using IBM’s powerful foundation model — `granite-3-8b-instruct`. It leverages **Watsonx**, Python, and Streamlit to provide an interactive and intelligent sentence continuation experience.

---

## 🚀 Features

- 🤖 Uses IBM Watsonx Granite Foundation Model (`granite-3-8b-instruct`)
- 🧠 Few-shot prompting for more contextual results
- 💻 Interactive frontend built with Streamlit
- 🔒 Secure API key handling via `.env` file or Render environment
- ☁️ Live deployment on Render

---

## 🎯 Use Case

Enter a partial sentence like:

> `I went to the market to`

And the app will complete it with something like:

> `buy fresh fruits and vegetables.`

This is useful for:
- AI writing assistants
- NLP demonstrations
- Creative writing support
- Learning how to use foundation models in apps

---

## 💻 Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/next-sentence-prediction-genai.git
cd next-sentence-prediction-genai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File
```env
IBM_API_KEY=your_actual_api_key
PROJECT_ID=your_project_id
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 🌐 Live Demo

👉 [Click here to try the live app](https://your-app.onrender.com)

---

## 🔐 Environment Variables

Set the following values in your `.env` file (locally) or in Render's Environment settings:

| Variable | Description |
|----------|-------------|
| `IBM_API_KEY` | Your IBM Cloud API key (from Watsonx credentials) |
| `PROJECT_ID` | Your Watsonx project ID |

---

## 🧠 Prompt Design (Few-shot Example)

```text
Input: Complete this sentence: I went to the market to
Output: buy fresh fruits and vegetables.

Input: I opened the fridge to
Output: grab a cold drink.

Input: Tomorrow, we will
Output: go hiking if the weather is good.

Input: <User's input>
Output: <Model's prediction>
```

---

## 🛠️ Built With

- [IBM Watsonx](https://www.ibm.com/watsonx)
- [Streamlit](https://streamlit.io/)
- [Python](https://www.python.org/)
- [Render](https://render.com)

---

## 📜 License

This project is submitted as part of an academic assignment and is free to use for educational purposes.

---

## 🙋‍♂️ Author

**Sanjay**  
[GitHub](https://github.com/your-username) | [Email](mailto:your@email.com)
