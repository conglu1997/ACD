class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'scenario': 'A company is being sued for breach of contract because it failed to deliver goods on time. The company claims that a natural disaster prevented timely delivery. Present an argument for the plaintiff (the party suing the company).'},
            '2': {'scenario': 'A tenant is being evicted for not paying rent. The tenant argues that the landlord failed to make necessary repairs, making the property uninhabitable. Present a counterargument on behalf of the landlord.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: argument formulation and counterargument presentation.

Part 1: Argument Formulation
Read the given legal scenario and formulate a coherent and structured argument for the specified party. Ensure your argument is logical, well-supported by facts, and adheres to legal principles. Provide your argument in plain text format.

Scenario: {t['scenario']}

Part 2: Counterargument Presentation
Present a counterargument that challenges the initial argument. Ensure your counterargument addresses the key points of the initial argument and provides logical reasoning and evidence to support your position. Provide your counterargument in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The initial argument should be coherent and well-structured.',
            'The initial argument should be logically consistent and supported by relevant facts and legal principles.',
            'The counterargument should effectively address the key points of the initial argument.',
            'The counterargument should provide logical reasoning and evidence to support its position.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
