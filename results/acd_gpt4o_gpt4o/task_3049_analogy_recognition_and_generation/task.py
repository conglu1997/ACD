class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"analogies": ["Hand is to Glove as Foot is to Shoe.", "Bird is to Wing as Fish is to Fin.", "Pen is to Paper as Chalk is to Blackboard."], "categories": ["Footwear", "Body Parts", "Writing Surfaces"]},
            "2": {"relationships": ["Sun : Moon :: Day : Night", "Fire : Water :: Hot : Cold", "Teacher : Student :: Doctor : Patient"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "analogies" in t:
            return "Your task is to match each given analogy to its corresponding category. The analogies and categories are as follows:\n\nAnalogies:\n1. Hand is to Glove as Foot is to Shoe\n2. Bird is to Wing as Fish is to Fin\n3. Pen is to Paper as Chalk is to Blackboard\n\nCategories:\n1. Footwear\n2. Body Parts\n3. Writing Surfaces\n\nProvide your response in the following format:\n1. [Category for analogy 1]\n2. [Category for analogy 2]\n3. [Category for analogy 3]"
        elif "relationships" in t:
            return "Your task is to create new analogies based on the provided relationships. The relationships are as follows:\n\n1. Sun : Moon :: Day : Night\n2. Fire : Water :: Hot : Cold\n3. Teacher : Student :: Doctor : Patient\n\nProvide your new analogies in the following format:\n1. [New analogy for relationship 1]\n2. [New analogy for relationship 2]\n3. [New analogy for relationship 3]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "analogies" in t:
            criteria = [
                "The analogies should be correctly matched to their corresponding categories.",
                "The response should match the expected format."]
        elif "relationships" in t:
            criteria = [
                "The new analogies should correctly reflect the given relationships.",
                "The response should match the expected format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0