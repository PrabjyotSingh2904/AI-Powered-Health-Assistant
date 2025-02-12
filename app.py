import streamlit as st 
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time, random

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="Sharathhebbar24/chat_gpt2_dpo")


health_tips = [
    "Did you know? Smiling can help lower your heart rate and reduce stress. 😃",
    "Drinking water boosts your metabolism. 🍏",
    "Stretching can help improve your flexibility and reduce muscle tension. 🧘‍♂",
    "Your health matters! Taking a deep breath can help reduce stress. 🌿",
    "Imagine a healthier you! Regular exercise boosts your mood. 👟",
    "“The greatest wealth is health.” 💪",
    "Take a deep breath. Relaxation is key to well-being. 🧘",
    "Did you know? Laughter boosts your immune system. 😂",
    "Take regular breaks from screens to reduce eye strain and improve focus. 📵",
    "Aim for at least 30 minutes of physical activity each day. It can be as simple as a brisk walk or dancing to your favorite tunes. 🏃‍♂",
    "Include a variety of colorful fruits and vegetables in your diet to ensure you're getting a wide range of nutrients. 🥦"
]


def get_predefined_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "\bhi\b" in user_input:
        return "Hi there! How may I help you today?"
    elif "symptom" in user_input  or "treatment" in user_input:
        return "It's important to consult a medical professional for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the Doctor"
    elif "allergies" in user_input or "allergy" in user_input:
        return "Managing allergies involves avoiding triggers and taking prescribed medications. Consult an allergist for personalized advice."
    elif "hydration" in user_input:
        return "Staying hydrated is essential for your body to function properly. Aim to drink at least 8 cups of water a day."
    elif "diet" in user_input:
        return "It's important to maintain a balanced diet with a variety of fruits, vegetables, and whole grains. For personalized advice, consult a nutritionist."
    elif "exercise" in user_input:
        return "Regular exercise can improve your overall health. Aim for at least 30 minutes of moderate activity most days of the week."
    elif "emergency" in user_input:
        return "If you're experiencing a medical emergency, please call your local emergency services immediately."
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor"
    elif "mental health" in user_input:
        return "Mental health is just as important as physical health. If you're feeling stressed or overwhelmed, consider talking to a mental health professional."
    elif "health tip" in user_input:
        return random.choice(health_tips)
    else:
        return None


def healthcare_chatbot(user_input):
    predefined_response = get_predefined_response(user_input)
    if predefined_response:
        return predefined_response
    else:
         try:
             response = chatbot(user_input, max_length=250, num_return_sequences=1, temperature=0.7, truncation=True)
             return response[0]['generated_text']
         except Exception as e:
             st.error(f"An error occurred while generating a response: {e}")
             return "I'm sorry, but something went wrong while processing your request."


def display_chatbot_page():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?",placeholder="Type your query here")
    print(user_input)
    if st.button("Submit"):
        if user_input:
           st.write("**[ USER ]** : ",user_input) 
           selected_tip = random.choice(health_tips)
           tip_container = st.empty()
           with st.spinner("Processing your query, PLEASE WAIT . . . . ."):
               tip_container.info(f"💡[ HEALTH-TIP ] :  {selected_tip}")
               time.sleep(2)
               response = healthcare_chatbot(user_input)
           tip_container.empty()   
           st.warning("*DISCLAIMER*: This chatbot may give wrong answers and should not be used for diagnosis or treatment. Always consult with a qualified healthcare professional for medical advice.") 
           st.write("**[ HEALTHCARE ASSISTANT 🤖]** : ",response)
           print(response)           
        else:
            st.error("Please enter a message to get a response")
            
            
def display_bmi_calculator():
    st.title("BMI Calculator")
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Enter your height (cm)", min_value=0.0, format="%.2f")
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = weight / (height/100)**2
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 24.9:
                category = "Normal weight"
            elif bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obese"
            st.success(f"Your BMI is {bmi:.2f}")
            st.info(f"Category: {category}")
        else:
            st.error("Please enter valid weight and height")

            
def display_faq_page():
    st.title("Frequently Asked Questions (FAQs)")
    st.info("**Q1: What is the recommended daily water intake?**")
    st.success("Ans: It's recommended to drink at least 2 liters (8 cups) of water daily.")
    st.info("**Q2: How often should I exercise?**")
    st.success("Ans: Aim for at least 30 minutes of moderate activity most days of the week.")
    st.info("**Q3: How much sleep do I need each night?**")
    st.success("Ans: Adults typically need 7-9 hours of sleep each night. However, it varies depending on the individual and age group.")
    st.info("**Q4: What is a healthy BMI?**")
    st.success("Ans: A healthy BMI (Body Mass Index) is between 18.5 and 24.9.")
    st.info("**Q5: What are the benefits of meditation?**")
    st.success("Ans: Meditation can reduce stress, improve concentration and promote emotional health.")
    st.info("**Q6: What are the benefits of regular physical activity?**")
    st.success("Ans: Regular physical activity can control weight, reduce the risk of chronic diseases, improve mood, boost energy levels, and promote better sleep.")

            
def main():
    st.sidebar.header("**QUICK ACCESS**")
    page = st.sidebar.radio("Go to:", ["Healthcare Chatbot","BMI Calculator", "FAQs"])
    if page == "Healthcare Chatbot":
        display_chatbot_page()
    elif page == "BMI Calculator":
        display_bmi_calculator()
    elif page == "FAQs":
        display_faq_page()


if __name__ == "__main__":
    main()