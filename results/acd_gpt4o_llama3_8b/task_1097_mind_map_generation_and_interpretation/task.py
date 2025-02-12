class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "generation",
                "topic": "Artificial Intelligence"
            },
            "2": {
                "task_type": "interpretation",
                "mind_map": {
                    "Node": "Climate Change",
                    "Children": [
                        {
                            "Node": "Causes",
                            "Children": [
                                {"Node": "Greenhouse gases"},
                                {"Node": "Deforestation"}
                            ]
                        },
                        {
                            "Node": "Effects",
                            "Children": [
                                {"Node": "Rising sea levels"},
                                {"Node": "Extreme weather events"}
                            ]
                        },
                        {
                            "Node": "Solutions",
                            "Children": [
                                {"Node": "Renewable energy"},
                                {"Node": "Reforestation"}
                            ]
                        }
                    ]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generation':
            return f"""Create a mind map for the following topic: {t['topic']}.

Ensure that the mind map includes at least three main branches and two sub-branches for each main branch. Submit the mind map in a structured text format resembling a tree, for example:

Node: [Main Topic]
Children:
  - Node: [Branch 1]
    Children:
      - Node: [Sub-branch 1]
      - Node: [Sub-branch 2]
  - Node: [Branch 2]
    Children:
      - Node: [Sub-branch 1]
      - Node: [Sub-branch 2]
  - Node: [Branch 3]
    Children:
      - Node: [Sub-branch 1]
      - Node: [Sub-branch 2]
"""
        else:
            return """Interpret the following mind map and generate a coherent summary that explains the relationships and key points.

Mind Map:
Node: Climate Change
Children:
  - Node: Causes
    Children:
      - Node: Greenhouse gases
      - Node: Deforestation
  - Node: Effects
    Children:
      - Node: Rising sea levels
      - Node: Extreme weather events
  - Node: Solutions
    Children:
      - Node: Renewable energy
      - Node: Reforestation

Submit your summary as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generation':
            validation_criteria = ["The mind map should include at least three main branches.", "Each main branch should have at least two sub-branches.", "The structure should be clear and logically organized.", "All branches should be relevant to the main topic."]
        else:
            validation_criteria = ["The summary should accurately reflect the relationships and key points in the mind map.", "The summary should be coherent and logically organized.", "The summary should cover all main branches and sub-branches in the mind map.", "The summary should not omit any significant details."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
