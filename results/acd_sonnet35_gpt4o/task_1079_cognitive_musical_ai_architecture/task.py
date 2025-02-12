import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "working memory",
            "pattern recognition",
            "emotional processing",
            "analogical reasoning",
            "auditory processing"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre",
            "form"
        ]
        ai_techniques = [
            "neural networks",
            "reinforcement learning",
            "generative models",
            "knowledge representation",
            "evolutionary algorithms"
        ]
        musical_traditions = [
            "Western classical",
            "Indian classical",
            "West African",
            "Chinese traditional",
            "Middle Eastern"
        ]
        return {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements),
                "ai_technique": random.choice(ai_techniques),
                "musical_tradition": random.choice(musical_traditions)
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements),
                "ai_technique": random.choice(ai_techniques),
                "musical_tradition": random.choice(musical_traditions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive architecture for an AI system capable of musical creativity and analysis, integrating principles from cognitive science, artificial intelligence, and music theory. Your architecture should focus on the cognitive process of {t['cognitive_process']}, the musical element of {t['musical_element']}, and incorporate the AI technique of {t['ai_technique']}. The system should be specialized for the {t['musical_tradition']} musical tradition, while also considering cross-cultural aspects of musical creativity.

Your response should include:

1. Conceptual Framework (200-250 words):
   a) Explain how {t['cognitive_process']} relates to musical creativity and perception in {t['musical_tradition']}.
   b) Describe how {t['musical_element']} can be represented and manipulated in an AI system for {t['musical_tradition']}.
   c) Discuss how {t['ai_technique']} can be applied to musical tasks in {t['musical_tradition']}.
   d) Address how your framework considers cross-cultural aspects of musical creativity.

2. Architecture Design (250-300 words):
   a) Provide a high-level overview of your cognitive AI architecture for musical creativity in {t['musical_tradition']}.
   b) Explain how {t['cognitive_process']}, {t['musical_element']}, and {t['ai_technique']} are integrated into the architecture.
   c) Describe the key components and their interactions within the system.
   d) Include a visual representation (ASCII diagram) of your architecture, showing the main components and their relationships.

3. Functional Processes (200-250 words):
   a) Detail how your architecture would approach a specific musical task in {t['musical_tradition']} (e.g., composition, improvisation, or analysis).
   b) Explain the role of {t['cognitive_process']} in this task.
   c) Describe how {t['musical_element']} is processed or generated.
   d) Provide a step-by-step example of the system generating a short musical phrase in {t['musical_tradition']}.

4. Learning and Adaptation (150-200 words):
   a) Explain how your architecture could learn and improve its musical capabilities in {t['musical_tradition']} over time.
   b) Discuss how {t['ai_technique']} contributes to this learning process.
   c) Propose a specific experiment to test the system's learning capabilities across different musical traditions.

5. Evaluation and Creativity Assessment (150-200 words):
   a) Propose methods to evaluate the musical output and creativity of your AI system in {t['musical_tradition']}.
   b) Discuss how you would measure the system's understanding and use of {t['musical_element']}.
   c) Address the challenges of assessing machine creativity in music, specifically in {t['musical_tradition']}.
   d) Suggest a novel metric for quantifying the system's creativity that considers cross-cultural aspects.

6. Ethical Implications (100-150 words):
   a) Discuss potential ethical concerns related to your AI system's impact on human musicians and musical traditions.
   b) Address issues of cultural appropriation and preservation in AI-generated music.
   c) Propose guidelines for responsible development and use of your system.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and music theory, particularly as they relate to {t['musical_tradition']}. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.

Format your response with clear headings for each section and include the ASCII diagram in the Architecture Design section. Adhere to the word limits for each section. Your total response should be between 1050-1350 words, excluding the ASCII diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['cognitive_process']} and its relation to musical creativity in {t['musical_tradition']}.",
            f"The architecture effectively incorporates {t['musical_element']} and explains its representation and manipulation in {t['musical_tradition']}.",
            f"The AI technique of {t['ai_technique']} is well-integrated and its application to musical tasks in {t['musical_tradition']} is clearly explained.",
            "The response shows a deep understanding of cognitive science, AI, and music theory principles, particularly in relation to the specified musical tradition.",
            "The proposed evaluation methods for musical output and creativity are relevant, well-thought-out, and specific to the given musical tradition.",
            "The ASCII diagram effectively communicates the architecture's structure and component relationships.",
            "The step-by-step example of generating a musical phrase in the specified tradition is clear and demonstrates the system's functionality.",
            "The proposed experiment to test the system's learning capabilities across different musical traditions is well-designed and relevant.",
            "The suggested novel metric for quantifying creativity considers cross-cultural aspects and is well-justified.",
            "The discussion of ethical implications is thoughtful and addresses cultural appropriation and preservation issues.",
            "The response adheres to the specified word limits for each section and demonstrates concise, focused writing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
