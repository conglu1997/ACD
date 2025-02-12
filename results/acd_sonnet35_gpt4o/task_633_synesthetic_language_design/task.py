import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_element": "Phonemes",
                "sensory_modality": "Color",
                "cognitive_aspect": "Memory"
            },
            {
                "linguistic_element": "Syntax",
                "sensory_modality": "Texture",
                "cognitive_aspect": "Attention"
            },
            {
                "linguistic_element": "Semantics",
                "sensory_modality": "Taste",
                "cognitive_aspect": "Emotional processing"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synesthetic language system that maps the linguistic element of {t['linguistic_element']} to the sensory modality of {t['sensory_modality']}, analyze its cognitive implications, and explore its potential applications in AI development, with a focus on the cognitive aspect of {t['cognitive_aspect']}. Your response should include:

1. Synesthetic Language Design (250-300 words):
   a) Explain the core principles of your synesthetic language system.
   b) Describe how {t['linguistic_element']} are mapped to {t['sensory_modality']} experiences.
   c) Provide 3-5 example sentences or expressions in your language with their sensory interpretations.
   d) Explain how your system maintains linguistic coherence while incorporating sensory elements.

2. Cognitive Implications (200-250 words):
   a) Analyze how your language might influence speakers' cognitive processes, particularly {t['cognitive_aspect']}.
   b) Discuss potential effects on perception and information processing.
   c) Explore how this language might shape other aspects of cognition or experience.

3. AI Applications (200-250 words):
   a) Propose how your synesthetic language design could be applied to AI systems.
   b) Explain the potential benefits and challenges of this application, especially in relation to {t['cognitive_aspect']}.
   c) Discuss how it might advance current AI capabilities in natural language processing or multimodal learning.

4. Comparative Analysis (150-200 words):
   a) Compare your synesthetic language's approach to existing forms of synesthesia in humans.
   b) Discuss any similarities or differences with other constructed languages or formal systems that incorporate sensory elements.

5. Experimental Design (150-200 words):
   a) Propose an experiment to test the cognitive effects of your synesthetic language on human subjects, focusing on {t['cognitive_aspect']}.
   b) Outline the methodology, including how you would measure both linguistic comprehension and sensory experiences.
   c) Describe expected outcomes and potential implications for cognitive science and AI research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, synesthesia, and artificial intelligence principles. Be creative in your language design while maintaining scientific plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes a synesthetic language system mapping {t['linguistic_element']} to {t['sensory_modality']}",
            "The language design is creative, coherent, and scientifically plausible",
            f"The cognitive implications section thoroughly analyzes the impact on {t['cognitive_aspect']}",
            "The AI applications proposed are innovative and relevant to the language design",
            "The comparative analysis demonstrates understanding of human synesthesia and other relevant systems",
            f"The experimental design is well-structured and focuses on testing effects related to {t['cognitive_aspect']}",
            "The response shows deep understanding of linguistics, cognitive science, synesthesia, and AI principles",
            "The response is well-structured, following the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
