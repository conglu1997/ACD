class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "analyze", "story": "Once upon a time in a small village, there lived a young girl named Lily. She was known for her kindness and bravery. One day, she decided to venture into the dark forest to find a rare flower that could cure her sick mother. Along the way, she encountered numerous challenges but overcame them with her wit and courage. In the end, she found the flower and saved her mother, becoming a hero in her village.", "prompt": "Analyze the narrative structure, character development, and plot consistency of the story."},
            "2": {"task_type": "create", "themes": "friendship, adventure", "characters": "a young boy named Tom, a talking cat named Whiskers", "prompt": "Create a new story that incorporates the given themes and characters."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'analyze':
            return f"""Your task is to analyze the following story and provide insights into its narrative structure, character development, and plot consistency.\n\nStory: {t['story']}\n\nEnsure your analysis is detailed and covers the following aspects:\n- Narrative Structure: Describe the beginning, middle, and end of the story.\n- Character Development: Explain how the main character(s) evolve throughout the story.\n- Plot Consistency: Identify any plot holes or inconsistencies.\nProvide your response in the following format:\n\nAnalysis:\n- Narrative Structure: [Your analysis]\n- Character Development: [Your analysis]\n- Plot Consistency: [Your analysis]\n\nExample Analysis:\n- Narrative Structure: The story begins with an introduction of the main character, Lily, and her motivation. The middle includes her journey and challenges in the dark forest. The end resolves with her finding the flower and saving her mother, completing her character arc.\n- Character Development: Lily starts as a kind and brave girl, and through her journey, she demonstrates wit and courage, ultimately becoming a hero in her village.\n- Plot Consistency: The story is consistent with no noticeable plot holes."""
        elif t['task_type'] == 'create':
            return f"""Your task is to create a new story that incorporates the given themes and characters based on the following prompt:\n\nPrompt: {t['prompt']}\n\nThemes: {t['themes']}\nCharacters: {t['characters']}\n\nEnsure your story is vivid, engaging, and maintains narrative coherence. Provide your response in the following format:\n\nStory: [Your story]\n\nExample: For themes of friendship and adventure, an appropriate story could be 'Tom and Whiskers set out on a journey to find a hidden treasure. Along the way, they face numerous obstacles but their friendship helps them overcome each challenge. In the end, they find the treasure and realize that their bond is the true reward.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'analyze':
            criteria = ["The response should be formatted with headings for 'Narrative Structure', 'Character Development', and 'Plot Consistency'.", "The analysis must cover all three aspects in detail.", "The analysis must be relevant to the given story."]
        elif t['task_type'] == 'create':
            criteria = ["The response should be formatted as 'Story: [Your story]'.", "The story must incorporate the given themes and characters.", "The story must be engaging and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
