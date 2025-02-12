class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"discovery": "a new element discovered on Mars that can generate unlimited clean energy"},
            "2": {"discovery": "a microorganism found in the deep ocean that can break down plastic waste efficiently"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a fictional scientific report based on the following hypothetical discovery:

Discovery: {t['discovery']}

Instructions:
1. Provide an introduction (at least 100 words) that explains the context and significance of the discovery.
2. Describe the methodology (at least 150 words) used to make the discovery.
3. Detail the findings (at least 200 words) and their potential impact on science and society.
4. Conclude with future directions for research and possible applications of the discovery (at least 100 words).

Your response should be structured as follows:
Introduction: [Your introduction]
Methodology: [Your methodology]
Findings: [Your findings]
Conclusion: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The introduction should clearly explain the significance of the discovery and be at least 100 words.", "The methodology should be scientifically plausible and at least 150 words.", "The findings should be detailed, highlight the impact of the discovery, and be at least 200 words.", "The conclusion should provide future directions and applications and be at least 100 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
