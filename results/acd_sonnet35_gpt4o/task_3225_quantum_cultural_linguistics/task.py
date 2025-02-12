import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_feature": "phonological shifts",
                "cultures": ["Mandarin Chinese", "English", "Arabic"],
                "quantum_principle": "superposition",
                "time_span": "next 50 years"
            },
            {
                "linguistic_feature": "semantic drift",
                "cultures": ["Japanese", "Spanish", "Swahili"],
                "quantum_principle": "entanglement",
                "time_span": "next 100 years"
            },
            {
                "linguistic_feature": "syntactic structures",
                "cultures": ["Hindi", "Russian", "Portuguese"],
                "quantum_principle": "quantum tunneling",
                "time_span": "next 75 years"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm to model and analyze the evolution of {t['linguistic_feature']} across {', '.join(t['cultures'])} cultures, incorporating the quantum principle of {t['quantum_principle']}. Then, use your algorithm to predict language changes over the {t['time_span']} and propose a solution to a cross-cultural communication problem. Your response should include:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the key components of your quantum algorithm for modeling linguistic evolution.
   b) Explain how you incorporate {t['quantum_principle']} into your algorithm.
   c) Detail how your algorithm represents and processes linguistic and cultural data.
   d) Provide a high-level quantum circuit diagram or pseudocode for a crucial part of your algorithm.

2. Linguistic-Cultural Model (250-300 words):
   a) Explain how your model simulates the evolution of {t['linguistic_feature']} across the specified cultures.
   b) Describe how cultural factors are integrated into your linguistic model.
   c) Discuss how quantum effects in your algorithm influence the modeling of linguistic changes.

3. Predictive Analysis (200-250 words):
   a) Present your algorithm's predictions for changes in {t['linguistic_feature']} across the specified cultures over the {t['time_span']}.
   b) Explain the reasoning behind these predictions, citing relevant linguistic and cultural factors.
   c) Discuss any potential limitations or uncertainties in your predictions.

4. Cross-Cultural Communication Problem (200-250 words):
   a) Identify a specific cross-cultural communication problem arising from the predicted linguistic changes.
   b) Propose a solution to this problem using insights from your quantum-cultural linguistic model.
   c) Explain how your solution leverages the quantum nature of your algorithm.

5. Quantum Advantage Analysis (150-200 words):
   a) Discuss the advantages of using a quantum approach for this linguistic-cultural modeling task.
   b) Compare the performance of your quantum algorithm to classical methods for similar tasks.
   c) Identify any unique insights or capabilities provided by the quantum approach.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss the ethical considerations of using quantum computing to predict and potentially influence linguistic evolution.
   b) Analyze the potential societal impacts of your algorithm and its predictions.
   c) Propose guidelines for the responsible use of quantum-cultural linguistic modeling.

7. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your quantum-cultural linguistic model.
   b) Propose a novel research question that could be explored using your approach.

8. Practical Example (150-200 words):
   a) Provide a brief example of how your algorithm would process a specific instance of {t['linguistic_feature']} in one of the specified cultures. Explain the steps involved and how the quantum aspects come into play.
   b) Compare how this example would be processed using a classical approach versus your quantum approach, highlighting the key differences and advantages of the quantum method.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, cultural anthropology, and complex systems modeling. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1500-1900 words. Include a word count at the end of each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed quantum algorithm design for modeling the evolution of {t['linguistic_feature']} across the specified cultures.",
            f"The algorithm should incorporate the quantum principle of {t['quantum_principle']} in a meaningful way.",
            f"The linguistic-cultural model should demonstrate a deep understanding of both linguistic principles and cultural factors.",
            f"The predictive analysis should provide plausible predictions for linguistic changes over the {t['time_span']}.",
            "The proposed solution to the cross-cultural communication problem should be innovative and well-reasoned.",
            "The response should clearly articulate the quantum advantage for this linguistic-cultural modeling task.",
            "The ethical and societal implications of the quantum-cultural linguistic modeling should be thoroughly discussed.",
            "The response should demonstrate creativity and interdisciplinary knowledge integration throughout.",
            f"A practical example of how the algorithm processes a specific instance of {t['linguistic_feature']} should be provided and explained clearly.",
            "The response should include a comparison between the quantum and classical approaches for processing the specific linguistic feature.",
            "The response should adhere to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
