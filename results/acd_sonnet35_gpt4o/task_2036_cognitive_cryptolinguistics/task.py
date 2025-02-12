import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'language': 'Spanish',
                'linguistic_feature': 'Phonotactic constraints',
                'message': 'El sol brilla en el cielo azul',
                'feature_example': 'Spanish words rarely end in consonants other than n, d, l, r, s, z'
            },
            {
                'language': 'Mandarin Chinese',
                'linguistic_feature': 'Tonal patterns',
                'message': '春天来了 花儿开了',
                'feature_example': 'Mandarin has four tones: high level, rising, falling-rising, and falling'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive model for decrypting messages encoded using a complex substitution cipher based on linguistic patterns. Your task focuses on {t['language']} and the linguistic feature of {t['linguistic_feature']}. The encoded message is: '{TaskFamily.encode_message(t['message'], t['linguistic_feature'])}'Example of the linguistic feature: {t['feature_example']}Provide your response in the following format:1. Cipher Design (200-250 words):   a) Create a substitution cipher that incorporates {t['linguistic_feature']} of {t['language']}.   b) Explain how your cipher leverages these linguistic patterns to enhance encryption.   c) Provide an example of how a short phrase would be encoded using your cipher.2. Cognitive Decryption Model (250-300 words):   a) Design a cognitive model that simulates how a human might approach decrypting this cipher.   b) Explain how your model incorporates knowledge of {t['linguistic_feature']} in {t['language']}.   c) Describe the step-by-step process your model would follow to decrypt the message.3. Computational Implementation (200-250 words):   a) Outline an algorithm that implements your cognitive decryption model.   b) Explain how this algorithm mimics human cognitive processes in code-breaking.   c) Discuss any optimizations or heuristics your algorithm employs.4. Model Analysis (150-200 words):   a) Analyze the strengths and limitations of your cognitive decryption model.   b) Compare your model's approach to traditional computational cryptanalysis methods.   c) Discuss how your model might inform our understanding of human language processing and problem-solving.5. Ethical Implications (100-150 words):   a) Discuss the potential dual-use nature of cognitive models for decryption.   b) Propose guidelines for the responsible development and use of such models.6. Future Research Directions (100-150 words):   a) Suggest how your model could be extended to other languages or linguistic features.   b) Propose an experiment to validate your cognitive model against human performance.7. Decrypted Message:   Provide the decrypted message here.Ensure your response demonstrates a deep understanding of cryptography, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def encode_message(message: str, feature: str) -> str:
        if feature == 'Phonotactic constraints':
            # Encode Spanish message considering phonotactic constraints
            consonants = 'bcdfghjklmnpqrstvwxyz'
            vowels = 'aeiou'
            encoded = ''
            for char in message.lower():
                if char in consonants:
                    encoded += random.choice(vowels + 'nlrsz')
                elif char in vowels:
                    encoded += random.choice(consonants)
                else:
                    encoded += char
            return encoded
        elif feature == 'Tonal patterns':
            # Encode Chinese message considering tonal patterns
            tones = ['1', '2', '3', '4']
            encoded = ''
            for char in message:
                if char.isalnum():
                    encoded += char + random.choice(tones)
                else:
                    encoded += char
            return encoded
        else:
            return message  # Fallback to no encoding if feature is unknown

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['linguistic_feature']} in {t['language']}.",
            "The proposed cognitive model is innovative, scientifically plausible, and incorporates the specified linguistic feature.",
            "The computational implementation effectively mimics human cognitive processes in decryption.",
            "The analysis shows critical thinking about the model's strengths, limitations, and implications.",
            f"The decrypted message '{t['message']}' is correctly included in the response.",
            "The response follows the specified format and addresses all required sections comprehensively."
        ]
        result = eval_with_llm_judge(instructions, submission, criteria)
        if not result:
            print("The agent may have failed due to incomplete understanding of the linguistic features, inadequate cognitive modeling, or inability to decrypt the message correctly.")
        return 1.0 if result else 0.0
