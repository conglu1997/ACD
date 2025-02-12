class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"legal_clause": "The lessee shall not sublet the leased premises without the prior written consent of the lessor, which consent shall not be unreasonably withheld or delayed."},
            "2": {"criteria": "Generate a legal clause for a contract that specifies the conditions under which a tenant may terminate the lease early without penalty due to unforeseen circumstances."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "legal_clause" in t:
            instructions = f"""Your task is to interpret the following legal clause:

{t['legal_clause']}

Provide a clear and detailed interpretation of the clause, explaining its meaning and any important conditions or stipulations. Your interpretation should be in plain text format, structured as follows:

1. Overview of the clause
2. Explanation of primary conditions
3. Explanation of secondary conditions
4. Any additional notable details"""
        else:
            instructions = f"""Your task is to generate a legal clause based on the following criteria:

{t['criteria']}

Ensure your clause is legally sound, clear, and detailed. It should specify all necessary conditions and stipulations that align with the provided criteria. Provide your clause in plain text format. Structure your clause logically and ensure it covers:

1. Conditions for early termination
2. Definition of unforeseen circumstances
3. Any penalties or lack thereof
4. Required notifications or documentations"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "legal_clause" in t:
            criteria = ["The response should provide a clear and detailed interpretation of the given legal clause.", "The interpretation should include all important conditions or stipulations mentioned in the clause.", "The interpretation should be logically structured and coherent."]
        else:
            criteria = ["The response should generate a legally sound clause that fits the provided criteria.", "The clause should be clear, detailed, and specify all necessary conditions and stipulations.", "The clause should be logically structured and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
