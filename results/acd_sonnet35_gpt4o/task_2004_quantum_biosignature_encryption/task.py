import random
from typing import List, Optional

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biosignatures = ['amino acid chirality', 'atmospheric oxygen', 'chlorophyll red edge', 'methane-carbon dioxide disequilibrium']
        quantum_properties = ['superposition', 'entanglement', 'quantum tunneling', 'wave function collapse']
        astrobiological_contexts = ['exoplanet atmosphere', 'subsurface ocean', 'interstellar medium', 'planetary magnetosphere']
        
        return {
            "1": {
                "biosignature": random.choice(biosignatures),
                "quantum_property": random.choice(quantum_properties),
                "context": random.choice(astrobiological_contexts)
            },
            "2": {
                "biosignature": random.choice([b for b in biosignatures if b != biosignatures[0]]),
                "quantum_property": random.choice([q for q in quantum_properties if q != quantum_properties[0]]),
                "context": random.choice([c for c in astrobiological_contexts if c != astrobiological_contexts[0]])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Design a theoretical quantum encryption system based on the biological signature of {t['biosignature']}, "
            f"utilizing the quantum property of {t['quantum_property']}. Then, use this system to encode and decode "
            f"a message within the astrobiological context of a {t['context']}. Your response should include:\n\n"
            f"1. Encryption System Design (250-300 words):\n"
            f"   a) Describe the key components of your quantum encryption system.\n"
            f"   b) Explain how it incorporates the biological signature {t['biosignature']}.\n"
            f"   c) Detail how the quantum property of {t['quantum_property']} is utilized in the encryption process.\n"
            f"   d) Discuss any novel algorithms or approaches used in your design.\n\n"
            f"2. Message Encoding and Decoding (200-250 words):\n"
            f"   a) Provide a sample message (50-75 words) related to astrobiology or SETI.\n"
            f"   b) Explain the step-by-step process of encoding this message using your system.\n"
            f"   c) Describe how the message would be decoded by a recipient.\n"
            f"   d) Discuss any potential sources of error or ambiguity in the encoding/decoding process.\n\n"
            f"3. Astrobiological Context (200-250 words):\n"
            f"   a) Explain how your encryption system could be implemented or detected within a {t['context']}.\n"
            f"   b) Discuss the challenges and advantages of using this system in this specific context.\n"
            f"   c) Analyze how this system might influence our search for extraterrestrial intelligence.\n\n"
            f"4. Implications for SETI (150-200 words):\n"
            f"   a) Discuss how your quantum biosignature encryption system might impact SETI strategies.\n"
            f"   b) Explore the potential implications if such a system were detected from an extraterrestrial source.\n"
            f"   c) Propose a method for distinguishing this type of encrypted signal from natural phenomena.\n\n"
            f"5. Ethical and Philosophical Considerations (150-200 words):\n"
            f"   a) Analyze the ethical implications of using biological signatures for encryption.\n"
            f"   b) Discuss the philosophical implications of finding such an encryption system in nature.\n"
            f"   c) Explore how this concept challenges or extends our current understanding of life and intelligence.\n\n"
            f"Ensure your response demonstrates a deep understanding of quantum mechanics, information theory, and astrobiology. "
            f"Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology "
            f"and provide clear explanations for complex concepts.\n\n"
            f"Format your response with clear headings for each section, and begin each section with a brief introductory sentence. "
            f"For example, under 'Encryption System Design', you might start with: 'The proposed quantum encryption system "
            f"integrates {t['biosignature']} and {t['quantum_property']} in the following manner...'\n\n"
            f"Your total response should be between 950-1200 words."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, information theory, and astrobiology.",
            "The encryption system design is creative, scientifically plausible, and effectively incorporates the given biological signature and quantum property.",
            "The message encoding and decoding process is clearly explained and logically consistent with the proposed system.",
            "The astrobiological context is thoroughly considered, with insightful analysis of implementation challenges and advantages.",
            "The implications for SETI are thoughtfully explored, including potential detection methods and distinguishing features.",
            "Ethical and philosophical considerations are addressed with depth and originality.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts.",
            "The answer is well-structured, following the requested format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
