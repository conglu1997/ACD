import random
import string
import time

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                "name": "Quantum Chlorophyllians",
                "biology": "Plant-like organisms with quantum-entangled distributed neural networks",
                "communication": "Superposed chemical-quantum signaling through root systems, airborne spores, and entangled particles"
            },
            {
                "name": "Chrono-Cephalopodians",
                "biology": "Highly intelligent aquatic creatures with time-sensitive chromatophore-based skin and temporal lobe manipulation abilities",
                "communication": "Complex patterns of color changes, bioluminescence, and localized time-field distortions"
            },
            {
                "name": "Hyperdimensional Crystallines",
                "biology": "Silicon-based lifeforms with piezoelectric properties existing across multiple spatial dimensions",
                "communication": "Vibrational frequencies, resonance patterns, and hyperdimensional geometric configurations"
            },
            {
                "name": "Quantum Nebulites",
                "biology": "Gaseous entities existing in interstellar clouds with quantum superposition properties",
                "communication": "Modulations in electromagnetic emissions, quantum state changes, and probability field manipulations"
            }
        ]
        
        return {
            "1": random.choice(alien_species),
            "2": random.choice(alien_species)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework and system for translating between human language and the complex, multi-modal biosemiotic communication system of the {t['name']} alien species. Then, apply your system to decode a simulated alien message with potential ambiguities. You have a maximum of 30 minutes to complete this task. Your response should include:

1. Advanced Biosemiotic Analysis (300-350 words):
   a) Analyze the {t['name']}'s biology and multi-modal communication system.
   b) Identify key principles of their biosemiotic system, including potential quantum or hyperdimensional aspects.
   c) Compare and contrast with human language and communication, highlighting unique challenges.

2. Multi-Modal Translation Framework (350-400 words):
   a) Propose a theoretical framework for translating between human language and the alien biosemiotic system.
   b) Describe the key components and processes of your translation system, addressing each mode of communication.
   c) Explain how your system addresses the unique challenges of this alien communication method, including potential quantum or hyperdimensional aspects.
   d) Include a detailed diagram or flowchart illustrating your translation process.

3. Advanced Information Theory Application (250-300 words):
   a) Apply advanced concepts from information theory to analyze the alien communication system.
   b) Discuss entropy, channel capacity, and signal-to-noise ratio in the context of this complex biosemiotic system.
   c) Explain how these concepts inform your translation approach, considering potential quantum or hyperdimensional aspects.

4. Ambiguous Message Decoding (300-350 words):
   a) Given the following simulated alien message: '{TaskFamily.generate_alien_message(t['name'])}'
   b) Apply your translation system to decode this message, considering potential ambiguities.
   c) Provide a step-by-step explanation of your decoding process, including how you handle ambiguities.
   d) Present your interpretation of the message's meaning, discussing any alternative interpretations.

5. Advanced Challenges and Limitations (200-250 words):
   a) Discuss the main challenges in translating this complex alien biosemiotic system.
   b) Identify potential sources of error or misinterpretation in your approach, including quantum or hyperdimensional aspects.
   c) Propose advanced methods to validate and improve the accuracy of your translation system.

6. Ethical and Philosophical Implications (200-250 words):
   a) Explore the ethical considerations of interspecies communication with advanced alien life forms.
   b) Discuss how successful translation might impact our understanding of language, cognition, consciousness, and reality itself.
   c) Consider the potential consequences of miscommunication or mistranslation in this context, including possible existential risks.

Ensure your response demonstrates a deep understanding of advanced biosemiotics, linguistics, information theory, quantum mechanics, and xenobiology. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Your total response should be between 1600-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates an exceptional understanding of the {t['name']}'s unique biology and complex, multi-modal communication system, including quantum or hyperdimensional aspects.",
            "The proposed multi-modal translation framework is highly creative, well-structured, and scientifically plausible, addressing the specific challenges of the advanced alien species.",
            "The application of advanced information theory concepts to the alien communication system is sophisticated, insightful, and tailored to the species' unique characteristics.",
            f"The decoding process for the simulated {t['name']} message is logical, well-explained, and consistent with the proposed framework, effectively addressing potential ambiguities.",
            "The discussion of advanced challenges, limitations, and ethical implications is exceptionally thoughtful, comprehensive, and considers the unique aspects of the alien species and potential existential risks.",
            "The response demonstrates a high level of creativity and speculative thinking while maintaining scientific plausibility and coherence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

    @staticmethod
    def generate_alien_message(species_name: str) -> str:
        if species_name == "Quantum Chlorophyllians":
            quantum_states = ['|0⟩', '|1⟩', '|+⟩', '|-⟩', '|i⟩', '|-i⟩']
            return ''.join(random.choices(string.ascii_lowercase, k=20)) + '-' + ''.join(random.choices(string.digits, k=15)) + '-' + ''.join(random.choices(['C', 'H', 'O', 'N'], k=15)) + '-' + ''.join(random.choices(quantum_states, k=15))
        elif species_name == "Chrono-Cephalopodians":
            colors = ['R', 'G', 'B', 'Y', 'P', 'O']
            time_distortions = ['⏪', '⏩', '⏸️', '⏭️', '⏮️', '⏯️']
            return ''.join(random.choices(colors, k=25)) + '-' + ''.join(random.choices(string.ascii_uppercase, k=15)) + '-' + ''.join(random.choices(['.', '-', '~', '*'], k=15)) + '-' + ''.join(random.choices(time_distortions, k=10))
        elif species_name == "Hyperdimensional Crystallines":
            frequencies = [str(random.randint(1, 1000)) for _ in range(15)]
            dimensions = ['3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D']
            return '-'.join(frequencies) + '-' + ''.join(random.choices(string.hexdigits, k=15)) + '-' + ''.join(random.choices(dimensions, k=10))
        elif species_name == "Quantum Nebulites":
            em_spectrum = ['RF', 'MW', 'IR', 'V', 'UV', 'X', 'G']
            quantum_states = ['|S⟩', '|T⟩', '|Ψ+⟩', '|Ψ-⟩', '|Φ+⟩', '|Φ-⟩']
            return ''.join(random.choices(em_spectrum, k=20)) + '-' + ''.join(random.choices(string.ascii_letters + string.digits, k=20)) + '-' + ''.join(random.choices(quantum_states, k=15))
        else:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=50))
