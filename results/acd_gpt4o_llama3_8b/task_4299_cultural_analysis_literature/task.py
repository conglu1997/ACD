class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"excerpt": "In Mark Twain's 'The Adventures of Huckleberry Finn,' Huck and Jim travel down the Mississippi River. Discuss the cultural significance of the river in the context of American history and society. How does the river function as a symbol in the narrative? Avoid superficial analysis."},
            "2": {"excerpt": "In Chinua Achebe's 'Things Fall Apart,' the protagonist Okonkwo grapples with the changes brought by colonialism. Analyze the cultural clash depicted in the novel and discuss how Achebe portrays the impact of colonialism on traditional Igbo society. Provide an in-depth analysis."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given literary excerpt and provide insights into the cultural context and themes. Your analysis should include the following:\n1. A discussion of the cultural significance of the elements mentioned in the excerpt.\n2. An interpretation of the themes presented and their relevance to the cultural context.\n3. A coherent and well-rounded analysis that ties together the cultural and thematic aspects.\n4. Avoid superficial analysis and ensure depth in your discussion.\n\nExcerpt:\n{t['excerpt']}\n\nSubmit your response as a plain text string in the following format:\n\nAnalysis: [Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should discuss the cultural significance of the elements mentioned.", "The themes presented should be interpreted and tied to the cultural context.", "The analysis should be coherent and well-rounded.", "The analysis should avoid superficial discussion and provide depth."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
