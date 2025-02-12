import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "Joy",
            "Sadness",
            "Anger",
            "Fear",
            "Surprise"
        ]
        musical_styles = [
            "Classical",
            "Jazz",
            "Electronic",
            "Folk",
            "Avant-garde"
        ]
        cognitive_principles = [
            "Neural resonance",
            "Predictive coding",
            "Gestalt principles",
            "Cognitive dissonance",
            "Embodied cognition"
        ]
        
        tasks = {}
        for i in range(2):
            emotion = random.choice(emotions)
            style = random.choice(musical_styles)
            principle = random.choice(cognitive_principles)
            
            tasks[str(i+1)] = {
                "emotion": emotion,
                "style": style,
                "principle": principle
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive model for musical harmony perception and use it to compose an original piece of music that elicits the emotion of {t['emotion']}. Your entire response must be your own original work, demonstrating creativity and innovation throughout. Your task has the following components:

1. Cognitive Model Design (300-350 words):
   a) Develop a cognitive model that explains how the brain perceives and processes musical harmony.
   b) Incorporate the cognitive principle of {t['principle']} into your model.
   c) Explain how your model accounts for the perception of consonance and dissonance.
   d) Describe how your model relates harmonic structures to emotional responses.
   e) Discuss any potential conflicts between the {t['principle']} principle and eliciting {t['emotion']}, and how you resolve them.
   f) Consider cross-cultural implications of your model, addressing how it might apply or differ across at least two distinct musical traditions.
   g) Discuss potential limitations of your cognitive model and areas for future research.

2. Harmonic Analysis (250-300 words):
   a) Analyze the harmonic structures commonly associated with {t['emotion']} in the {t['style']} musical style.
   b) Explain how these structures align with your cognitive model.
   c) Identify specific chord progressions or harmonic techniques that your model predicts would elicit {t['emotion']}.

3. Composition Framework (250-300 words):
   a) Develop a framework for composing music based on your cognitive model.
   b) Explain how this framework translates cognitive principles into musical elements.
   c) Describe how your framework ensures the composed music will elicit the target emotion.
   d) Discuss any constraints or guidelines your framework imposes on the composition process.
   e) Address potential limitations of your composition framework and suggest areas for improvement.

4. Musical Composition (200-250 words):
   a) Using your framework, outline a short, original musical piece in the {t['style']} style designed to elicit {t['emotion']}. Assume you have 30 minutes to complete this composition.
   b) Describe the key harmonic progressions and structures used in your composition.
   c) Explain how specific elements of your composition relate to your cognitive model.
   d) Provide a simple musical notation or diagram to illustrate a key part of your composition. This should be presented as ASCII art or a text-based representation, using standard musical notation symbols where possible (e.g., note names, chord symbols, time signatures). The representation should be clear enough for a musician to interpret.

5. Cognitive-Emotional Analysis (200-250 words):
   a) Analyze how your composition is likely to be processed by the brain according to your cognitive model.
   b) Predict the emotional responses at different points in the composition.
   c) Discuss potential individual or cultural variations in the perception of your composition, considering at least two different cultural contexts.

6. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness of your cognitive model and composition.
   b) Describe the methodology, including participant selection, stimuli presentation, and response measurement.
   c) Explain how you would analyze the results to validate or refine your cognitive model.
   d) Address how your experiment accounts for cultural differences in music perception and emotional response.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and emotion research across cultures. Use technical terminology appropriately and provide explanations where necessary. Be creative and original in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word count guidelines provided. Your total response should be between 1400-1700 words, not including the musical notation or diagram. Present the musical notation or diagram as ASCII art or a text-based representation within your response.

Note: Your response will be evaluated based on the quality, originality, and coherence of your cognitive model, the creativity and appropriateness of your musical composition, the depth of your analysis, and your consideration of cross-cultural factors. A perfect score requires meeting all criteria and demonstrating exceptional interdisciplinary integration, originality, and critical thinking. Partial credit may be given for responses that meet some but not all criteria."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of cognitive science principles, particularly {t['principle']}, and their application to music perception across cultures",
            "The cognitive model for musical harmony perception is well-developed, scientifically plausible, considers cross-cultural implications, and acknowledges its limitations",
            f"The harmonic analysis of {t['emotion']} in {t['style']} music is thorough and insightful",
            "The composition framework effectively translates cognitive principles into musical elements and addresses its potential limitations",
            f"The outlined musical composition in {t['style']} style is creative, original, and designed to elicit {t['emotion']} within the given time constraint",
            "The cognitive-emotional analysis of the composition is detailed, aligns with the proposed model, and considers cultural variations",
            "The experimental design to test the model and composition is well-thought-out, scientifically valid, and accounts for cultural differences",
            "The response demonstrates exceptional interdisciplinary integration of cognitive science, music theory, and emotion research across cultures",
            "The response includes appropriate technical terminology and clear explanations",
            "The response follows the specified format with clear headings and adheres to the provided word count guidelines",
            "The response includes a musical notation or diagram presented as ASCII art or a text-based representation, using standard musical notation symbols where possible",
            f"The response addresses potential conflicts between the {t['principle']} principle and eliciting {t['emotion']}",
            "The response is entirely original, demonstrates creativity throughout, and does not contain copied content from existing sources",
            "The response critically evaluates the proposed cognitive model and composition framework, identifying limitations and areas for future research"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
