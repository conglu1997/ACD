class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"narrative": "In a distant future, humanity has colonized Mars. Amidst the red deserts, a young scientist named Aria discovers an ancient Martian artifact that hints at a lost civilization. As she delves deeper, she faces opposition from her superiors who want to exploit the artifact for its energy potential. Torn between her duty and her curiosity, Aria must decide the fate of the artifact.", "questions": ["What is the central conflict in the narrative?", "Describe the character of Aria and her motivations.", "What themes are explored in this narrative?"]},
            "2": {"narrative": "In a small village surrounded by enchanted forests, a young boy named Leo discovers he has the ability to communicate with animals. As he befriends a wise old owl, he learns of a dark force threatening the forest. With the help of his animal friends, Leo embarks on a quest to save his home. Along the way, he learns valuable lessons about bravery and friendship.", "questions": ["What is the central conflict in the narrative?", "Describe the character of Leo and his development throughout the story.", "What themes are explored in this narrative?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following fictional narrative and answer the questions provided. Ensure your response is detailed and addresses each question thoroughly. Submit your response in the following format:

Narrative: {t['narrative']}

1. {t['questions'][0]}
2. {t['questions'][1]}
3. {t['questions'][2]}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should address each question in a detailed and coherent manner.", "The analysis should demonstrate an understanding of the narrative's conflict, characters, and themes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
