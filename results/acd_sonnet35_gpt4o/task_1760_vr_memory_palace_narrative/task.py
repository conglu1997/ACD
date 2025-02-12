import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_types = [
            "Episodic memory",
            "Semantic memory"
        ]
        narrative_themes = [
            "Historical events",
            "Scientific concepts"
        ]
        vr_environments = [
            "Ancient Greek city",
            "Futuristic space station"
        ]
        return {
            "1": {
                "memory_type": random.choice(memory_types),
                "narrative_theme": random.choice(narrative_themes),
                "vr_environment": random.choice(vr_environments)
            },
            "2": {
                "memory_type": random.choice(memory_types),
                "narrative_theme": random.choice(narrative_themes),
                "vr_environment": random.choice(vr_environments)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system that allows users to create personalized memory palaces, then use it to construct a narrative experience that enhances long-term memory formation. Your task focuses on the following parameters:

Memory Type: {t['memory_type']}
Narrative Theme: {t['narrative_theme']}
VR Environment: {t['vr_environment']}

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your VR memory palace system.
   b) Explain how the system incorporates principles of {t['memory_type']}.
   c) Detail how the system allows users to create and customize their memory palaces.
   d) Discuss any novel features that enhance memory formation and retrieval.

2. Narrative Design (200-250 words):
   a) Outline a narrative experience based on the theme "{t['narrative_theme']}" within the VR environment of a {t['vr_environment']}.
   b) Explain how this narrative integrates with the memory palace concept.
   c) Describe how the narrative elements enhance memory encoding and retrieval.
   d) Provide an example of how a specific piece of information would be memorized using your system.

3. Cognitive Mechanisms (200-250 words):
   a) Analyze how your system leverages cognitive principles to enhance memory formation.
   b) Explain the role of spatial cognition in your memory palace design.
   c) Discuss how the narrative elements interact with memory processes.
   d) Predict potential cognitive benefits or challenges of using your system.

4. User Experience (150-200 words):
   a) Describe the user interface and interaction methods in your VR system.
   b) Explain how users navigate and manipulate their memory palaces.
   c) Discuss how the system provides feedback on memory formation and retrieval.

5. Technical Considerations (150-200 words):
   a) Identify key technical challenges in implementing your system.
   b) Propose solutions to these challenges using current or near-future VR technology.
   c) Discuss any limitations of current VR technology in realizing your full system design.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss potential benefits and risks of using VR for memory enhancement.
   b) Address privacy concerns related to storing personal memories in a virtual system.
   c) Explore potential applications of your system beyond individual memory improvement.

Ensure your response demonstrates a deep understanding of cognitive neuroscience, virtual reality technology, and narrative design. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['memory_type']}, virtual reality technology, and narrative design.",
            f"The proposed system effectively integrates {t['memory_type']}, the narrative theme of {t['narrative_theme']}, and the VR environment of a {t['vr_environment']}.",
            "The narrative design creatively enhances memory formation and retrieval.",
            "The response addresses technical challenges and ethical implications thoroughly.",
            "The overall design is innovative, scientifically plausible, and well-explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
