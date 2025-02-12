import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "priming_type": "associative",
                "prime_target_pairs": [
                    ("doctor", "nurse"),
                    ("bread", "butter"),
                    ("king", "queen")
                ]
            },
            "2": {
                "priming_type": "semantic",
                "prime_target_pairs": [
                    ("apple", "pear"),
                    ("car", "truck"),
                    ("happy", "joyful")
                ]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and replicate human-like semantic priming effects in AI language models, focusing on {t['priming_type']} priming. Your task has three parts:

1. Explanation (150-200 words):
   a) Define {t['priming_type']} priming and explain how it differs from other types of semantic priming.
   b) Describe how this priming effect manifests in human cognition and language processing.

2. AI Replication (200-250 words):
   a) Propose a method to replicate {t['priming_type']} priming effects in an AI language model.
   b) Explain how your method would work, including any necessary modifications to the model's architecture or training process.
   c) Discuss potential challenges in implementing this method and how you would address them.

3. Experimental Design (200-250 words):
   Design an experiment to test whether your AI model exhibits human-like {t['priming_type']} priming effects. Your experimental design should:
   a) Use the following prime-target pairs: {t['prime_target_pairs']}
   b) Include a control condition
   c) Describe the procedure, measures, and expected results
   d) Explain how you would interpret different possible outcomes

Ensure your response demonstrates a deep understanding of semantic priming, cognitive linguistics, and AI language models. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should accurately define and explain {t['priming_type']} priming.",
            "The proposed AI replication method should be feasible and well-reasoned.",
            "The experimental design should be well-structured and include all required elements.",
            "The response should demonstrate a deep understanding of semantic priming, cognitive linguistics, and AI language models."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
