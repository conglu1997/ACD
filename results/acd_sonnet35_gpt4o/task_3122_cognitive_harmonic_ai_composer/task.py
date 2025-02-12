import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_model": "Conceptual Metaphor Theory",
                "linguistic_structure": "Syntactic Trees",
                "musical_element": "Chord Progressions",
                "application": "Language Learning",
                "constraint": "Include at least one non-Western musical scale"
            },
            {
                "cognitive_model": "Construction Grammar",
                "linguistic_structure": "Semantic Frames",
                "musical_element": "Melodic Contours",
                "application": "Emotion Regulation",
                "constraint": "Incorporate microtonal intervals"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that composes music based on cognitive models of harmonic perception and linguistic structure, then analyze its output for cross-modal applications. Your system should incorporate the cognitive model of {t['cognitive_model']}, focus on the linguistic structure of {t['linguistic_structure']}, compose with emphasis on {t['musical_element']}, and aim for application in {t['application']}. Additional constraint: {t['constraint']}.\n\nYour response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the overall structure of your AI music composition system.\n   b) Explain how it incorporates the specified cognitive model in its design.\n   c) Detail how the system translates linguistic structures into musical elements.\n   d) Discuss how the system implements the specified musical focus and additional constraint.\n   e) Include a high-level diagram or flowchart of your system (describe it textually).\n\n2. Cognitive-Linguistic-Musical Interface (250-300 words):\n   a) Explain how your system maps linguistic structures to musical parameters.\n   b) Describe how these parameters are used to generate the specified musical elements.\n   c) Discuss any challenges in bridging cognitive linguistics and music theory, and how you address them.\n   d) Provide a specific example of how your system would compose a musical phrase based on a given linguistic input.\n\n3. AI Composition Process (250-300 words):\n   a) Detail the step-by-step process your AI system follows to compose a piece of music.\n   b) Explain how the system ensures coherence and structure in the composition.\n   c) Describe how the system balances linguistic fidelity with musical aesthetics.\n   d) Discuss any machine learning techniques or algorithms used in the composition process.\n\n4. Cross-modal Analysis (200-250 words):\n   a) Propose a method for analyzing the cross-modal effects of the AI-generated music on linguistic processing.\n   b) Describe how you would measure the effectiveness of the music in enhancing the specified application.\n   c) Discuss potential differences in cross-modal perception across different listener groups.\n\n5. Application in {t['application']} (250-300 words):\n   a) Explain how the AI-generated music could be used in the specified application.\n   b) Discuss potential benefits and challenges of using linguistically-informed AI-composed music in this context.\n   c) Propose a study design to test the effectiveness of the music in the given application.\n   d) Suggest two other potential applications for your cognitive harmonic AI composition system.\n\n6. Ethical Considerations (150-200 words):\n   a) Discuss ethical implications of using AI-generated music for cognitive or linguistic manipulation.\n   b) Address concerns about AI replacing human composers or devaluing human creativity.\n   c) Propose guidelines for the responsible development and use of cognitive-linguistic music AI systems.\n\n7. Future Developments (150-200 words):\n   a) Suggest potential improvements or extensions to your cognitive harmonic AI composition system.\n   b) Discuss how advancements in cognitive linguistics or AI could enhance such systems in the future.\n   c) Propose a novel research question that arises from the intersection of cognitive linguistics, AI, and music theory.\n\nEnsure your response demonstrates a deep understanding of cognitive linguistics, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific and artistic plausibility.\n\nFormat your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1550-1900 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['cognitive_model']} and its application to music composition.",
            f"The system effectively translates {t['linguistic_structure']} into musical elements, particularly {t['musical_element']}.",
            f"The proposed application in {t['application']} is well-reasoned and innovative.",
            f"The system incorporates the additional constraint: {t['constraint']}.",
            "The response shows a clear integration of cognitive linguistics, music theory, and artificial intelligence.",
            "The ethical considerations and future developments are thoughtfully addressed.",
            "The overall response is creative, original, scientifically plausible, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
