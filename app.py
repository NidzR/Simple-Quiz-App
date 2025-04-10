import streamlit as st # type: ignore

st.title("AI Knowledge Quiz")

# Quiz questions with multiple choice options
questions = {
    "What is the capital of Pakistan?": {
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    "Which is the largest ocean?": {
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    "What does 'LLM' stand for in AI?": {
        "options": ["Large Language Model", "Long Learning Machine", "Layered Logic Module", "Linguistic Learning Method"],
        "answer": "Large Language Model"
    },
    "Which company developed ChatGPT?": {
        "options": ["Google", "OpenAI", "Microsoft", "Amazon"],
        "answer": "OpenAI"
    },
    "What is the transformer architecture used for?": {
        "options": ["Image recognition", "Language processing", "Robotics", "Data storage"],
        "answer": "Language processing"
    },
    "Which of these is NOT an AI application?": {
        "options": ["Chatbots", "Self-driving cars", "Blockchain", "Facial recognition"],
        "answer": "Blockchain"
    }
}

score = 0
user_answers = {}

# Display each question
for i, (question, data) in enumerate(questions.items()):
    st.subheader(f"Question {i+1}: {question}")
    user_answer = st.radio(
        "Select your answer:",
        data["options"],
        key=question,
        index=None  # Forces user to make a selection
    )
    user_answers[question] = user_answer

# Show results
if st.button("Submit Quiz"):
    # Calculate score
    score = sum(1 for q, data in questions.items() 
              if user_answers.get(q) == data["answer"])
    
    # Display results
    st.success(f"Your Score: {score}/{len(questions)} ({score/len(questions):.0%})")
    
    # Performance feedback
    if score == len(questions):
        st.balloons()
        st.write("🎉 AI Expert! Perfect score!")
    elif score >= len(questions)*0.7:
        st.write("👍 Great job! You know your AI!")
    elif score >= len(questions)*0.4:
        st.write("🤓 Good effort! Keep learning about AI!")
    else:
        st.write("💪 A good start! Try again!")
    
    # Show detailed review
    st.subheader("Quiz Review:")
    for i, (question, data) in enumerate(questions.items()):
        user_ans = user_answers.get(question, "Not answered")
        correct = user_ans == data["answer"]
        
        st.write(f"**Question {i+1}:** {question}")
        st.write(f"Your answer: {'✅' if correct else '❌'} {user_ans}")
        if not correct:
            st.write(f"Correct answer: {data['answer']}")
        st.write("---")