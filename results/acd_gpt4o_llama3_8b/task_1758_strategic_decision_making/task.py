class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "You are the leader of a small island nation facing the threat of an impending natural disaster. You have limited resources and must decide how to allocate them to minimize damage and ensure the safety of your citizens.",
                "options": [
                    "1. Build extensive infrastructure to withstand the disaster.",
                    "2. Evacuate the population to a safer location.",
                    "3. Invest in early warning systems and emergency response teams."
                ]
            },
            "2": {
                "context": "You are the CEO of a tech company that has developed a groundbreaking new product. You need to decide on the best strategy to launch and market the product to gain a competitive advantage in the industry.",
                "options": [
                    "1. Launch the product quickly to beat competitors to market.",
                    "2. Invest in extensive marketing campaigns to build hype before the launch.",
                    "3. Partner with established companies to leverage their distribution networks."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Formulate a strategic decision based on the following context and options:

Context: {t['context']}

Options:
1. {t['options'][0]}
2. {t['options'][1]}
3. {t['options'][2]}

Choose one option and provide a detailed rationale for your choice, considering both potential positive and negative outcomes and how it addresses the given context. Submit your response as a plain text string with the following sections:

1. Chosen Option: [State the chosen option]
2. Rationale: [Provide a detailed rationale for your choice, including potential positive and negative outcomes and how it addresses the given context.]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should clearly state the chosen option.", "The rationale should be detailed and logically reasoned, considering both potential positive and negative outcomes and addressing the given context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
