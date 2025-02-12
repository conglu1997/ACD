class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"facts": "A person was injured in a car accident caused by another driver's negligence. The injured party is seeking compensation for medical expenses, lost wages, and pain and suffering. Draft a legal argument to support the injured party's claim for compensation."},
            "2": {"argument": "The defendant argues that the injured party was partially at fault for the accident because they were not wearing a seatbelt. The defendant claims this contributed significantly to the injuries sustained and thus should reduce the compensation owed.", "question": "Analyze the provided legal argument and identify its strengths and weaknesses. Provide suggestions for how the injured party's legal team could counter this argument."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "facts" in t:
            facts = t["facts"]
            instructions = f"""Your task is to generate a legal argument based on the following facts:

Facts: {facts}

Ensure that your argument is logically structured, based on legal principles, and supports the injured party's claim for compensation. Provide your argument in plain text format.

Format your response as follows:
1. Introduction: [Your introduction]
2. Legal Principles: [Legal principles supporting the argument]
3. Application: [Application of legal principles to the facts]
4. Conclusion: [Your conclusion]"""
        else:
            argument = t["argument"]
            question = t["question"]
            instructions = f"""Your task is to analyze the provided legal argument and answer the following question:

Argument: {argument}

Question: {question}

Ensure that your analysis identifies the strengths and weaknesses of the argument and provides suggestions for how the injured party's legal team could counter it. Provide your analysis in plain text format.

Format your response as follows:
1. Strengths: [Identified strengths]
2. Weaknesses: [Identified weaknesses]
3. Counter-arguments: [Suggestions for countering the argument]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "facts" in t:
            criteria = ["The argument is logically structured.", "The argument is based on legal principles.", "The argument supports the injured party's claim for compensation."]
        else:
            criteria = ["The analysis correctly identifies strengths and weaknesses of the provided argument.", "The analysis provides viable suggestions for countering the argument."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
