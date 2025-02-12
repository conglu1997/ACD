class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "Starry Night",
                "artist": "Vincent van Gogh",
                "description": "A swirling night sky over a small town with a prominent cypress tree in the foreground. The sky is filled with large, bright stars and a crescent moon. The brushstrokes are visible, adding a sense of movement and emotion to the scene. The town below is rendered in darker hues, with a church steeple standing out. The contrast between the turbulent sky and the quiet town creates a sense of dynamic tension. The painting uses a palette of blues and yellows, with the swirling patterns conveying a sense of turbulence and motion. The cypress tree in the foreground adds a vertical element that contrasts with the horizontal flow of the landscape."
            },
            "2": {
                "title": "Mona Lisa",
                "artist": "Leonardo da Vinci",
                "description": "A portrait of a woman with a mysterious smile. She is seated against a distant landscape with winding paths and a bridge. The use of sfumato technique creates soft transitions between colors and tones, giving the painting a lifelike quality. The woman's gaze and enigmatic smile have intrigued viewers for centuries, adding to the painting's allure. The background features a hazy, dreamlike quality that contrasts with the detailed rendering of the subject. The use of light and shadow in the painting adds depth and realism, with the subtle details of the subject's hands and face enhancing the lifelike appearance. The subject's attire and the background suggest a sense of timelessness and serenity."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and critique the following piece of art based on the provided description. Your critique should cover the following aspects:
1. Composition and use of space
2. Use of color and light
3. Emotional impact and mood
4. Historical and cultural context
5. Overall impression and personal interpretation

Title: {t['title']}
Artist: {t['artist']}
Description: {t['description']}

Format your response as follows:
1. Introduction
2. Composition and Use of Space
3. Use of Color and Light
4. Emotional Impact and Mood
5. Historical and Cultural Context
6. Overall Impression and Personal Interpretation
Your response should be detailed and well-structured, drawing on artistic knowledge and critical thinking skills. Ensure clarity and coherence in your writing. Each section should provide in-depth insights and use specific references to the description to support your critique."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an introduction, analysis of composition and use of space, use of color and light, emotional impact and mood, historical and cultural context, and overall impression and personal interpretation.",
            "The critique should be detailed, well-structured, and coherent.",
            "Each section should provide in-depth insights and use specific references to the description to support the critique.",
            "The critique should demonstrate an understanding of the artistic techniques mentioned in the description.",
            "The critique should provide a balanced analysis, covering both strengths and potential weaknesses of the artwork."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
