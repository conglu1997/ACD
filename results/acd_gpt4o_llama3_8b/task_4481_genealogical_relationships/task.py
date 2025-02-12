class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a family tree diagram for the following family description.",
                "family_description": "John and Mary have two children, Alice and Bob. Alice is married to George and they have one child, Emma. Bob is married to Sarah and they have two children, Jack and Lily."
            },
            "2": {
                "description": "Describe the familial relationships in the given family tree.",
                "family_tree": {
                    "John and Mary": ["Alice", "Bob"],
                    "Alice and George": ["Emma"],
                    "Bob and Sarah": ["Jack", "Lily"]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "family_description" in t:
            return f"""Generate a family tree diagram based on the given family description.

Family Description: {t['family_description']}

Submit your response as a plain text string in the following format:
- Family Tree: [Your family tree here, represented hierarchically. For example: \nJohn and Mary\n  - Alice\n    - Emma\n  - Bob\n    - Jack\n    - Lily]

Ensure that the representation clearly shows the relationships, with parents listed first, followed by their children indented under their names. Use indentation to show generations clearly."""
        elif "family_tree" in t:
            return f"""Describe the familial relationships in the given family tree.

Family Tree: {t['family_tree']}

Submit your response as a plain text string in the following format:
- Description: [Your detailed description of the familial relationships here, e.g., 'John and Mary are the parents of Alice and Bob. Alice is married to George and they have a daughter named Emma. Bob is married to Sarah and they have two children, Jack and Lily.']

Ensure that your description accurately reflects all relationships and clearly explains the connections between family members. Double-check for completeness and clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should accurately represent the given family description or tree.",
            "The relationships should be clear and correctly interpreted.",
            "The family tree should be in a hierarchical format with proper indentation.",
            "The description should be detailed and correctly describe all relationships."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
