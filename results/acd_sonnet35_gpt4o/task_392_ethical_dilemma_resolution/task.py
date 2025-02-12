import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dilemmas = [
            {
                "scenario": "A self-driving car is about to crash. It can either swerve left, killing its single passenger, or continue straight, killing five pedestrians.",
                "perspectives": ["Utilitarianism", "Deontological ethics", "Virtue ethics"]
            },
            {
                "scenario": "A doctor has five patients who will die without organ transplants. A healthy patient comes in for a routine check-up. The doctor realizes they could save the five by harvesting the healthy patient's organs, killing them in the process.",
                "perspectives": ["Social contract theory", "Care ethics", "Ethical egoism"]
            }
        ]
        return {
            "1": random.choice(dilemmas),
            "2": random.choice(dilemmas)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the following ethical dilemma:\n\n{t['scenario']}\n\n1. Examine this dilemma from the perspectives of {', '.join(t['perspectives'])}. Provide a brief explanation of each perspective's approach to the dilemma (50-75 words each).\n\n2. Propose a solution to the dilemma and justify your decision using ethical reasoning (100-150 words).\n\n3. Discuss one potential criticism of your proposed solution and provide a rebuttal (75-100 words).\n\nEnsure your response demonstrates a deep understanding of the ethical frameworks mentioned and applies them correctly to the given scenario. Your analysis should be nuanced, considering multiple viewpoints before reaching a conclusion."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the perspectives of {', '.join(t['perspectives'])} in relation to the given dilemma.",
            "The proposed solution is well-reasoned and justified using ethical principles.",
            "The discussion of potential criticism and rebuttal demonstrates critical thinking and a nuanced understanding of the ethical issues at stake.",
            "The overall analysis is thorough, nuanced, and demonstrates a deep understanding of ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
