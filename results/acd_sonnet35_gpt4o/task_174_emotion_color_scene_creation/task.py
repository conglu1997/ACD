class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"emotion": "melancholy", "description": "a feeling of pensive sadness, typically with no obvious cause"},
            {"emotion": "euphoria", "description": "a feeling or state of intense excitement and happiness"},
            {"emotion": "serenity", "description": "the state of being calm, peaceful, and untroubled"},
            {"emotion": "anxiety", "description": "a feeling of worry, nervousness, or unease about something with an uncertain outcome"}
        ]
        import random
        selected_emotions = random.sample(emotions, 2)
        return {
            "1": selected_emotions[0],
            "2": selected_emotions[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a 'mood palette' and scene description based on the emotion: {t['emotion']} ({t['description']})

        Your task is to:
        1. Create a color palette of 5 colors that represent the given emotion. For each color, provide:
           a) The color name
           b) Its hexadecimal code
           c) A brief explanation of why this color represents the emotion (1-2 sentences)
        2. Justify the order of colors in your palette based on color theory principles (2-3 sentences)

        3. Using only the colors from your palette, describe a scene that evokes the given emotion. Your description should:
           a) Be 100-150 words long
           b) Use vivid, sensory language
           c) Explicitly mention how each color from your palette is used in the scene
           d) Evoke the given emotion without explicitly naming it

        4. Explain how your scene and color choices reflect principles of color theory and emotional psychology (2-3 sentences)

        5. Describe how viewing this scene might affect a person's emotional state (2-3 sentences)

        Format your response as follows:

        Emotion: {t['emotion']}

        Color Palette:
        1. [Color Name] (Hex: #------)
           [Explanation]
        2. [Color Name] (Hex: #------)
           [Explanation]
        3. [Color Name] (Hex: #------)
           [Explanation]
        4. [Color Name] (Hex: #------)
           [Explanation]
        5. [Color Name] (Hex: #------)
           [Explanation]

        Palette Order Justification:
        [Your 2-3 sentence justification]

        Scene Description:
        [Your 100-150 word scene description]

        Color Theory and Emotional Psychology Explanation:
        [Your 2-3 sentence explanation]

        Emotional Impact on Viewer:
        [Your 2-3 sentence description]
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The color palette contains exactly 5 colors with names, valid hexadecimal codes, and explanations.",
            "The palette order is justified using color theory principles.",
            "The scene description is 100-150 words long and uses all 5 colors from the palette.",
            "The scene evokes the given emotion without explicitly naming it.",
            "The explanation demonstrates understanding of color theory and emotional psychology principles.",
            "The emotional impact on the viewer is described.",
            "The response follows the specified format exactly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
