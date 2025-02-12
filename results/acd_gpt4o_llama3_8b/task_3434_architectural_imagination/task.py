class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Design a futuristic skyscraper in a bustling metropolis. The building should incorporate sustainable energy sources, have a unique architectural style, include recreational areas for residents, and be able to withstand natural disasters."},
            "2": {"constraints": "Design a medieval castle situated on a hill overlooking a valley. The castle should have defensive features, a grand hall, living quarters for the royal family, and secret passageways."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t["constraints"]
        return f"""Generate a detailed description of an imagined architectural structure based on the following constraints:

Constraints: {constraints}

Ensure your description includes details about the structure's design, materials, features, and any unique aspects. The description should be at least 200 words long. Additionally, provide a brief explanation (at least 50 words) of the design choices you made. Submit your response as a plain text string in the following format:

Description: [Your detailed description here]

Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be detailed and coherent.", "The description should adhere to the given constraints.", "The architectural structure should be imaginative and visually compelling.", "The description should be at least 200 words long.", "The explanation of design choices should be at least 50 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
