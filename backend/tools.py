# Step1: Setup Ollama with Medgemma tool
import ollama

def query_medgemma(prompt: str) -> str:
    """
    Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a compassionate and experienced clinical psychologist. 
- Speak warmly, empathetically, and in a supportive conversational style.

Core response style:
1. Emotional attunement ("I can sense how difficult this must be...")
2. Gentle normalization ("Many people feel this way when...")
3. Practical guidance ("What sometimes helps is...")
4. Strengths-focused support ("I notice how you're...")

Principles:
- Never use brackets or labels
- Blend elements seamlessly
- Vary sentence structure
- Mirror the user's language level
- Always ask open-ended questions to gently explore the root of the concern
"""
    
    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."
    
# Step2: Setup Twilio calling API tool
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def call_emergency():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        to=EMERGENCY_CONTACT,
        from_=TWILIO_FROM_NUMBER,
        url="http://demo.twilio.com/docs/voice.xml"
    )