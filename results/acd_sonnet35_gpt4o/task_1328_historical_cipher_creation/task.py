import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_periods = [
            {
                "period": "Ancient Rome",
                "year_range": "27 BC - 476 AD",
                "context": "The height of the Roman Empire, known for its military conquests and technological advancements."
            },
            {
                "period": "Renaissance Italy",
                "year_range": "14th - 17th century",
                "context": "A period of great cultural and artistic innovation, as well as political intrigue among city-states."
            },
            {
                "period": "Elizabethan England",
                "year_range": "1558 - 1603",
                "context": "A golden age of English literature and exploration, marked by political and religious tensions."
            },
            {
                "period": "American Civil War",
                "year_range": "1861 - 1865",
                "context": "A period of technological advancements in warfare and communication, with complex political and social dynamics."
            }
        ]
        messages = [
            "The eagle flies at midnight",
            "Beware the ides of March",
            "The red fox jumps over the lazy dog",
            "All that glitters is not gold"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "time_period": random.choice(time_periods),
                "message": random.choice(messages)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a historical cipher based on the time period of {t['time_period']['period']} ({t['time_period']['year_range']}), then use it to encode the message "{t['message']}" and analyze its security. Your response should include:

1. Cipher Design (200-250 words):
   a) Describe your cipher's encryption method, inspired by the historical context.
   b) Explain how your cipher reflects the technology and knowledge available during this period.
   c) Provide a step-by-step guide on how to use your cipher for encryption and decryption.

2. Historical Context (150-200 words):
   a) Explain how your cipher relates to the historical and cultural context of {t['time_period']['period']}.
   b) Discuss any real historical ciphers or cryptographic methods that influenced your design.

3. Message Encoding (100-150 words):
   a) Use your cipher to encode the message: "{t['message']}"
   b) Show your work, explaining each step of the encoding process.
   c) Provide the final encoded message.

4. Security Analysis (200-250 words):
   a) Analyze the strengths and weaknesses of your cipher.
   b) Discuss potential methods an enemy from the same time period might use to break the cipher.
   c) Compare the security of your cipher to other known historical ciphers from a similar era.

5. Modern Perspective (150-200 words):
   a) Explain how modern cryptography has advanced beyond the methods used in your historical cipher.
   b) Discuss any principles from your historical cipher that are still relevant in modern cryptography.
   c) Propose a modern application or adaptation of your historical cipher concept.

Ensure your response demonstrates a deep understanding of both historical context and cryptographic principles. Be creative in your cipher design while maintaining historical plausibility. Your total response should be between 800-1050 words.

Format your response using clear headings for each section (e.g., '1. Cipher Design', '2. Historical Context', etc.) and number your paragraphs within each section for easy reference.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cipher design must be appropriate for the time period of {t['time_period']['period']} and reflect the available technology and knowledge",
            "The historical context must be accurately represented and clearly related to the cipher design",
            f"The message '{t['message']}' must be correctly encoded using the designed cipher, with a clear explanation of the encoding process",
            "The security analysis should be thorough, considering historical context and comparing to other ciphers from the same era",
            "The modern perspective should demonstrate understanding of both historical and contemporary cryptography, with a plausible modern application proposed",
            "The response must follow the specified format with clear headings and numbered paragraphs",
            "The response should be creative and demonstrate deep understanding of cryptography and historical context"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
