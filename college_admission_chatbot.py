
"""
AI Chatbot Prototype for College Admission Queries
Simulated Q&A interactions using a simple command-line interface
Author: YourName
"""

def chatbot_response(user_input):
    responses = {
        "last date to apply for btech": "The last date to apply for B.Tech is 20th April 2025.",
        "scholarships for girls": "Yes, we offer 25% tuition fee waivers for female students scoring above 80%.",
        "hostel available": "Yes, hostel accommodation is available for all first-year students on a first-come, first-served basis.",
        "documents needed": "You will need: 10th and 12th mark sheets, Transfer certificate, ID proof (Aadhar/passport), Passport-size photographs.",
        "apply with 65 in pcm": "Yes, but eligibility depends on the course. For B.Tech, a minimum of 60% in PCM is required."
    }

    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I don't have information on that yet. Please contact the admission office."

# Demo interaction
if __name__ == "__main__":
    print("Welcome to the College Admission Assistant!")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you! Have a great day.")
            break
        print("Bot:", chatbot_response(user_input))
