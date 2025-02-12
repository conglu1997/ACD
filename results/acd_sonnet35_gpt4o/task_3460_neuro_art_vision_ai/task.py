class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"art_style": "Impressionism", "neural_process": "visual perception"},
            "2": {"art_style": "Abstract Expressionism", "neural_process": "emotional processing"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design an AI system that bridges neuroscience, computer vision, and art history to analyze and generate visual art. Specifically, design an AI system that analyzes and generates visual art in the style of {t['art_style']}, based on neural patterns associated with {t['neural_process']}. Your system should incorporate principles from neuroscience, computer vision, and art history. Provide your response in the following format:

1. Neuroscientific Basis (200-250 words):
   a) Explain the neural patterns associated with {t['neural_process']} and how they relate to aesthetic appreciation.
   b) Describe how these patterns might influence the perception or creation of {t['art_style']} art.
   c) Discuss any relevant neuroscientific studies or theories that inform your approach.

2. Computer Vision Integration (200-250 words):
   a) Describe the computer vision techniques your AI system would use to analyze {t['art_style']} artworks.
   b) Explain how your system would extract relevant features and patterns from visual art.
   c) Discuss any novel algorithms or adaptations necessary for processing {t['art_style']} specifically.

3. Art Historical Context (200-250 words):
   a) Provide a brief overview of the key characteristics and historical context of {t['art_style']}.
   b) Explain how your AI system incorporates art historical knowledge in its analysis and generation processes.
   c) Discuss how your system ensures cultural and historical accuracy in its art generation.

4. AI System Architecture (200-250 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system integrates neuroscientific data, computer vision analysis, and art historical knowledge.
   c) Detail the process by which your system generates new artworks in the {t['art_style']} style.

5. Training and Data Requirements (200-250 words):
   a) Describe the types of data your system would need for training.
   b) Explain how you would acquire or generate this data, considering both neuroscientific and art historical aspects.
   c) Discuss any challenges in data acquisition or preprocessing for this task.

6. Evaluation Methodology (200-250 words):
   a) Propose methods to evaluate the effectiveness of your system in analyzing and generating {t['art_style']} artworks.
   b) Describe how you would assess both the neuroscientific accuracy and artistic quality of the system's outputs.
   c) Suggest ways to validate the system's art historical understanding.

7. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical implications of using AI to analyze and generate art.
   b) Address limitations of your approach, particularly in capturing the full complexity of human artistic creation.
   c) Propose guidelines for responsible use of your system in art analysis and generation.

Ensure your response demonstrates a deep understanding of neuroscience, computer vision, and art history. Use appropriate terminology from each field and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response fully addresses all 7 required sections.",
            "The answer demonstrates deep understanding and integration of neuroscience, computer vision, and art history.",
            "The proposed AI system is innovative yet scientifically plausible.",
            "The response uses appropriate terminology from all relevant fields.",
            "The answer is coherent, well-structured, and within the specified word count.",
            f"The response specifically addresses the art style of {t['art_style']} and the neural process of {t['neural_process']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
