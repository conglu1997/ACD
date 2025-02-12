import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = ['rhythm', 'melody', 'harmony', 'timbre']
        cognitive_processes = ['auditory scene analysis', 'expectation', 'emotion', 'memory']
        musical_cultures = ['Western classical', 'West African', 'Indian classical', 'Chinese traditional']
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'musical_element': random.choice(musical_elements),
                'cognitive_process': random.choice(cognitive_processes),
                'musical_culture': random.choice(musical_cultures)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models human music cognition and applies it to generate culturally adaptive musical compositions. Your system should focus on the musical element of {t['musical_element']}, the cognitive process of {t['cognitive_process']}, and be able to generate music in the style of {t['musical_culture']} music. Your response should include:

1. Cognitive-Musical Model (250-300 words):
   a) Explain how the specified cognitive process ({t['cognitive_process']}) relates to music perception and creation.
   b) Describe how you would model this cognitive process in an AI system.
   c) Discuss how this model would interact with the musical element of {t['musical_element']}.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI music cognition and composition system.
   b) Explain how your system integrates the cognitive-musical model with music generation techniques.
   c) Describe how your system would learn and apply the stylistic elements of {t['musical_culture']} music.

3. Cultural Adaptation Mechanism (200-250 words):
   a) Explain how your AI system would adapt its output to align with {t['musical_culture']} musical traditions.
   b) Discuss potential challenges in modeling cross-cultural musical elements and how you would address them.
   c) Describe a method for evaluating the cultural authenticity of the generated compositions.

4. Composition Process (200-250 words):
   a) Provide a step-by-step explanation of how your AI system would compose a short musical piece.
   b) Explain how the cognitive process of {t['cognitive_process']} influences each stage of composition.
   c) Describe how the system would handle creative decision-making during the composition process.

5. Implications and Analysis (200-250 words):
   a) Discuss how your AI system might contribute to our understanding of human music cognition.
   b) Explain potential implications of your system for music theory and composition techniques.
   c) Analyze how AI-generated music might impact cultural preservation and evolution in {t['musical_culture']} traditions.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI-generated music and cultural appropriation.
   b) Propose guidelines for the responsible development and use of AI in music composition.
   c) Discuss the potential impact of your system on human musicians and composers.

7. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your AI music cognition and composition system.
   b) Propose an experiment to test a key aspect of your system's cognitive-musical model.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific and cultural plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence",
            "The AI system design effectively integrates the specified musical element, cognitive process, and cultural style",
            "The cultural adaptation mechanism is well-explained and addresses potential challenges",
            "The composition process is clearly described and incorporates the cognitive process effectively",
            "The implications for music theory and cognitive science are thoughtfully analyzed",
            "Ethical considerations are thoroughly addressed with proposed guidelines",
            "The response is creative and innovative while maintaining scientific and cultural plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
