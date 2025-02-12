import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_periods = ['Ancient Egypt', 'Medieval Europe', 'Renaissance Italy']
        quantum_principles = ['superposition', 'entanglement', 'quantum tunneling']
        linguistic_features = ['syntax', 'semantics', 'pragmatics']
        
        tasks = [
            {
                'historical_period': random.choice(historical_periods),
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_feature': random.choice(linguistic_features),
                'text_length': random.randint(300, 400)
            },
            {
                'historical_period': random.choice(historical_periods),
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_feature': random.choice(linguistic_features),
                'text_length': random.randint(300, 400)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired linguistic analysis system to uncover hidden patterns and potential encrypted messages in historical texts from {t['historical_period']}. Your system should incorporate the quantum principle of {t['quantum_principle']} and focus on the linguistic feature of {t['linguistic_feature']}. Then, apply your system to analyze a given historical text and propose hypotheses about its significance. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired linguistic analysis system.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your analysis model.
   c) Detail how your system processes and analyzes the linguistic feature of {t['linguistic_feature']}.
   d) Discuss any novel algorithms or data structures used in your design.
   e) Include a high-level diagram of your system's architecture (describe it textually using ASCII characters, max 20 lines).

2. Quantum-Linguistic Interface (250-300 words):
   a) Explain how your system translates linguistic concepts into quantum states or operations.
   b) Describe how quantum computations are mapped back to linguistic phenomena.
   c) Discuss any challenges in reconciling quantum and linguistic paradigms.
   d) Provide a mathematical formulation or equation representing a key aspect of your quantum-linguistic interface.

3. Historical Text Analysis (250-300 words):
   a) Apply your system to analyze the following historical text (note: this is a generated text for the purpose of this task):
      '{TaskFamily.generate_historical_text(t['historical_period'], t['text_length'])}'
   b) Explain how your system identifies potential hidden patterns or encrypted messages.
   c) Describe any preprocessing or contextual analysis your system performs.
   d) Provide a step-by-step breakdown of your system's analysis process.

4. Hypothesis Generation and Evaluation (200-250 words):
   a) Present at least two hypotheses about the historical significance of the analyzed text based on your system's output.
   b) Explain how your system generates and evaluates these hypotheses.
   c) Discuss the role of the quantum principle and linguistic feature in shaping these hypotheses.
   d) Provide a confidence score (0-100%) for each hypothesis and justify these scores.

5. Cryptographic Analysis (200-250 words):
   a) If your system identified potential encrypted content, describe your approach to decrypting or interpreting it.
   b) Explain how historical context and linguistic features inform your cryptographic analysis.
   c) Discuss any quantum-inspired techniques used in the decryption process.
   d) Provide an example of a decrypted message or pattern, if applicable.

6. Historical Implications and Limitations (150-200 words):
   a) Discuss the potential historical implications of your findings.
   b) Address the limitations of your approach and potential sources of error or bias.
   c) Propose future research directions or improvements to your system.
   d) Discuss the ethical considerations of using quantum-inspired AI for historical analysis.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic analysis, historical context, and cryptography. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and historical plausibility.

Format your response with clear headings for each section, and include the requested diagrams, equations, and examples. Your total response should be between 1350-1650 words."""

    @staticmethod
    def generate_historical_text(period: str, length: int) -> str:
        base_texts = {
            'Ancient Egypt': "The sacred ibis flies over the Nile, its wings casting shadows on the great pyramids. Pharaoh Amenhotep gazes upon the horizon, his eyes fixed on the setting sun. The scribes hurriedly record the day's events on papyrus, their reed pens scratching in the silence of the evening. In the distance, the sound of stone against stone echoes as workers continue their labor on the new temple. A merchant whispers to his companion, 'The stars align, the time is near.' The companion nods, tracing a symbol in the sand.",
            'Medieval Europe': "In the candlelit chambers of the monastery, Brother Thomas carefully illuminates the manuscript before him. Outside, the town crier's voice rings out, announcing the arrival of a royal envoy. The clatter of hooves on cobblestones grows louder as knights in shining armor approach the castle gates. In the fields beyond, peasants toil under the watchful eye of their feudal lord. A hooded figure slips a parchment into a hollow tree, muttering, 'The rose blooms at midnight.' A bird takes flight, carrying a message tied to its leg.",
            'Renaissance Italy': "Leonardo da Vinci's hand moves swiftly across the parchment, sketching his latest invention. In the piazza, merchants haggle over the price of exotic spices from the East. The sound of a lute drifts from an open window, mingling with the chatter of scholars debating the latest philosophical treatise. In his workshop, Michelangelo chips away at a block of marble, slowly revealing the form of David. A cloaked woman passes a coded message to a young apprentice, whispering, 'The key lies within the fresco.' The apprentice nods, his eyes darting to a particular painting on the wall."
        }
        base_text = base_texts.get(period, "")
        
        # Add some pseudo-encrypted content
        encrypted_snippets = [
            "Xjm ywt htrjx ns ymj ifwp tk snlmy",
            "Ymj wtxj gqttrx fy rnishlmy",
            "Ymj pjd qnjx bnymns ymj kwjxht"
        ]
        
        while len(base_text) < length:
            if random.random() < 0.2:  # 20% chance to insert encrypted snippet
                base_text += " " + random.choice(encrypted_snippets)
            else:
                base_text += " " + ''.join(random.choices(string.ascii_lowercase, k=5))
        
        return base_text[:length]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing principles (especially {t['quantum_principle']}), linguistic analysis (focusing on {t['linguistic_feature']}), historical context of {t['historical_period']}, and cryptography.",
            "The proposed system effectively integrates quantum-inspired algorithms with linguistic analysis techniques, with a clear explanation of how the quantum principle is applied to the linguistic feature.",
            "The analysis of the given historical text is thorough and plausible, with creative yet scientifically grounded hypotheses. The confidence scores for hypotheses are provided and well-justified.",
            "The cryptographic analysis approach is well-explained, contextually appropriate, and includes an example of a decrypted message or pattern (if applicable).",
            "The response includes the requested diagrams, equations, and examples for each section, with the system architecture diagram properly described using ASCII characters.",
            "The discussion of historical implications, limitations, and ethical considerations is thoughtful and well-reasoned.",
            "The response is well-structured, clear, and adheres to the specified word count range (1350-1650 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
