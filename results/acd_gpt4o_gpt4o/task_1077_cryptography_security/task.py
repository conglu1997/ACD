class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "explain", "algorithm": "RSA", "scenario": "key generation"},
            "2": {"type": "analyze", "scenario": "man in the middle attack", "context": "public key exchange"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'explain':
            return f"""Your task is to explain the {t['algorithm']} algorithm and implement its key generation process in pseudocode. Provide a detailed explanation of each step involved in the key generation process. Ensure your pseudocode is clear and logically structured. Provide your response in the following format:\n\n1. Explanation: [Detailed explanation of the algorithm]\n2. Pseudocode: [Pseudocode for the key generation process]\n\nExample (Note: This is a partial example and does not cover the full process):\nExplanation: The RSA algorithm involves the following steps...\nPseudocode:\n1. Choose two distinct prime numbers p and q..."""
        elif t['type'] == 'analyze':
            return f"""Your task is to analyze the given security scenario: {t['scenario']}. Describe the potential vulnerabilities and suggest measures to mitigate these risks in the context of {t['context']}. Provide a detailed analysis and practical recommendations. Provide your response in the following format:\n\n1. Vulnerabilities: [List and description of potential vulnerabilities]\n2. Mitigations: [List and description of measures to mitigate the risks]\n\nExample (Note: This is a partial example and does not cover all vulnerabilities or mitigations):\nVulnerabilities: A man in the middle attack can occur if...\nMitigations: To prevent this, use mutual authentication..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'explain':
            criteria = ["The explanation of the algorithm should be detailed and accurate.", "The pseudocode should be clear, logically structured, and correctly implement the key generation process."]
        elif t['type'] == 'analyze':
            criteria = ["The analysis should identify and describe potential vulnerabilities.", "The recommendations should be practical and effectively mitigate the risks."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
