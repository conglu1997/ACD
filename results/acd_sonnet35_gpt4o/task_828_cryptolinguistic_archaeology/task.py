import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scripts = [
            {
                "name": "Linear A",
                "origin": "Minoan civilization",
                "period": "1800-1450 BCE",
                "decryption_status": "undeciphered"
            },
            {
                "name": "Rongorongo",
                "origin": "Easter Island",
                "period": "pre-1860s",
                "decryption_status": "undeciphered"
            },
            {
                "name": "Voynich Manuscript",
                "origin": "Unknown, possibly Central Europe",
                "period": "early 15th century",
                "decryption_status": "undeciphered"
            },
            {
                "name": "Indus Script",
                "origin": "Indus Valley Civilization",
                "period": "3500-1900 BCE",
                "decryption_status": "undeciphered"
            }
        ]
        
        cryptographic_techniques = [
            "frequency analysis",
            "polyalphabetic substitution",
            "transposition ciphers",
            "steganography"
        ]
        
        cultural_contexts = [
            "religious practices",
            "trade and commerce",
            "astronomical observations",
            "political systems"
        ]
        
        return {
            "1": {
                "script": random.choice(scripts),
                "technique": random.choice(cryptographic_techniques),
                "context": random.choice(cultural_contexts)
            },
            "2": {
                "script": random.choice(scripts),
                "technique": random.choice(cryptographic_techniques),
                "context": random.choice(cultural_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        word_counts = {
            "cryptographic_analysis": f"{random.randint(240, 260)}-{random.randint(290, 310)}",
            "linguistic_features": f"{random.randint(190, 210)}-{random.randint(240, 260)}",
            "cultural_context": f"{random.randint(190, 210)}-{random.randint(240, 260)}",
            "decryption_methodology": f"{random.randint(240, 260)}-{random.randint(290, 310)}",
            "interdisciplinary": f"{random.randint(140, 160)}-{random.randint(190, 210)}",
            "implications": f"{random.randint(140, 160)}-{random.randint(190, 210)}"
        }
        
        return f"""You are a cryptolinguistic archaeologist tasked with decrypting and analyzing an ancient or mysterious script. Your goal is to apply cryptographic techniques, linguistic analysis, and historical or cultural context to gain insights into the script and its creators.

Script Information:
- Name: {t['script']['name']}
- Origin: {t['script']['origin']}
- Period: {t['script']['period']}
- Decryption Status: {t['script']['decryption_status']}

Your task has the following components:

1. Cryptographic Analysis ({word_counts['cryptographic_analysis']} words):
   a) Describe how you would apply the {t['technique']} technique to analyze this script.
   b) Explain potential challenges in using this technique for this particular script.
   c) Propose a novel approach that combines this technique with another method to enhance decryption efforts.

2. Linguistic Features ({word_counts['linguistic_features']} words):
   a) Identify and describe potential linguistic features of the script (e.g., syntax, morphology, phonology).
   b) Compare these features to known language families or writing systems.
   c) Propose a hypothesis about the language's structure based on your analysis.

3. Cultural Context Analysis ({word_counts['cultural_context']} words):
   a) Analyze how the {t['context']} of the script's origin might influence its content and structure.
   b) Propose three specific types of information you would expect to find in the script based on this context.
   c) Explain how deciphering this script could enhance our understanding of the culture that produced it.

4. Decryption Methodology ({word_counts['decryption_methodology']} words):
   a) Outline a step-by-step methodology for attempting to decrypt this script.
   b) Explain how you would validate partial decryptions or hypotheses about the script's meaning.
   c) Describe potential pitfalls in the decryption process and how you would address them.

5. Interdisciplinary Connections ({word_counts['interdisciplinary']} words):
   a) Discuss how insights from other fields (e.g., archaeology, computer science, cognitive psychology) could aid in decrypting and understanding this script.
   b) Propose an experiment or study that combines multiple disciplines to further the decryption effort.

6. Implications and Ethics ({word_counts['implications']} words):
   a) Discuss the potential implications of successfully decrypting this script for our understanding of history or language evolution.
   b) Address any ethical considerations in the decryption and analysis of ancient or mysterious scripts.

Ensure your response demonstrates a deep understanding of cryptography, linguistics, and historical analysis. Be creative in your approach while maintaining scientific rigor and plausibility. Use clear headings for each section of your response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the {t['technique']} cryptographic technique and its application to the {t['script']['name']} script.",
            "The linguistic analysis is thorough and makes plausible connections to known language families or writing systems.",
            f"The cultural context analysis provides insightful connections between the {t['context']} and the potential content and structure of the script.",
            "The proposed decryption methodology is logical, comprehensive, and addresses potential challenges.",
            "The response shows creativity and interdisciplinary thinking in approaching the decryption task.",
            "Ethical considerations and implications of the decryption are thoughtfully addressed.",
            "The submission follows the specified format and adheres to the given word count ranges for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
