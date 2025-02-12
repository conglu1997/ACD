class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "setup": "A seesaw with a fulcrum in the middle, a 10 kg weight on the left side 1 meter from the fulcrum, a 20 kg weight on the right side 0.5 meters from the fulcrum, and an additional 5 kg weight on the left side 2 meters from the fulcrum."
            },
            "2": {
                "setup": "A pulley system with two pulleys and a rope passing over them. One end of the rope is attached to a 5 kg weight, and the other end is pulled with a force of 100 N. There is also a 2 kg weight hanging from the middle of the rope."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following mechanical setup, predict the behavior of the system. Explain your reasoning in detail, including any relevant physical principles or laws. Your explanation should be clear and logically structured. Submit your prediction and explanation as a plain text string in the following format:\n\nPrediction: [Your prediction]\nExplanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The prediction should be accurate and based on correct physical principles.",
            "The explanation should be clear, logically structured, and include relevant physical principles or laws.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
