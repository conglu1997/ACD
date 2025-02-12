class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"technology_name": "Quantum Neural Processor", "prompt": "Generate a detailed technical documentation for a Quantum Neural Processor that includes an overview, features, usage instructions, and potential applications."},
            "2": {"technology_name": "Holographic Data Storage", "prompt": "Generate a detailed technical documentation for Holographic Data Storage that includes an overview, features, usage instructions, and potential applications."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with generating technical documentation for a fictional technology called '{t["technology_name"]}'. Your documentation should include the following sections:

1. Overview: Provide a brief overview of the technology, explaining what it is and its purpose.
2. Features: List and describe the key features of the technology.
3. Usage Instructions: Provide detailed instructions on how to use the technology.
4. Potential Applications: Discuss potential applications and use cases for the technology.

Ensure that your documentation is clear, coherent, technically plausible, and creative. Submit your response as a plain text string in the following format:

Overview: [Your overview]
Features: [Your features]
Usage Instructions: [Your usage instructions]
Potential Applications: [Your potential applications]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The documentation should be clear, coherent, technically plausible, and creative.", "All four sections (Overview, Features, Usage Instructions, Potential Applications) should be appropriately addressed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
