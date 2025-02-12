import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "wave function collapse",
            "quantum tunneling",
            "quantum decoherence",
            "quantum interference"
        ]
        story_themes = [
            "time travel",
            "parallel universes",
            "consciousness transfer",
            "alien communication",
            "quantum immortality",
            "simulated reality"
        ]
        tasks = {}
        for i in range(2):
            concepts = random.sample(quantum_concepts, 2)
            tasks[str(i+1)] = {
                "quantum_concept1": concepts[0],
                "quantum_concept2": concepts[1],
                "story_theme": random.choice(story_themes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a narrative encryption system based on the quantum concepts of {t['quantum_concept1']} and {t['quantum_concept2']}, then use it to encode and analyze a short story with the theme of {t['story_theme']}. Your response should include the following sections, each with its own heading:

1. Encryption System Design (300-350 words):
   a) Explain how you incorporate both {t['quantum_concept1']} and {t['quantum_concept2']} into your narrative encryption system.
   b) Describe the rules and mechanics of your encryption system.
   c) Discuss how your system maintains the balance between information security and narrative coherence.
   d) Propose a potential real-world application for your quantum narrative encryption system.

2. Short Story Creation (200-250 words):
   Create a short story (about 150 words) on the theme of {t['story_theme']}. The story should have a clear beginning, middle, and end.

3. Story Encryption (250-300 words):
   a) Encrypt your short story using your quantum-inspired system.
   b) Provide the encrypted version of the story.
   c) Explain the encryption process, highlighting how {t['quantum_concept1']} and {t['quantum_concept2']} influence the narrative structure.

4. Decryption and Analysis (250-300 words):
   a) Describe the decryption process for your system.
   b) Analyze how the encryption affects the story's interpretation and reader experience.
   c) Discuss any emergent narrative properties resulting from your encryption system.

5. Quantum-Classical Comparison (200-250 words):
   a) Compare your quantum-inspired encryption to classical encryption methods.
   b) Discuss potential advantages or limitations of your approach.
   c) Propose a hypothetical experiment to test the effectiveness of your system.
   d) Speculate on how your system might evolve with advancements in quantum computing.

Ensure your response demonstrates a deep understanding of both quantum physics and narrative theory. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and adhere to the word count guidelines provided.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate headings",
            f"The encryption system is based on both quantum concepts ({t['quantum_concept1']} and {t['quantum_concept2']}) and demonstrates accurate understanding of these concepts",
            f"The short story addresses the theme of {t['story_theme']} and is within the specified word count",
            "The encryption process is explained clearly and incorporates both quantum concepts",
            "An encrypted version of the story is provided",
            "The analysis demonstrates understanding of both quantum physics and narrative theory",
            "The response is creative and innovative while maintaining scientific plausibility",
            "The response adheres to the specified word count guidelines for each section",
            "A potential real-world application for the quantum narrative encryption system is proposed",
            "The response speculates on the system's evolution with advancements in quantum computing"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
