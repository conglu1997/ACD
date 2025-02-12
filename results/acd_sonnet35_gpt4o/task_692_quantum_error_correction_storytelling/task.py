import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "Surface code",
                "description": "A type of quantum error correction code that arranges physical qubits in a 2D lattice to detect and correct errors"
            },
            {
                "concept": "Bit-flip error",
                "description": "An error in quantum computing where a qubit's state is flipped from |0⟩ to |1⟩ or vice versa"
            },
            {
                "concept": "Decoherence",
                "description": "The loss of quantum information due to interaction between a quantum system and its environment"
            },
            {
                "concept": "Quantum teleportation",
                "description": "A technique for transferring quantum information from one location to another using quantum entanglement and classical communication"
            }
        ]
        
        story_settings = [
            "A medieval fantasy kingdom",
            "A futuristic space colony",
            "An underwater civilization",
            "A microscopic world inside a computer chip"
        ]
        
        tasks = {}
        for i in range(1, 3):
            concept = random.choice(quantum_concepts)
            setting = random.choice(story_settings)
            tasks[str(i)] = {"concept": concept, "setting": setting}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create an allegorical story that explains the quantum error correction concept of '{t['concept']['concept']}' in the setting of {t['setting']}. Your task has the following parts:\n\n1. Allegorical Story (300-350 words):\n   Write a creative story set in {t['setting']} that serves as an allegory for {t['concept']['concept']}. Your story should:\n   a) Incorporate key elements and principles of the quantum concept\n   b) Use characters, events, or phenomena in the chosen setting to represent aspects of the quantum concept\n   c) Be engaging and accessible to a non-scientific audience\n\n2. Concept Explanation (150-200 words):\n   Provide a clear, scientific explanation of {t['concept']['concept']}, including its significance in quantum error correction.\n\n3. Allegory Analysis (200-250 words):\n   a) Explain how specific elements in your story represent aspects of {t['concept']['concept']}\n   b) Discuss the strengths and limitations of your allegory in conveying the quantum concept\n   c) Analyze how effective your story might be in helping a layperson understand the quantum concept\n\n4. Improvement Suggestion (100-150 words):\n   Propose one way to enhance your allegory to better represent {t['concept']['concept']}, explaining how this change would improve understanding of the quantum concept.\n\nEnsure your response demonstrates a deep understanding of quantum error correction principles while showcasing creative storytelling and analytical skills. Use appropriate scientific terminology in the explanation and analysis sections, but keep the story itself accessible to a general audience."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story effectively allegorizes the concept of {t['concept']['concept']} while maintaining scientific accuracy",
            "The allegorical story is creative, engaging, and accessible to a non-scientific audience",
            "The scientific explanation is accurate, clear, and demonstrates a deep understanding of the quantum concept",
            "The allegory analysis shows insightful connections between the story elements and the quantum concept",
            "The improvement suggestion is thoughtful and would enhance both the storytelling and the understanding of the quantum concept"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
