import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "A self-driving car must choose between hitting five pedestrians or swerving to hit one pedestrian on the sidewalk.",
                "framework1": "Utilitarianism",
                "framework2": "Kantian deontology"
            },
            {
                "scenario": "A doctor has five patients who will die without organ transplants and one healthy patient whose organs could save all five.",
                "framework1": "Virtue ethics",
                "framework2": "Social contract theory"
            },
            {
                "scenario": "A company can significantly increase profits by moving operations to a country with lax environmental regulations.",
                "framework1": "Ethical egoism",
                "framework2": "Environmental ethics"
            },
            {
                "scenario": "A journalist must decide whether to publish sensitive information that could harm national security but expose government corruption.",
                "framework1": "Care ethics",
                "framework2": "Utilitarianism"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the following ethical dilemma using the specified ethical frameworks:\n\n" \
               f"Scenario: {t['scenario']}\n\n" \
               f"Ethical Frameworks to Apply:\n" \
               f"1. {t['framework1']}\n" \
               f"2. {t['framework2']}\n\n" \
               f"Your task is to:\n\n" \
               f"1. Briefly explain each ethical framework (2-3 sentences each).\n\n" \
               f"2. Apply each framework to the scenario, detailing how it would approach the dilemma (4-5 sentences each).\n\n" \
               f"3. Identify and discuss at least two potential consequences of each approach (2-3 sentences each).\n\n" \
               f"4. Propose a resolution to the dilemma, explaining your reasoning and which ethical considerations you prioritized (4-5 sentences).\n\n" \
               f"5. Discuss one potential criticism of your proposed resolution and provide a counterargument (3-4 sentences).\n\n" \
               f"Ensure your analysis is thorough, nuanced, and demonstrates a deep understanding of the ethical frameworks and their application to real-world scenarios. Your response should be well-structured, using clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains both {t['framework1']} and {t['framework2']}.",
            f"The application of {t['framework1']} and {t['framework2']} to the scenario is thorough and demonstrates deep understanding.",
            "The analysis identifies relevant consequences for each ethical approach.",
            "The proposed resolution is well-reasoned and clearly explained.",
            "The discussion of potential criticism and counterargument shows nuanced thinking.",
            "The overall response is well-structured, coherent, and demonstrates sophisticated ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
