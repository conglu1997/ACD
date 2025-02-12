import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_contexts = [
            {
                'era': 'World War II',
                'conflict': 'Allied vs Axis powers',
                'key_figures': ['Winston Churchill', 'Franklin D. Roosevelt', 'Joseph Stalin', 'Adolf Hitler'],
                'encryption_method': 'Substitution cipher'
            },
            {
                'era': 'Cold War',
                'conflict': 'USA vs USSR',
                'key_figures': ['John F. Kennedy', 'Nikita Khrushchev', 'Fidel Castro'],
                'encryption_method': 'One-time pad'
            }
        ]
        return {str(i+1): context for i, context in enumerate(historical_contexts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create and analyze a coded message within the context of {t['era']}, focusing on the conflict between {t['conflict']}. Your response should include the following elements:

1. Historical Context (100-150 words):
   Briefly describe the strategic situation during this period, mentioning at least two of the key figures: {', '.join(t['key_figures'])}. Explain why secure communication would be crucial in this context.

2. Coded Message (100-150 words):
   Create a short coded message (3-5 sentences) using the {t['encryption_method']} method. The message should contain strategically important information relevant to the historical context. Explain your encryption process.

3. Decryption and Analysis (150-200 words):
   Provide the decrypted version of your message. Analyze the potential impact of this information if it were intercepted and decrypted by the opposing side. How might it affect their strategic decisions?

4. Security Evaluation (100-150 words):
   Evaluate the strengths and weaknesses of the {t['encryption_method']} in this historical context. Suggest one way the method could be improved or an alternative method that might be more secure.

5. Counterfactual Scenario (150-200 words):
   Propose a plausible alternate historical outcome if this coded message had been intercepted and successfully decrypted by the opposition. How might the course of events have changed?

Ensure your response is historically accurate, demonstrates an understanding of basic cryptographic principles, and shows strategic thinking in the analysis of the message's potential impact. Be creative in your message creation and analysis while maintaining plausibility within the historical context.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately reflects the historical context of {t['era']} and the conflict between {t['conflict']}.",
            f"The coded message uses the {t['encryption_method']} method correctly and contains strategically relevant information.",
            "The analysis demonstrates understanding of cryptographic principles and strategic implications.",
            "The counterfactual scenario is plausible and shows creative thinking about historical possibilities.",
            "All sections (Historical Context, Coded Message, Decryption and Analysis, Security Evaluation, and Counterfactual Scenario) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
