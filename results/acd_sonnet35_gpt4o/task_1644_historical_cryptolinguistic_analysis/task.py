import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_ciphers = [
            {
                'name': 'Caesar Cipher',
                'period': 'Ancient Rome',
                'encrypted_text': 'YHQL YLGL YLFL',
                'key': 3,
                'historical_context': 'Julius Caesar\'s famous declaration after a swift victory.'
            },
            {
                'name': 'Vigenère Cipher',
                'period': 'Renaissance',
                'encrypted_text': 'LXFOPVEFRNHR',
                'key': 'LEMON',
                'historical_context': 'A message about a plot against Queen Elizabeth I.'
            },
            {
                'name': 'Playfair Cipher',
                'period': 'American Civil War',
                'encrypted_text': 'BMODZBXDNABEKUDMUIXMMOUVIF',
                'key': 'CONFEDERACY',
                'historical_context': 'A coded message about troop movements during the Battle of Gettysburg.'
            },
            {
                'name': 'ADFGVX Cipher',
                'period': 'World War I',
                'encrypted_text': 'FXFDAGDFFAAXFGFGAVDDGXDAVFX',
                'key': ('CRYPTOGRAPHY', 'ENIGMA'),
                'historical_context': 'A German military communication about a planned offensive on the Western Front.'
            },
            {
                'name': 'Enigma Machine',
                'period': 'World War II',
                'encrypted_text': 'DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ',
                'key': ('GRUNDSTELLUNG: ABL', 'UMKEHRWALZE: B', 'WALZENLAGE: II IV V'),
                'historical_context': 'A crucial message intercepted by Allied forces during the Battle of the Atlantic.'
            },
            {
                'name': 'Navajo Code',
                'period': 'World War II',
                'encrypted_text': 'DIBEH SHUSH MOASI TKIN NESH-CHEE AH-NAH A-KEH-DI-GLINI KLIZZIE-YAZZIE',
                'key': 'Navajo Code Talker Dictionary',
                'historical_context': 'A message transmitted by Navajo Code Talkers during the Pacific Campaign.'
            }
        ]
        
        tasks = random.sample(historical_ciphers, 2)
        return {str(i+1): {'cipher': cipher} for i, cipher in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 30 minutes to complete this task. Analyze and decode the following historical cipher, then use the decrypted information to solve a linguistic and historical puzzle:

Cipher Name: {t['cipher']['name']}
Historical Period: {t['cipher']['period']}
Encrypted Text: {t['cipher']['encrypted_text']}
Historical Context: {t['cipher']['historical_context']}

Your task consists of the following steps:

1. Decryption (200-250 words):
   a) Explain the decryption process for this specific cipher.
   b) Show your work in decrypting the given text.
   c) Provide the decrypted message.

2. Linguistic Analysis (200-250 words):
   a) Analyze the language used in the decrypted message.
   b) Identify any unusual words, phrases, or grammatical structures.
   c) Explain how the language reflects the historical period.

3. Historical Context (200-250 words):
   a) Relate the decrypted message to the provided historical context.
   b) Explain the significance of this message in its historical setting.
   c) Propose a hypothesis about the sender and intended recipient of the message.

4. Cryptographic Implications (150-200 words):
   a) Discuss the strengths and weaknesses of this cipher.
   b) Explain how this cipher compares to modern encryption methods.
   c) Speculate on how this cipher might have been broken by contemporary adversaries.

5. Interdisciplinary Connections (150-200 words):
   a) Explore how this example connects cryptography, linguistics, and history.
   b) Discuss how studying historical ciphers can inform modern cybersecurity practices.
   c) Propose a novel research question that arises from this interdisciplinary analysis.

6. Creative Extension (100-150 words):
   Create a short (2-3 sentence) coded message using the same cipher, related to a significant event from the same historical period. Provide both the encoded and decoded versions.

7. Error Analysis (100-150 words):
   a) Identify potential sources of error in your decryption or analysis.
   b) Explain how these errors could impact your conclusions.
   c) Propose methods to mitigate these potential errors in future analyses.

Ensure your response demonstrates a deep understanding of cryptography, linguistics, and historical analysis. Use appropriate technical terminology and provide clear explanations. Be creative in your approach while maintaining historical accuracy and plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the specific cipher and its decryption process.",
            "The linguistic analysis is insightful and relates well to the historical period.",
            "The historical context is accurately interpreted and expanded upon.",
            "The cryptographic implications are well-reasoned and show an understanding of both historical and modern encryption.",
            "The interdisciplinary connections are thoughtfully explored and lead to a novel research question.",
            "The creative extension is appropriate to the historical period and correctly uses the cipher.",
            "The error analysis demonstrates critical thinking and awareness of potential pitfalls in the analysis.",
            "The overall response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
