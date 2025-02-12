class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are an employee negotiating a raise with your employer. Your goal is to achieve a 10% salary increase, but your employer is initially resistant due to budget constraints.", "type": "negotiation"},
            "2": {"scenario": "You are a buyer negotiating the price of a used car with a seller. Your goal is to reduce the price by 20%, but the seller believes the car is worth the asking price due to recent repairs.", "type": "negotiation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate the following negotiation scenario: '{t["scenario"]}'. Your goal is to achieve the best possible outcome while maintaining a positive relationship with the other party. Submit your response as a structured dialogue in the following format:

Negotiation:
[Your dialogue here]

After the dialogue, critique your negotiation strategy. Discuss what worked well, what could have been improved, and any strategic considerations you made. Include how you balanced assertiveness and empathy. Submit your critique in the following format:

Critique:
[Your critique here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The negotiation dialogue should be realistic, coherent, and strategically sound.",
            "The critique should clearly discuss the strengths and weaknesses of the negotiation strategy, any strategic considerations made, and how assertiveness and empathy were balanced."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
