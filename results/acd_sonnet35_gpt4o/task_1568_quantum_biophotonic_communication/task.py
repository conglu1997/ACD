import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "habitat": "Abyssal plain",
                "pressure": "High (400-600 atmospheres)",
                "light": "Bioluminescence only",
                "temperature": "Near freezing (2-4°C)",
                "organism": "Giant isopod (Bathynomus giganteus)"
            },
            {
                "habitat": "Hydrothermal vent",
                "pressure": "Extreme (250-400 atmospheres)",
                "light": "Thermal radiation",
                "temperature": "Highly variable (2-400°C)",
                "organism": "Pompeii worm (Alvinella pompejana)"
            }
        ]
        return {
            "1": random.choice(environments),
            "2": random.choice(environments)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based biophotonic communication system for deep-sea organisms living in a {t['habitat']} environment with the following conditions:
- Pressure: {t['pressure']}
- Light: {t['light']}
- Temperature: {t['temperature']}
- Target organism: {t['organism']}

Then, analyze its potential applications in human technology. Your response should follow this structure:

Brief explanations:
- Quantum entanglement: A phenomenon where particles become interconnected and the quantum state of each particle cannot be described independently of the others.
- Quantum superposition: A principle where a quantum system can exist in multiple states simultaneously until measured or observed.

1. System Design (300-350 words):
   a) Describe the key components of your quantum biophotonic communication system.
   b) Explain how it utilizes at least two quantum principles (e.g., entanglement, superposition) in conjunction with biophotonic processes.
   c) Detail how the system adapts to the specific deep-sea environment conditions.
   d) Discuss at least two novel biomimetic features inspired by the target organism or other deep-sea creatures.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how your system integrates quantum processes with biological systems.
   b) Describe the mechanisms for generating, transmitting, and receiving quantum-biophotonic signals.
   c) Discuss at least three challenges in maintaining quantum coherence in a biological context and how you address them.

3. Information Encoding and Processing (250-300 words):
   a) Propose a specific method for encoding information in your quantum-biophotonic signals.
   b) Explain how this encoding scheme leverages both quantum and biological properties.
   c) Describe how the system processes and interprets received signals.
   d) Quantitatively compare the potential information capacity and transmission speed to at least one existing biological and one technological system.

4. Environmental Adaptation and Efficiency (200-250 words):
   a) Analyze how your system optimizes energy use in the given deep-sea environment.
   b) Discuss at least two mechanisms for error correction or signal amplification in challenging conditions.
   c) Explain how the system might evolve or be artificially improved over time.

5. Human Technological Applications (250-300 words):
   a) Propose two specific potential applications of your quantum-biophotonic communication system in human technology.
   b) Explain how these applications could advance fields such as underwater communication, quantum computing, or biomedical imaging.
   c) Discuss at least two ethical considerations and two potential risks associated with these applications.
   d) Suggest a 5-year research roadmap for developing and implementing these technologies.

Ensure your response demonstrates a deep understanding of quantum mechanics, biophotonics, marine biology, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary. Your proposed system should be grounded in current scientific understanding while exploring speculative but feasible advancements.

Format your response with clear headings for each section and use subheadings (a, b, c, d) as outlined above. Your total response should be between 1250-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response designs a quantum-based biophotonic communication system specifically for the {t['habitat']} environment, addressing the given pressure, light, temperature, and target organism",
            "The system design incorporates at least two quantum principles and biophotonic processes, with clear explanations of how they are utilized",
            "The response explains in detail how quantum processes are integrated with biological systems and addresses at least three challenges in maintaining quantum coherence",
            "The information encoding and processing method leverages both quantum and biological properties, with a quantitative comparison to existing systems",
            "The system's adaptation to the deep-sea environment and energy efficiency are thoroughly discussed, including at least two error correction or signal amplification mechanisms",
            "Two specific potential applications in human technology are proposed and analyzed in depth, including ethical considerations, potential risks, and a detailed 5-year research roadmap",
            "The response demonstrates a deep understanding of quantum mechanics, biophotonics, marine biology, and information theory, using appropriate technical terminology and maintaining scientific plausibility",
            "The response follows the required format with clear headings and subheadings, and falls within the specified word count of 1250-1500 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
