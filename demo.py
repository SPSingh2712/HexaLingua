import requests

API_URL = "http://127.0.0.1:5000/ask"

# Extended demo questions (rephrased + indirect + one Hindi)
demo_questions = [
    "How to apply for hostel admission?",                     # simple rephrase
    "माइग्रेशन सर्टिफिकेट प्राप्त करने की प्रक्रिया क्या है?",          # synonym test
    "છોકરીઓની સ્કોલરશિપ માટે અરજી કેવી રીતે કરવી?",           # different wording
    "ફાળવેલી બેઠક કેવી રીતે રદ કરવી?",       # indirect form
    "How to correct mistake in application form?",                          # short form
    "पिछले साल का कटऑफ कैसे देखें?",         # context test
    "કાઉન્સેલિંગ માટે નોંધણી કેવી રીતે કરવી?",          # health center
    "അപേക്ഷയിൽ മൊബൈൽ നമ്പർ എങ്ങനെ അപ്ഡേറ്റ് ചെയ്യാം?",           # transport variation
    "How to apply for MBA admission?",                       # hostel curfew
    "क्या AKTU कॉलेज में हॉस्टल सुविधा उपलब्ध है?",                 # Hindi test
]

def run_demo():
    print("🚀 HexaLingua Demo Started\n")
    for q in demo_questions:
        print(f"Q: {q}")
        try:
            resp = requests.post(API_URL, json={"question": q})
            if resp.status_code == 200:
                print("A:", resp.json().get("answer", "No answer found"))
            else:
                print("⚠️ Error:", resp.text)
        except Exception as e:
            print("❌ Failed to connect:", e)
        print("-" * 50)

if __name__ == "__main__":
    run_demo()
