import ollama

FEEDBACK_FILE = "feedback-5.0.txt"

MODEL = "llama3.1"
# MODEL = "llama3.2"
# MODEL = "gemma2"


PROMPT = """
Summarize the feedbacks for the event, keep every feedback point very short. 
Make sure to include every opinion and note when it is suported by multiple people. Try to find patterns in the feedback.
Some feedback is in Czech make sure to translate it to English.

The feedbacks follow:

{}
"""

def main():
    feedback = ""
    with open(FEEDBACK_FILE, 'r') as f:
        feedback = f.read().strip()

    prompt = PROMPT.format(feedback)
    print(prompt)
    print("----")

    response = ollama.generate(
        model=MODEL,
        prompt=prompt,
    )

    print(response["response"])


if __name__ == '__main__':
    main()
