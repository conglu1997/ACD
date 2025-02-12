import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "auditory cortex",
            "prefrontal cortex",
            "hippocampus",
            "amygdala",
            "cerebellum"
        ]
        musical_elements = [
            "rhythm",
            "melody",
            "harmony",
            "timbre",
            "dynamics"
        ]
        ai_techniques = [
            "recurrent neural networks",
            "transformer models",
            "generative adversarial networks",
            "reinforcement learning",
            "evolutionary algorithms"
        ]
        therapeutic_applications = [
            "stress reduction",
            "cognitive enhancement",
            "mood regulation",
            "pain management",
            "motor rehabilitation"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "ai_technique": random.choice(ai_techniques),
                "therapeutic_application": random.choice(therapeutic_applications)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "ai_technique": random.choice(ai_techniques),
                "therapeutic_application": random.choice(therapeutic_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that synthesizes musical compositions based on neural activity patterns from the {t['brain_region']}, focusing on the musical element of {t['musical_element']}. Your system should use {t['ai_technique']} as its primary AI approach. Then, analyze its output in terms of musical theory and potential applications in {t['therapeutic_application']}. Your response should demonstrate strong interdisciplinary integration across neuroscience, AI, music theory, and therapeutic applications.

Include the following sections:

1. Neuroscientific Basis (250-300 words):
   a) Explain the role of the {t['brain_region']} in music perception and processing.
   b) Describe how neural activity in this region relates to {t['musical_element']}.
   c) Discuss challenges in translating neural signals to musical parameters.
   d) Propose a novel hypothesis about the relationship between {t['brain_region']} activity and musical creativity.

2. AI System Architecture (300-350 words):
   a) Design an AI system that uses {t['ai_technique']} to generate music based on neural activity.
   b) Explain how your system processes neural data and converts it into musical parameters.
   c) Describe how the system ensures the generated music maintains coherence and structure.
   d) Discuss potential limitations of using {t['ai_technique']} for this task and how you might address them.
   e) Include a high-level diagram or pseudocode to illustrate your system's design.

3. Music Theory Analysis (250-300 words):
   a) Analyze how your system's output relates to traditional music theory concepts.
   b) Discuss how the focus on {t['musical_element']} influences the overall musical structure.
   c) Compare the potential musical qualities of your AI-generated compositions to human-composed music.
   d) Propose a novel music theory concept that could emerge from your AI system's compositions.

4. Therapeutic Application (200-250 words):
   a) Explain how your system's output could be used for {t['therapeutic_application']}.
   b) Describe a potential experimental setup to test the efficacy of your AI-generated music in this therapeutic context.
   c) Discuss ethical considerations in using AI-generated music for therapy.
   d) Propose a mechanism by which the AI-generated music might influence neural activity to achieve therapeutic effects.

5. Evaluation and Future Directions (200-250 words):
   a) Propose methods to evaluate the quality and effectiveness of your AI-generated music.
   b) Discuss potential limitations of your approach and suggest improvements.
   c) Explore how this technology could advance our understanding of the relationship between brain activity and music.
   d) Suggest a groundbreaking experiment that combines your AI system with brain-computer interfaces for real-time music generation and therapy.

Ensure your response demonstrates a deep understanding of all involved disciplines. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the specified brain region ({t['brain_region']}) and its role in music perception and processing.",
            f"The AI system design uses {t['ai_technique']} as its primary approach.",
            f"The music theory analysis focuses on the musical element of {t['musical_element']}.",
            f"The therapeutic application section discusses the use of AI-generated music for {t['therapeutic_application']}.",
            "The response includes all five required sections: Neuroscientific Basis, AI System Architecture, Music Theory Analysis, Therapeutic Application, and Evaluation and Future Directions.",
            "The AI system design demonstrates a plausible method for translating neural activity into musical parameters.",
            "The music theory analysis shows understanding of how AI-generated music relates to traditional music theory concepts.",
            "The therapeutic application discussion includes a potential experimental setup and addresses ethical considerations.",
            "The evaluation section proposes methods to assess the quality and effectiveness of the AI-generated music.",
            "The response includes at least one novel hypothesis or concept.",
            "The response demonstrates interdisciplinary integration across neuroscience, AI, music theory, and therapeutic applications.",
            "The total word count is between 1200-1450 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
