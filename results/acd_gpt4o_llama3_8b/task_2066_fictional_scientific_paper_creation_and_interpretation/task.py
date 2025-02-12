class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "create_scientific_paper",
                "topic": "A new method for faster-than-light travel using quantum entanglement."
            },
            "2": {
                "task": "interpret_scientific_abstract",
                "abstract": "We present a novel approach to harnessing dark matter for energy production. Our experiments demonstrate that dark matter can be converted into a usable energy source through a process of quantum tunneling and particle collision. The implications of this discovery could revolutionize the energy sector and provide a near-limitless source of clean energy."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'create_scientific_paper':
            return f"Create a fictional scientific research paper on the following topic: {t['topic']}. The paper should include an abstract, introduction, methodology, results, and conclusion. Ensure the content is coherent, scientifically plausible, and follows the structure of a typical research paper. Your paper should strive to be innovative and engaging, and exhibit a deep understanding of the scientific principles involved. Submit your paper as a plain text string in the following format: 'Abstract: [Your abstract] Introduction: [Your introduction] Methodology: [Your methodology] Results: [Your results] Conclusion: [Your conclusion]'."
        elif t['task'] == 'interpret_scientific_abstract':
            return f"Interpret the following fictional scientific abstract: {t['abstract']}. Provide a summary of the main findings, the potential implications, and any assumptions or limitations you identify. Your interpretation should demonstrate a clear understanding of the scientific concepts and their broader impact. Submit your interpretation as a plain text string in the following format: 'Summary: [Your summary] Implications: [The potential implications] Assumptions: [Any assumptions or limitations]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'create_scientific_paper':
            validation_criteria = [
                "The paper should be coherent and follow the structure of a typical research paper (abstract, introduction, methodology, results, conclusion).",
                "The content should be scientifically plausible and innovative.",
                "The paper should be engaging and demonstrate a deep understanding of the scientific principles involved.",
                "The paper should be in the correct format: 'Abstract: [Your abstract] Introduction: [Your introduction] Methodology: [Your methodology] Results: [Your results] Conclusion: [Your conclusion]'."
            ]
        elif t['task'] == 'interpret_scientific_abstract':
            validation_criteria = [
                "The summary should accurately capture the main findings.",
                "The implications should be logically derived from the abstract.",
                "Any assumptions or limitations identified should be reasonable.",
                "The interpretation should be in the correct format: 'Summary: [Your summary] Implications: [The potential implications] Assumptions: [Any assumptions or limitations]'."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
