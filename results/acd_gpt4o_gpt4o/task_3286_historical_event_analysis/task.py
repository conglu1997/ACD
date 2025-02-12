class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776."},
            "2": {"event": "The fall of the Berlin Wall in 1989."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """You are provided with a description of a historical event. Your task is to perform the following:
1. Analyze the given historical event and discuss its significance.
2. Connect the given event to another related historical event, explaining the connection and its importance.

Event: {t['event']}

Example response format:
1. Analysis: [Your analysis of the historical event]
2. Connection: [Your connection to another related historical event]

Example 1:
Event: 'The signing of the Declaration of Independence in 1776.'
1. Analysis: The signing of the Declaration of Independence marked the formal assertion of the American colonies' desire to separate from British rule. It laid the foundation for the creation of the United States and introduced the principles of liberty, equality, and democracy.
2. Connection: This event is connected to the French Revolution in 1789, as the ideals of liberty and equality espoused in the Declaration of Independence inspired French revolutionaries. The French Revolution, in turn, had a profound impact on the spread of democratic ideals across Europe and the world.

Example 2:
Event: 'The fall of the Berlin Wall in 1989.'
1. Analysis: The fall of the Berlin Wall symbolized the end of the Cold War and the division between East and West Germany. It marked the decline of communist influence in Eastern Europe and led to the reunification of Germany and the collapse of the Soviet Union.
2. Connection: This event is connected to the Velvet Revolution in Czechoslovakia in 1989. The peaceful protests and political changes in Czechoslovakia were part of the broader wave of anti-communist movements in Eastern Europe, influenced by the fall of the Berlin Wall. These movements contributed to the end of communist regimes in the region and the establishment of democratic governments."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should accurately discuss the significance of the given historical event.",
            "The connection should be relevant and explain the relationship between the given event and the related historical event."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
