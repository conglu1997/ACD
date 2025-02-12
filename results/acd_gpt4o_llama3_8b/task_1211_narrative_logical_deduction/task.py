class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"narrative": "Detective Sarah arrived at the scene of a burglary. The window was broken, and there was a muddy footprint on the floor. The homeowner, Mr. Johnson, was away on vacation. However, the neighbors noticed a suspicious person lurking around the house the previous night. The person was wearing a red jacket and carrying a large bag. Additionally, a known burglar, who often works in this neighborhood, was recently released from prison and was seen at a nearby park earlier in the day.", "question": "Who is the most likely suspect?"},
            "2": {"narrative": "During the annual town fair, the prize-winning pie went missing from the competition tent. Witnesses reported seeing a young girl in a blue dress near the tent just before the pie disappeared. The girl was later seen running towards the park with something wrapped in a cloth. Another witness mentioned seeing an older man, who is known for his fondness for pies, lingering around the tent earlier. The man was later seen near the park, looking very satisfied.", "question": "Where is the pie most likely to be found?"}
        }
    
    @staticmethod
    def get_instructions(t: dict) -> str:
        narrative = t["narrative"]
        question = t["question"]
        return f"""Read the following narrative and answer the question based on the provided details:\n\nNarrative: {narrative}\n\nQuestion: {question}\n\nSubmit your answer as a plain text string in the format:\n\nAnswer: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
