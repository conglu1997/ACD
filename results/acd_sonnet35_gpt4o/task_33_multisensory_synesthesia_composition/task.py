import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synesthesia_types = [
            {
                "type": "Chromesthesia",
                "description": "Association of sounds with colors",
                "input": "A piece of classical music",
                "output": "A detailed visual description"
            },
            {
                "type": "Lexical-gustatory synesthesia",
                "description": "Association of words with tastes",
                "input": "A short poem",
                "output": "A gourmet dish description"
            },
            {
                "type": "Spatial-sequence synesthesia",
                "description": "Perception of numerical sequences as points in space",
                "input": "A mathematical equation",
                "output": "A landscape description"
            }
        ]
        return {str(i+1): synesthesia for i, synesthesia in enumerate(random.sample(synesthesia_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a multisensory composition based on the following synesthesia type:

{t['type']}: {t['description']}

Your task is to translate the given input into the specified output format, as if you were experiencing this form of synesthesia. Follow these steps:

1. Briefly explain the synesthesia type and how it affects perception (2-3 sentences).
2. Provide a sample input in the given input format ({t['input']}).
3. Create a detailed output in the specified format ({t['output']}) that corresponds to your synesthetic experience of the input.
4. Explain the rationale behind your synesthetic associations (2-3 sentences).
5. Describe how this type of synesthesia might impact daily life for someone who experiences it (2-3 sentences).

Provide your response in the following format:

Synesthesia Explanation:
[Your explanation]

Input:
[Your sample input]

Synesthetic Output:
[Your detailed output]

Association Rationale:
[Your explanation]

Impact on Daily Life:
[Your description]

Ensure that your composition is creative, detailed, and demonstrates a clear understanding of the synesthesia type and its potential effects on perception."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific synesthesia type: {t['type']}",
            "The synesthesia explanation should be accurate and concise",
            f"The input should be in the format of {t['input']}",
            f"The synesthetic output should be a detailed {t['output']} that creatively interprets the input",
            "The association rationale should logically connect the input and output",
            "The impact on daily life should be plausible and insightful",
            "The response should demonstrate both scientific understanding and creativity",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
