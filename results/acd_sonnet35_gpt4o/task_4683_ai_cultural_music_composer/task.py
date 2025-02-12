import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_traditions = [
            {
                'tradition': 'Indian Classical',
                'key_elements': 'Raga, Tala, Drone',
                'emotional_associations': 'Spirituality, Devotion, Tranquility',
                'example_pattern': 'Sa Re Ga Ma Pa Dha Ni Sa'
            },
            {
                'tradition': 'West African',
                'key_elements': 'Polyrhythms, Call and Response, Pentatonic scales',
                'emotional_associations': 'Community, Joy, Ancestral connection',
                'example_pattern': '12/8 rhythm: 1 2 3 4 5 6 7 8 9 10 11 12'
            }
        ]
        
        target_emotions = [
            'Nostalgia',
            'Excitement'
        ]
        
        tasks = [
            {
                'musical_tradition': musical_traditions[0],
                'target_emotion': target_emotions[0],
                'contrast_tradition': musical_traditions[1]
            },
            {
                'musical_tradition': musical_traditions[1],
                'target_emotion': target_emotions[1],
                'contrast_tradition': musical_traditions[0]
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates culturally-informed musical compositions based on the {t['musical_tradition']['tradition']} tradition and analyzes their emotional impact, with a focus on evoking the emotion of {t['target_emotion']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system incorporates key elements of {t['musical_tradition']['tradition']} music ({t['musical_tradition']['key_elements']}).
   c) Detail how the system models and generates emotional content in music.
   d) Include a simple ASCII diagram or flowchart of your system architecture.
   e) Provide a high-level pseudocode (10-15 lines) for the main composition generation algorithm.

2. Cultural-Musical Knowledge Representation (250-300 words):
   a) Explain how your AI system represents and utilizes cultural knowledge about {t['musical_tradition']['tradition']} music.
   b) Describe how it captures the relationship between musical elements and emotional associations in this tradition.
   c) Discuss any challenges in representing complex cultural musical concepts in an AI system.
   d) Propose a data structure to represent the musical pattern: {t['musical_tradition']['example_pattern']}

3. Composition Generation Process (250-300 words):
   a) Outline the step-by-step process your AI uses to generate a composition in the {t['musical_tradition']['tradition']} style.
   b) Explain how it incorporates techniques to evoke the emotion of {t['target_emotion']}.
   c) Describe any creative or adaptive elements in your generation process.
   d) Propose a novel musical element that combines aspects of {t['musical_tradition']['tradition']} with the emotion of {t['target_emotion']}.
   e) Provide a concrete example of how your AI system would generate a short musical phrase (4-8 measures) in the {t['musical_tradition']['tradition']} style to evoke {t['target_emotion']}. Use standard musical notation or a clear textual representation.

4. Emotional Impact Analysis (200-250 words):
   a) Propose methods for your AI to analyze the emotional impact of its generated compositions.
   b) Explain how it would assess whether the composition successfully evokes {t['target_emotion']}.
   c) Discuss how your system accounts for cultural differences in emotional perception of music.
   d) Provide a sample output of your AI's emotional analysis for the musical phrase you generated in section 3.

5. Cross-Cultural Application (250-300 words):
   a) Describe how your system could be adapted to generate music in the {t['contrast_tradition']['tradition']} tradition.
   b) Compare and contrast how {t['musical_tradition']['tradition']} and {t['contrast_tradition']['tradition']} music express emotions, particularly {t['target_emotion']}.
   c) Discuss potential challenges in translating emotional content across these diverse musical cultures.
   d) Propose an experiment to test the emotional impact of your AI's compositions across audiences from both cultural backgrounds.
   e) Suggest a method for quantifying cross-cultural emotional resonance.

6. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to generate culturally-specific music.
   b) Address concerns about cultural appropriation and authenticity.
   c) Propose guidelines for responsible development and use of your AI system.
   d) Discuss potential biases in your AI system and how to mitigate them.

7. Future Developments (150-200 words):
   a) Suggest two potential improvements or extensions to your AI music composition system.
   b) Discuss how advancements in AI or music theory might enhance cultural music generation in the future.
   c) Propose a novel research question that arises from your AI system design.

Ensure your response demonstrates a deep understanding of music theory, cultural anthropology, emotional psychology, and AI system design. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and scientific plausibility.

Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1550-1900 words. Maintain internal consistency across all sections of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['musical_tradition']['tradition']} music and how to evoke the emotion of {t['target_emotion']}.",
            "The AI system design is innovative, coherent, and effectively integrates cultural knowledge with music generation capabilities.",
            "The proposed composition generation process includes a novel musical element that combines traditional aspects with the target emotion.",
            "A concrete example of a short musical phrase generation is provided, along with its emotional analysis.",
            f"The cross-cultural application section effectively compares and contrasts {t['musical_tradition']['tradition']} and {t['contrast_tradition']['tradition']} in terms of emotional expression.",
            "The response thoroughly addresses ethical considerations, including potential biases and mitigation strategies.",
            "The future developments section proposes a novel and relevant research question.",
            "The response maintains internal consistency across all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
