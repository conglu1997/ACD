import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Amazonian Tribal",
            "Tibetan Buddhist",
            "Silicon Valley Tech",
            "Inuit",
            "Maasai"
        ]
        concepts = [
            "Time",
            "Nature",
            "Community",
            "Knowledge",
            "Progress"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Coherence",
            "Quantum Annealing"
        ]
        
        tasks = {}
        for i in range(1, 3):
            culture1, culture2 = random.sample(cultures, 2)
            concept = random.choice(concepts)
            principles = random.sample(quantum_principles, 2)
            tasks[str(i)] = {
                "culture1": culture1,
                "culture2": culture2,
                "concept": concept,
                "principles": principles
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum neurolinguistic cultural interface system that facilitates understanding of the concept of '{t['concept']}' between {t['culture1']} and {t['culture2']} cultures. Your system should leverage the quantum principles of {t['principles'][0]} and {t['principles'][1]}. Provide your response in the following format:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your quantum neurolinguistic cultural interface.\n   b) Explain how it integrates principles from quantum computing, neurolinguistics, and cultural anthropology.\n   c) Detail how the system leverages {t['principles'][0]} and {t['principles'][1]} for cross-cultural communication.\n   d) Provide a simple diagram or pseudocode to illustrate your system design.\n\n2. Operational Mechanism (200-250 words):\n   a) Explain how your system interfaces with the human brain to facilitate cross-cultural understanding.\n   b) Describe the process of translating cultural concepts between the two cultures.\n   c) Discuss how quantum effects enhance this translation process.\n\n3. Cultural Analysis (200-250 words):\n   a) Compare and contrast how the concept of '{t['concept']}' is understood in {t['culture1']} and {t['culture2']} cultures.\n   b) Explain how your system bridges these differences in understanding.\n   c) Provide an example of a potential misunderstanding that your system could prevent.\n\n4. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical implications of using this technology for cross-cultural communication.\n   b) Address concerns about privacy, cultural preservation, and potential misuse.\n   c) Propose guidelines for the responsible development and use of quantum neurolinguistic interfaces.\n\n5. Future Implications (150-200 words):\n   a) Speculate on how this technology might impact global communication and cultural exchange.\n   b) Discuss potential applications in fields such as diplomacy, education, or conflict resolution.\n   c) Suggest areas for future research to enhance the capabilities of your system.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, neurolinguistics, and cultural anthropology. Be creative and speculative while maintaining scientific plausibility. Your total response should be between 950-1200 words. Each section must meet the minimum word count specified. Additionally, cite at least one relevant scientific paper or theory in your response to support your design or analysis."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing principles, particularly {t['principles'][0]} and {t['principles'][1]}, as well as neurolinguistics and cultural anthropology",
            "The system design is creative, innovative, and scientifically plausible, with a clear diagram or pseudocode provided",
            f"The cultural analysis shows insightful comparison between {t['culture1']} and {t['culture2']} cultures regarding the concept of {t['concept']}, with specific examples",
            "The operational mechanism clearly explains how the system interfaces with the human brain and translates cultural concepts, including details on neural pathways or brain regions involved",
            "Ethical considerations are thoroughly addressed, including privacy, cultural preservation, and potential misuse, with specific mitigation strategies proposed",
            "Future implications and potential applications are thoughtfully discussed, with at least one novel idea presented",
            "The response adheres to the specified format and word count guidelines for each section",
            "At least one relevant scientific paper or theory is cited and appropriately integrated into the response"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
