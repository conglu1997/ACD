class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"title": "Understanding Quantum Entanglement", "abstract": "Quantum entanglement is a physical phenomenon that occurs when pairs or groups of particles are generated, interact, or share spatial proximity in ways such that the quantum state of each particle cannot be described independently of the state of the others, even when the particles are separated by a large distance."},
            "2": {"title": "CRISPR-Cas9 Gene Editing", "abstract": "The CRISPR-Cas9 system is a revolutionary method for editing genes. It allows scientists to alter DNA sequences and modify gene function. Its many potential applications include correcting genetic defects, treating and preventing the spread of diseases, and improving crops."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        title = t["title"]
        abstract = t["abstract"]
        instructions = f"""Your task is to analyze the following scientific abstract and provide a summary that includes the key points and an interpretation of the main concepts. The summary should be clear, concise, and accurately reflect the content of the abstract.

Title: {title}
Abstract: {abstract}

Provide your summary in plain text format, ensuring it is well-structured and insightful. Structure your response as follows:
1. Title
2. Summary
3. Key Points
4. Interpretation
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should accurately reflect the content of the abstract.",
            "The key points should be clearly identified and relevant.",
            "The interpretation should be insightful and demonstrate understanding of the main concepts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
