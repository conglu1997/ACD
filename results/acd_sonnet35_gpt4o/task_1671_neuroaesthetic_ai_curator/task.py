import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "art_movement": "Abstract Expressionism",
                "neuroscience_principle": "Neuroaesthetics of color perception",
                "target_audience": "General public with no formal art education"
            },
            {
                "art_movement": "Surrealism",
                "neuroscience_principle": "Neural correlates of imagination and creativity",
                "target_audience": "Psychology students"
            },
            {
                "art_movement": "Renaissance",
                "neuroscience_principle": "Visual perception of depth and perspective",
                "target_audience": "Art history enthusiasts"
            },
            {
                "art_movement": "Impressionism",
                "neuroscience_principle": "Neural processing of light and shadow",
                "target_audience": "Aspiring artists"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that curates art exhibitions based on neuroscientific principles of aesthetic perception, focusing on the art movement of {t['art_movement']} and the neuroscience principle of {t['neuroscience_principle']}. Your system should be designed to create exhibitions for {t['target_audience']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI curatorial system.
   b) Explain how your system integrates art historical knowledge with neuroscientific principles.
   c) Discuss any novel elements in your design that enable realistic simulation of human aesthetic perception.
   d) Provide a high-level diagram or flowchart of your system's architecture (describe it textually).

2. Neuroscientific Foundation (200-250 words):
   a) Explain the chosen neuroscience principle and its relevance to aesthetic perception.
   b) Describe how your AI system models this principle computationally.
   c) Discuss potential limitations in applying neuroscientific principles to machine perception of art.

3. Art Historical Analysis (200-250 words):
   a) Provide a brief overview of the chosen art movement and its key characteristics.
   b) Explain how your AI system analyzes and categorizes artworks from this movement.
   c) Discuss how your system accounts for historical and cultural context in its analysis.

4. Curatorial Process (250-300 words):
   a) Describe the step-by-step process your AI system uses to curate an exhibition.
   b) Explain how the system balances neuroscientific principles with art historical significance.
   c) Discuss how your system adapts its curatorial choices for the specified target audience.
   d) Provide an example of how your system might select and arrange 3-5 specific artworks in an exhibition.

5. Visitor Experience Analysis (200-250 words):
   a) Predict how visitors might respond to an AI-curated exhibition based on neuroscientific principles.
   b) Discuss potential cognitive or emotional impacts on the target audience.
   c) Compare the expected visitor experience to that of traditionally curated exhibitions.

6. Ethical and Cultural Implications (150-200 words):
   a) Discuss potential ethical concerns of using AI to curate art exhibitions.
   b) Address how your system might impact the role of human curators and art historians.
   c) Consider potential cultural implications of applying neuroscientific principles to art appreciation.

7. Future Developments and Research (150-200 words):
   a) Propose two potential enhancements or extensions to your AI curatorial system.
   b) Suggest a research study to evaluate the effectiveness of your system in enhancing art appreciation.
   c) Speculate on how this technology might influence future art creation and art education.

Ensure your response demonstrates a deep understanding of neuroscience, art history, and artificial intelligence. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response comprehensively addresses the art movement of {t['art_movement']} and the neuroscience principle of {t['neuroscience_principle']}.",
            f"The AI system design is tailored for the target audience of {t['target_audience']}.",
            "The system architecture integrates art historical knowledge with neuroscientific principles in a novel and plausible way.",
            "The curatorial process is clearly explained, with a specific example of artwork selection and arrangement.",
            "The response demonstrates a deep understanding of neuroscience, art history, and artificial intelligence, using appropriate terminology throughout.",
            "Ethical and cultural implications of AI-curated art exhibitions are thoughtfully addressed.",
            "The proposed future developments and research directions are innovative and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
