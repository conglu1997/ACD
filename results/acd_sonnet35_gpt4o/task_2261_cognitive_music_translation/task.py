import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "Working Memory",
            "Selective Attention",
            "Cognitive Flexibility",
            "Emotional Regulation",
            "Pattern Recognition",
            "Divergent Thinking",
            "Decision Making",
            "Language Processing",
            "Spatial Reasoning",
            "Metacognition"
        ]
        musical_elements = [
            "Harmony",
            "Rhythm",
            "Melody",
            "Timbre",
            "Dynamics",
            "Form",
            "Texture",
            "Tonality",
            "Articulation",
            "Tempo"
        ]
        tasks = {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements),
                "direction": "cognitive_to_music"
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements),
                "direction": "music_to_cognitive"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of bidirectional translation between musical structures and cognitive processes, then apply it to analyze and generate music that represents specific mental states or cognitive phenomena. Focus on translating {t['cognitive_process']} to/from {t['musical_element']} in the direction of {t['direction']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for cognitive-music translation.
   b) Explain how your system represents and processes both cognitive and musical information.
   c) Detail the mechanisms used for bidirectional mapping between cognitive processes and musical elements.
   d) Discuss how your system ensures meaningful and coherent translations.

2. Translation Process (200-250 words):
   a) Outline the step-by-step process your AI system uses for the specified translation direction.
   b) Explain how the system selects relevant features from the source domain ({t['cognitive_process'] if t['direction'] == 'cognitive_to_music' else t['musical_element']}).
   c) Describe how these features are mapped to the target domain ({t['musical_element'] if t['direction'] == 'cognitive_to_music' else t['cognitive_process']}).
   d) Discuss any challenges specific to this particular cognitive-musical pairing and how your system addresses them.

3. Example Translation (200-250 words):
   a) Provide a detailed example of how your system would perform the specified translation.
   b) If translating from cognitive process to music, describe the musical output in technical terms.
   c) If translating from music to cognitive process, describe the inferred cognitive state or process.
   d) Explain how this translation captures key aspects of both the source and target domains.

4. Cognitive Science and Music Theory Insights (200-250 words):
   a) Analyze how your AI's approach to cognitive-music translation relates to current theories in cognitive science and music psychology.
   b) Discuss any novel insights your system might provide into the relationship between musical structures and cognitive processes.
   c) Propose a hypothesis about music cognition that could be tested using your AI system.

5. Applications and Implications (150-200 words):
   a) Suggest potential applications of your cognitive-music translation system in fields such as music therapy, cognitive enhancement, or AI-assisted composition.
   b) Discuss the implications of your system for our understanding of music perception and cognition.
   c) Consider potential ethical considerations in using AI to translate between cognitive processes and music.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence. Be creative in your system design and translation process while maintaining scientific plausibility. Adhere to the word limits for each section. Your total response should be between 1000-1250 words. Provide a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of both the specified cognitive process and musical element, as well as their potential relationships.",
            "The proposed AI system design is innovative, detailed, and scientifically plausible.",
            "The translation process is well-explained and logically sound, addressing the challenges of mapping between cognitive and musical domains.",
            "The example translation effectively illustrates the system's capabilities and the relationship between the cognitive process and musical element.",
            "The response provides insightful analysis of implications for cognitive science and music theory.",
            "The suggested applications and ethical considerations show critical thinking about the broader impacts of the technology.",
            "The response demonstrates creativity and novelty in the proposed system and its applications.",
            "The response maintains coherence and relevance throughout all sections and adheres to the specified word limits and total word count requirement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
