import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            {
                "feature": "grammatical gender",
                "example": "German assigns gender to all nouns",
                "domain": "object perception"
            },
            {
                "feature": "color vocabulary",
                "example": "Russian has separate words for light blue and dark blue",
                "domain": "color perception"
            }
        ]
        return {str(i+1): feature for i, feature in enumerate(language_features)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates linguistic relativity effects, then use it to explore how {t['feature']} influences {t['domain']}. Your task has the following parts:

1. System Design (250-300 words):
   a) Describe the architecture of your AI system for simulating linguistic relativity effects.
   b) Explain how it represents and manipulates language structures and cognitive processes.
   c) Detail how the system models the influence of {t['feature']} on {t['domain']}.
   d) Discuss how your system integrates principles from linguistics, cognitive science, and AI.

2. Experiment Design (200-250 words):
   a) Propose an experiment using your AI system to test the influence of {t['feature']} on {t['domain']}.
   b) Describe the experimental setup, including control and experimental groups.
   c) Explain how you will measure and analyze the results.
   d) Discuss potential confounding factors and how you'll address them.

3. Simulation and Analysis (200-250 words):
   a) Provide a hypothetical set of results from your experiment.
   b) Analyze these results, explaining what they suggest about the influence of {t['feature']} on {t['domain']}.
   c) Discuss how these findings relate to existing theories of linguistic relativity.
   d) Identify any surprising or counterintuitive outcomes.

4. Cognitive Implications (150-200 words):
   a) Discuss what your simulation and results suggest about the nature of the language-thought relationship.
   b) Explore potential real-world implications of your findings.
   c) Propose a follow-up study to further investigate the observed effects.

5. AI and Linguistic Relativity (150-200 words):
   a) Reflect on how an AI system's 'native language' might influence its cognitive processes or problem-solving approaches.
   b) Discuss the potential implications of linguistic relativity for developing multilingual AI systems.
   c) Propose a method for mitigating unintended biases in AI systems that might arise from linguistic relativity effects.

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and AI capabilities. Be innovative in your approach while maintaining scientific plausibility and rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The System Design section must clearly explain how the AI simulates the influence of {t['feature']} on {t['domain']}.",
            "The Experiment Design must be well-structured and address potential confounding factors.",
            "The Simulation and Analysis section should provide plausible results and a thoughtful analysis relating to linguistic relativity theories.",
            "The Cognitive Implications section must discuss at least two potential real-world implications of the findings.",
            "The AI and Linguistic Relativity section should provide insightful reflections on the implications for AI development.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, and critical thinking in linguistics, cognitive science, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
