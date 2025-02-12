import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture': 'Nomadic desert dwellers who can only communicate at night',
                'environment': 'Vast desert with frequent sandstorms',
                'constraint': 'Communication must be visible from a distance but leave no permanent trace'
            },
            {
                'culture': 'Subterranean society with limited access to surface materials',
                'environment': 'Network of underground caves and tunnels',
                'constraint': 'Communication must be entirely tactile or auditory'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a unique and creative communication system for a fictional culture with the following characteristics:

Culture: {t['culture']}
Environment: {t['environment']}
Constraint: {t['constraint']}

Your task:
1. Create a detailed communication system that fits the given cultural and environmental constraints. Your system should:
   a) Use at least two different elements or dimensions to encode information (e.g., color and shape, pitch and duration)
   b) Have a way to represent at least 20 distinct concepts or words
   c) Include a method for combining these concepts to form more complex messages
Describe the medium, method, and special features of your system (4-5 sentences).

2. Explicitly explain how your system meets each of the given constraints (2-3 sentences).

3. Provide 3 example messages in your system, along with their meanings. Each message should demonstrate a different aspect of your system.

4. Explain the logic behind your communication system, including how it encodes information (2-3 sentences).

5. Describe how this system reflects the culture and adapts to the environment (2-3 sentences).

6. Discuss one potential limitation of your system and propose a solution (2-3 sentences).

7. Decode the following message that uses your communication system:
"The oasis has dried up. Move to the backup location."

8. Encode the following message using your communication system:
"Dangerous predators spotted nearby. Remain silent and hidden."

Note: Your communication system should be original and creative. Simple substitution ciphers or morse code-like systems are not sufficient for this task.

Provide your response in the following format:

Communication System Description:
[Your detailed description]

Constraint Compliance:
[Explanation of how your system meets each constraint]

Example Messages:
1. [Message in your system]: [Meaning]
2. [Message in your system]: [Meaning]
3. [Message in your system]: [Meaning]

System Logic:
[Your explanation]

Cultural and Environmental Adaptation:
[Your description]

Limitation and Solution:
[Your discussion]

Decoded Message:
[Your decoded message using your system]

Encoded Message:
[Your encoded message using your system]

Explanation of Encoding/Decoding:
[Briefly explain how you applied your system to encode and decode the messages]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The communication system is unique, creative, and fully adheres to the given cultural and environmental constraints.",
            "The system uses at least two different elements to encode information and can represent at least 20 distinct concepts.",
            "The system description is detailed and clearly explains the medium, method, and special features (4-5 sentences).",
            "The constraint compliance is explicitly explained for each given constraint.",
            "The example messages demonstrate a consistent and logical use of the communication system, each highlighting a different aspect.",
            "The system logic is clearly explained, including how it encodes information.",
            "The cultural and environmental adaptation is thoughtfully described and directly relates to the given scenario.",
            "A plausible limitation and solution are provided, showing deep consideration of the system's practical use.",
            "The decoded message accurately represents 'The oasis has dried up. Move to the backup location.' using the created system.",
            "The encoded message accurately represents 'Dangerous predators spotted nearby. Remain silent and hidden.' using the created system.",
            "The explanation of encoding/decoding demonstrates a clear and consistent application of the system's rules."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
