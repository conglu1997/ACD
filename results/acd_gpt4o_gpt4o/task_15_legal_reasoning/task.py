class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Alice was walking her dog in a park where dogs are required to be on a leash. Her dog was not on a leash and bit a child. The child's parents are suing Alice for negligence. Provide a legal argument for Alice's defense.", "principles": ["Negligence requires proving duty, breach of duty, causation, and damages.", "Contributory negligence may reduce liability."]},
            "2": {"scenario": "John signed a contract to buy a car from Mary. The contract stated that the car was in 'excellent condition.' After the purchase, John discovered that the car had significant mechanical issues. John wants to sue Mary for breach of contract. Provide a legal argument for John's case.", "principles": ["A breach of contract occurs when one party fails to perform as specified in the contract.", "Misrepresentation or fraud may invalidate a contract."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        principles = "\n".join(t["principles"])
        instructions = f"""Your task is to interpret the following legal scenario and provide a reasoned legal argument or solution based on the given facts and principles:

Scenario: {scenario}

Relevant Legal Principles:
{principles}

Your argument should be clear, logical, and legally sound. Ensure that you address all relevant aspects of the scenario and apply the legal principles accurately. Provide your argument in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should address all relevant aspects of the scenario.",
            "The argument should apply the given legal principles accurately.",
            "The argument should be clear, logical, and legally sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
