class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Imagine a world where humans can communicate with animals. Describe the societal changes that might occur and the potential benefits and challenges.",
                "criteria": "The scenario should include at least 3 societal changes, 2 potential benefits, and 2 potential challenges."
            },
            "2": {
                "prompt": "Imagine a future where space travel is as common as air travel today. Describe how daily life and global dynamics might change, including economic, social, and environmental aspects.",
                "criteria": "The scenario should include at least 3 changes in daily life, 3 changes in global dynamics, and should cover economic, social, and environmental aspects."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with generating a detailed hypothetical scenario based on the given prompt. Your scenario should be coherent, logically structured, and explore the given criteria in depth.

Prompt: {t['prompt']}

Submit your response in the following format:
Scenario: [Your detailed scenario]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            t['criteria']
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
