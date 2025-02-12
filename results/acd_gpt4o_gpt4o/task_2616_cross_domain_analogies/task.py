class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_domain": "Biology",
                "source_concept": "Photosynthesis",
                "target_domain": "Economics",
                "description": "Create an analogy between photosynthesis in biology and a concept in economics."
            },
            "2": {
                "source_domain": "Music",
                "source_concept": "Harmony",
                "target_domain": "Team Dynamics",
                "description": "Create an analogy between harmony in music and a concept in team dynamics."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        source_domain = t["source_domain"]
        source_concept = t["source_concept"]
        target_domain = t["target_domain"]
        description = t["description"]
        instructions = f"""Your task is to create an analogy that connects the following concept from one domain to another domain.\n\nSource Domain: {source_domain}\nSource Concept: {source_concept}\nTarget Domain: {target_domain}\n\nDescription: {description}\n\nMake sure your analogy clearly explains the connection between the source concept and the target domain. Provide your analogy in plain text format.\n\nExample format:\n\nAnalogy: [Your analogy]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analogy should clearly connect the source concept to a relevant concept in the target domain.",
            "The analogy should be coherent and demonstrate an understanding of both domains."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
