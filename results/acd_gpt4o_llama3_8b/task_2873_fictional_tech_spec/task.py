class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"device_name": "Quantum Neural Interface", "function": "allow direct communication between the human brain and quantum computers."},
            "2": {"device_name": "Zero-Point Energy Generator", "function": "generate unlimited energy by harnessing zero-point energy fields."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        device_name = t['device_name']
        function = t['function']
        return f"""You are tasked with writing a detailed technical specification for a fictional technology or device. The device you need to describe is the {device_name}, which is designed to {function}. Your specification should include the following sections:

1. Introduction: Provide a brief overview of the device and its purpose.
2. Technical Specifications: Detail the technical aspects, including components, materials, and how it operates.
3. Applications: Describe potential applications and use cases for the device.
4. Advantages: Explain the advantages of this technology over existing solutions.

Ensure that your technical specification is coherent, logically structured, and technically plausible within a science fiction context. Submit your response as a plain text string in the following format:

Introduction:
[Your introduction here]

Technical Specifications:
[Your technical specifications here]

Applications:
[Your applications here]

Advantages:
[Your advantages here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The technical specification should be coherent.",
            "The technical specification should be logically structured.",
            "The technical specification should be technically plausible within a science fiction context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
