class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write an essay that synthesizes information from the fields of environmental science, economics, and sociology to discuss the impacts of climate change on urban development. Your essay should cover the following points:\n1. Environmental challenges posed by climate change for urban areas.\n2. Economic implications for urban development and infrastructure.\n3. Sociological effects on urban populations, including social equity and community resilience.\nEnsure your essay integrates perspectives from all three disciplines and provides a coherent, well-rounded discussion."},
            "2": {"prompt": "Write an essay that synthesizes information from the fields of psychology, education, and technology to explore the effects of digital learning tools on student engagement and learning outcomes. Your essay should cover the following points:\n1. Psychological theories on student motivation and engagement.\n2. Educational benefits and challenges of integrating digital tools in the classroom.\n3. Technological advancements and their potential impact on personalized learning.\nEnsure your essay integrates perspectives from all three disciplines and provides a coherent, well-rounded discussion."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nYour response should include:\n1. A comprehensive discussion that integrates perspectives from the specified academic disciplines.\n2. Clear and logical structuring of arguments.\n3. Coherent synthesis of information to provide a well-rounded perspective.\n\nSubmit your response as a plain text string in the following format:\n\nEssay: [Your essay here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The essay should integrate perspectives from the specified academic disciplines.", "The discussion should be comprehensive, well-rounded, and logically structured.", "The synthesis of information should be coherent and provide a clear perspective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
