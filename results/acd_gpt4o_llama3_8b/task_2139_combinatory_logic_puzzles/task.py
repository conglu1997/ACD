class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Solve the following combinatory logic puzzle: Five friends (Alice, Bob, Carol, Dave, and Eve) are sitting in a row of chairs. Each friend has a different favorite color (Red, Blue, Green, Yellow, and Purple) and a different pet (Dog, Cat, Fish, Bird, and Hamster). Use the following clues to determine the order in which the friends are sitting, their favorite colors, and their pets. Clues: 1. Alice is sitting next to the person whose favorite color is Green. 2. The person with the Cat is sitting in the middle. 3. Bob is sitting on one of the ends. 4. Dave's favorite color is Blue. 5. Eve is sitting next to the person with the Dog. 6. The person with the Fish is not sitting next to the person with the Bird.",
            },
            "2": {
                "description": "Solve the following combinatory logic puzzle: Four students (John, Mike, Sarah, and Tina) each have a different subject they excel in (Math, Science, History, and Literature) and a different favorite hobby (Reading, Swimming, Cooking, and Biking). Use the following clues to determine each student's favorite subject and hobby. Clues: 1. John excels in Science. 2. The student whose favorite hobby is Reading excels in History. 3. Mike's favorite hobby is not Cooking. 4. Sarah excels in Math. 5. The student whose favorite hobby is Biking excels in Literature.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following combinatory logic puzzle based on the given clues. Use logical deduction to determine the correct arrangement or associations. Submit your solution in a clear and structured format as follows:

Clues: {t['description']}

Solution:
1. [First deduction step]
2. [Second deduction step]
...
Final Arrangement:
[Final arrangement or association including all details: names, colors, pets/subjects, hobbies]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should use logical deduction based on the provided clues.",
            "The final arrangement or association should be clearly stated.",
            "The reasoning should be detailed and coherent.",
            "The solution should cover all provided clues without contradiction."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
