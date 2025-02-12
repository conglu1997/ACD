import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "script_origin": "Mesoamerican",
                "archaeological_context": "Underwater ruins",
                "linguistic_feature": "Logographic writing system"
            },
            {
                "script_origin": "Ancient Near East",
                "archaeological_context": "Clay tablets in a royal archive",
                "linguistic_feature": "Syllabic writing system"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational method to decipher an ancient, unknown script from {t['script_origin']} discovered in {t['archaeological_context']}. The script is believed to use a {t['linguistic_feature']}. Your task has the following components:

1. Computational Approach (250-300 words):
   a) Describe your proposed computational method for deciphering the script.
   b) Explain how your method incorporates linguistic principles and archaeological context.
   c) Detail any machine learning or statistical techniques you would employ.
   d) Discuss how your approach handles the challenges of a {t['linguistic_feature']}.

2. Data Analysis (200-250 words):
   a) Describe the types of data you would need to train your model.
   b) Explain how you would preprocess and represent the archaeological findings for computational analysis.
   c) Discuss any potential biases or limitations in your data approach.

3. Decipherment Process (200-250 words):
   a) Provide a step-by-step explanation of how your method would attempt to decipher the script.
   b) Describe how you would validate partial translations or hypotheses.
   c) Explain how your method might identify and interpret semantic or syntactic patterns.

4. Historical Implications (150-200 words):
   a) Speculate on potential historical insights that could be gained from deciphering this script.
   b) Discuss how these insights might change our understanding of {t['script_origin']} civilization.
   c) Explain how the {t['archaeological_context']} might influence the interpretation of the deciphered text.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical issues in using AI to decipher ancient scripts.
   b) Propose guidelines for responsible use of this technology in archaeology and linguistics.

Ensure your response demonstrates a deep understanding of computational linguistics, archaeology, and the specific challenges of the given script and context. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The computational approach effectively addresses the challenges of a {t['linguistic_feature']}.",
            f"The data analysis considers the specific context of {t['archaeological_context']}.",
            f"The decipherment process is logically sound and considers the unique aspects of {t['script_origin']} scripts.",
            "The historical implications are plausible and well-reasoned.",
            "The ethical considerations are thoughtful and relevant to the field of computational archaeology.",
            "The response demonstrates a deep understanding of computational linguistics and archaeological methods.",
            "The proposed approach is innovative while remaining scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
