class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The importance of renewable energy"
            },
            "2": {
                "essay": "School uniforms should be mandatory in all schools. Uniforms create a sense of equality and belonging among students, reducing peer pressure and bullying. They also save time in the morning, as students do not have to decide what to wear. Furthermore, uniforms are cost-effective for parents, reducing the need for multiple outfits."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "topic" in t:
            return f"""Write a persuasive essay on the following topic: {t['topic']}. Your essay should be well-structured with a clear introduction, body, and conclusion. Use logical arguments, evidence, and rhetorical devices to persuade the reader of your viewpoint. Ensure coherence and logical flow throughout the essay. Your essay should be at least 300 words long. Submit your essay as a plain text string labeled as follows:

Essay:
[Your essay]"""
        else:
            return f"""Analyze the following persuasive essay for its effectiveness. Discuss the strengths and weaknesses of the essay's arguments, structure, and use of rhetorical devices. Provide specific examples to support your analysis. Submit your analysis as a plain text string labeled as follows:

Analysis:
[Your analysis]

Essay: {t['essay']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "topic" in t:
            validation_criteria = [
                "The essay should have a clear introduction, body, and conclusion.",
                "The arguments should be logical and well-supported with evidence.",
                "The essay should use rhetorical devices effectively to persuade the reader.",
                "The essay should be at least 300 words long.",
                "The essay should ensure coherence and logical flow."
            ]
        else:
            validation_criteria = [
                "The analysis should discuss the strengths and weaknesses of the essay's arguments.",
                "The analysis should evaluate the structure and use of rhetorical devices.",
                "The analysis should provide specific examples to support the evaluation."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
