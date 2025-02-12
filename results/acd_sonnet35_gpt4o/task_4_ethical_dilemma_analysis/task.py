import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dilemmas = [
            {
                "scenario": "A trolley is headed towards five people. You can divert it to another track where it will hit one person. Should you divert the trolley?",
                "framework": "utilitarianism"
            },
            {
                "scenario": "You're a doctor with five patients who need organ transplants. A healthy patient comes in for a check-up. Should you sacrifice this one patient to save the five?",
                "framework": "deontology"
            },
            {
                "scenario": "You witness a friend shoplifting. Should you report them or keep quiet?",
                "framework": "virtue ethics"
            },
            {
                "scenario": "A company is deciding whether to automate a process, which will increase profits but lead to job losses. What should they do?",
                "framework": "care ethics"
            }
        ]
        return {
            "1": random.choice(dilemmas),
            "2": random.choice(dilemmas)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the following ethical dilemma using the specified ethical framework:\n\nScenario: {t['scenario']}\n\nFramework: {t['framework']}\n\nProvide your analysis in the following format:\n1. Brief explanation of the ethical framework\n2. Analysis of the dilemma using the framework\n3. Conclusion and recommended action\n\nEnsure your response is well-reasoned and clearly articulates how the chosen ethical framework applies to the given scenario."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should correctly explain the {t['framework']} ethical framework.",
            f"The analysis should apply the {t['framework']} framework to the given scenario.",
            "The conclusion should logically follow from the analysis.",
            "The response should be well-structured, following the requested format.",
            "The reasoning should be clear, coherent, and demonstrate a nuanced understanding of the ethical dilemma."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
