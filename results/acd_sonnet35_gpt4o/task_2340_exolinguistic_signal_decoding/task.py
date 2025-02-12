import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_environments = [
            {
                "planet_type": "Super-Earth",
                "atmosphere": "Methane-rich",
                "gravity": "1.5g",
                "dominant_wavelength": "Infrared",
                "signal": "🌀🔺🔷🔺🌀🔶🔷🔶 | 🌀🔺🔷🔺🌀🔶🔷🔶 | 🌀🔺🔷🔺🌀🔶🔷🔶"
            },
            {
                "planet_type": "Ocean world",
                "atmosphere": "Hydrogen-helium",
                "gravity": "0.8g",
                "dominant_wavelength": "Ultraviolet",
                "signal": "⭐🌊⭐⭐🌊🌊⭐🌊 | ⭐🌊⭐⭐🌊🌊⭐🌊 | ⭐⭐🌊🌊⭐🌊⭐🌊"
            }
        ]
        return {
            "1": alien_environments[0],
            "2": alien_environments[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical alien communication system for a civilization evolved in the following environment, then decode a simulated signal using principles from linguistics, information theory, and astrobiology:

Planet type: {t['planet_type']}
Atmosphere: {t['atmosphere']}
Gravity: {t['gravity']}
Dominant wavelength: {t['dominant_wavelength']}

Key concepts:
- Information theory: The study of quantification, storage, and communication of information.
- Astrobiology: The study of the origin, evolution, and distribution of life in the universe.

Your response should follow this structure:

1. Communication System Design (300-350 words):
   - Describe the physical basis of the communication system
   - Explain how the alien environment influences the design
   - Detail the basic units of information in this system
   - Propose a method for encoding complex messages

2. Linguistic and Information Theory Analysis (250-300 words):
   - Analyze the potential complexity of the alien language using information theory principles
   - Discuss concepts like entropy and redundancy in this system
   - Compare and contrast this system with human language
   - Speculate on the aliens' cognitive processes reflected in their communication

3. Signal Decoding Process (250-300 words):
   - Describe a step-by-step process for decoding a signal
   - Explain methods for identifying patterns and structure
   - Discuss potential challenges and how to address them
   - Propose a method for verifying decoding accuracy

4. Simulated Signal Decoding (200-250 words):
   Decode the following simulated alien signal using your proposed system and process:
   {t['signal']}
   - Show your work in decoding the signal
   - Provide your interpretation of the decoded message
   - Explain any assumptions or inferences made during decoding

5. Astrobiological Implications (200-250 words):
   - Discuss how this system reflects the aliens' biological and evolutionary history
   - Speculate on implications for alien social structures and cognitive capabilities
   - Consider how studying such systems could advance our understanding of extraterrestrial life

6. Comparative Analysis (200-250 words):
   - Compare your alien system with human language
   - Contrast your system with another hypothetical communication system (e.g., hive-mind species)
   - Discuss strengths, limitations, and unique features of each system

7. Ethical and Practical Considerations (150-200 words):
   - Discuss ethical implications of communicating with an alien civilization
   - Consider practical challenges in establishing two-way communication
   - Propose guidelines for responsible communication attempts

Ensure your response demonstrates a deep understanding of linguistics, information theory, and astrobiology. Be creative while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The communication system design considers the given alien environment and proposes a plausible method for encoding messages.",
            "The linguistic and information theory analysis applies relevant concepts to the alien communication system.",
            "The signal decoding process is logical and includes methods for pattern identification and accuracy verification.",
            "The simulated signal decoding shows a clear interpretation of the provided signal with explained reasoning.",
            "The astrobiological implications consider the biological and evolutionary aspects of the hypothetical alien species.",
            "The comparative analysis effectively contrasts the proposed alien system with human language and another hypothetical system.",
            "Ethical and practical considerations are discussed, including guidelines for responsible communication attempts.",
            "The response demonstrates interdisciplinary knowledge synthesis and creative problem-solving.",
            "The proposed ideas are innovative while maintaining scientific plausibility.",
            "The response follows the specified format and addresses all required points."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
