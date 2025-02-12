class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'scenario': 'Two employees, Alice and Bob, are in conflict over the distribution of tasks in their project. Alice feels that Bob is not contributing equally, while Bob believes that Alice is micromanaging and not giving him enough autonomy.'
            },
            '2': {
                'scenario': 'A couple, Jane and John, are having disagreements about their household responsibilities. Jane feels overwhelmed with the majority of chores, while John believes he is contributing enough and feels unappreciated for his efforts.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            'You are a mediator tasked with resolving the given conflict scenario. Engage in a role-play where you interact with the conflicting parties, understand their perspectives, and propose a resolution to the conflict. '
            'Your response should include the following elements:\n\n'
            '1. Dialogue: Simulate a conversation between you (the mediator) and the conflicting parties. Ensure that each party has a chance to express their views, and you respond empathetically.\n'
            '2. Mediation strategy: Explain the approach you are taking to mediate the conflict. \n'
            '3. Resolution: Propose a clear and fair resolution to the conflict.\n'
            '4. Justification: Provide a rationale for why you believe this resolution is fair and effective.\n'
            'Ensure your response is detailed, empathetic, and demonstrates a deep understanding of the conflict dynamics.'
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The dialogue should be realistic and show empathy towards both parties.',
            'The mediation strategy should be clear and appropriate for the scenario.',
            'The proposed resolution should be fair and address the concerns of both parties.',
            'The justification should logically explain why the resolution is effective.',
            'The response should be well-structured and coherent.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
