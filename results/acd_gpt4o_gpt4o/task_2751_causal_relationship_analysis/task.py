class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "A study observes the following: Group A consumes 2 cups of coffee daily and exercises 30 minutes daily, Group B consumes none and does not exercise. Group A reports an average of 6 hours of sleep per night, while Group B reports an average of 8 hours of sleep per night. Identify and explain the potential causal relationships between coffee consumption, exercise, and sleep duration."},
            "2": {"scenario": "In a local community, there's been an increase in outdoor physical activities over the past year. Concurrently, there's been a noticeable decrease in obesity rates and an increase in mental well-being reports. Generate a hypothesis explaining the potential causal relationships and propose a method to test these hypotheses."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "data" in t:
            data = t["data"]
            instructions = f"""Your task is to identify and explain the potential causal relationships based on the following data:

Data: {data}

Your explanation should include:
1. Identification of the observed correlations.
2. Plausible causal relationships between the variables.
3. Reasoning that supports the proposed causal relationships.
4. Consideration of possible confounding factors.

Ensure your explanation is coherent, well-structured, and scientifically plausible. Provide your response in plain text format in the following structure:

1. Correlations: [Identified correlations]
2. Causal Relationships: [Proposed causal relationships]
3. Reasoning: [Reasoning supporting the causal relationships]
4. Confounding Factors: [Consideration of confounding factors]"""
        else:
            scenario = t["scenario"]
            instructions = f"""Your task is to generate hypotheses and propose methods to test them based on the following scenario:

Scenario: {scenario}

Your response should include:
1. Clear statements of the hypotheses.
2. Reasoning that supports the hypotheses.
3. Detailed methods to test the hypotheses, including the type of study and data collection methods.

Ensure your hypotheses and methods are coherent, well-structured, and scientifically plausible. Provide your response in plain text format in the following structure:

1. Hypotheses: [Stated hypotheses]
2. Reasoning: [Reasoning supporting the hypotheses]
3. Methods: [Methods to test the hypotheses]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "data" in t:
            criteria = [
                "The explanation should identify the observed correlations.",
                "The explanation should propose plausible causal relationships.",
                "The explanation should include reasoning that supports the causal relationships.",
                "The explanation should consider possible confounding factors."]
        else:
            criteria = [
                "The hypotheses should be clearly stated.",
                "The reasoning should support the hypotheses.",
                "The methods to test the hypotheses should be detailed and scientifically plausible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
