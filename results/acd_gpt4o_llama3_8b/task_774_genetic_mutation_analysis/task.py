class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original_sequence": "ATGCGTACGTTAGCCTAGGATCAGTCGATCGATCGTACGATGCGTACGTTAGCCTAGGATCAGTCGATCGATCGTACG", "mutated_sequence": "ATGCGTACGTTAGCCTAGGCTCAGTCGATCGATCGTACGATGCGTACGTTAGCCTAGGATCAGTCGATCGATCGTACG"},
            "2": {"original_sequence": "ATGCGTACGTTAGCCTAGGATCAGTCGATCGATCGTACGATGCGTACGTTAGCCTAGGATCAGTCGATCGATCGTACG", "mutated_sequence": "ATGCGTACGTTAGCCTAGGATCAGTCCATCGATCGTACGATGCGTACGTTAGCCTAGGATCAGTCGATCGATCGTACG"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        original_sequence = t["original_sequence"]
        mutated_sequence = t["mutated_sequence"]
        return f"""Analyze the following DNA sequences to identify the mutation and explain its potential impact on the resulting protein function.

Original Sequence: {original_sequence}
Mutated Sequence: {mutated_sequence}

Identify the type of mutation (e.g., point mutation, insertion, deletion) and predict how this change might affect the protein that the gene encodes. Consider changes in amino acid sequence, potential loss of function, or gain of function.

Submit your analysis in the following format:
1. Type of Mutation: [Your identification of the mutation]
2. Impact on Protein Function: [Your detailed explanation of the potential impact]

Ensure your response is detailed and scientifically accurate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly identify the type of mutation.", "The response should accurately describe the potential impact on protein function.", "The analysis should be scientifically valid and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
