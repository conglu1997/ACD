import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            {
                "function": "Working Memory",
                "description": "Temporary storage and manipulation of information",
                "brain_region": "Prefrontal cortex"
            },
            {
                "function": "Attention",
                "description": "Focusing on specific stimuli while ignoring others",
                "brain_region": "Fronto-parietal network"
            },
            {
                "function": "Emotional Regulation",
                "description": "Managing and responding to emotional experiences",
                "brain_region": "Limbic system and prefrontal cortex"
            },
            {
                "function": "Language Processing",
                "description": "Comprehension and production of language",
                "brain_region": "Broca's and Wernicke's areas"
            }
        ]
        return {
            "1": random.choice(cognitive_functions),
            "2": random.choice(cognitive_functions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on neurocognitive principles to enhance {t['function']}. Then, analyze its potential impact on cognitive function and broader implications. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI music composition system.
   b) Explain how it incorporates principles from cognitive neuroscience, particularly related to {t['function']}.
   c) Detail how your system translates neural patterns associated with {t['function']} into musical elements.
   d) Discuss any novel approaches or algorithms you've incorporated to handle the complexity of this task.

2. Composition Process (200-250 words):
   a) Outline the step-by-step process your AI system uses to compose music.
   b) Explain how specific musical elements (e.g., rhythm, harmony, timbre) are chosen to target {t['function']}.
   c) Describe how your system adapts the composition based on real-time neural feedback.

3. Neuroscientific Basis (200-250 words):
   a) Discuss the current understanding of how music affects {t['function']}.
   b) Explain how your system's approach is grounded in neuroscientific research.
   c) Describe how your system might interact with the {t['brain_region']}.

4. Potential Cognitive Enhancement (200-250 words):
   a) Hypothesize how your AI-composed music could enhance {t['function']}.
   b) Propose a method to measure the cognitive effects of your system's music.
   c) Discuss potential limitations or risks associated with using music to enhance cognitive functions.

5. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns related to cognitive enhancement through AI-composed music.
   b) Discuss broader societal impacts if such technology becomes widely available.
   c) Propose guidelines for responsible development and use of neurocognitive music AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Propose a related research question that could further our understanding of music, cognition, and AI.
   c) Discuss how this technology might evolve in the next decade and its potential applications.

Ensure your response demonstrates a deep understanding of music theory, cognitive neuroscience, and artificial intelligence. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and accuracy.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of music theory, cognitive neuroscience, and artificial intelligence, and their integration.",
            "The proposed AI system architecture is well-defined and incorporates relevant neurocognitive principles.",
            "The composition process is clearly explained and shows a logical connection between musical elements and cognitive function.",
            "The neuroscientific basis is well-researched and accurately presented.",
            "The potential cognitive enhancement effects are plausibly hypothesized and include a viable measurement method.",
            "Ethical and societal implications are thoughtfully analyzed.",
            "Future research directions are innovative and relevant.",
            "The overall response is coherent, well-structured, and demonstrates strong interdisciplinary reasoning.",
            "The response adheres to the specified word limits for each section and does not exceed 1450 words in total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
