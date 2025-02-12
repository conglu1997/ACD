class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Your friend recently lost their beloved pet and is feeling devastated. The pet was with them for over 10 years and was like a family member. Write a letter to console them."},
            "2": {"scenario": "Your colleague has recently faced a difficult breakup after a long-term relationship and is struggling to cope with the emotional aftermath. Write a letter to offer your support and understanding."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write an empathetic letter in response to the following scenario: '{t["scenario"]}'. Your letter should:
1. Acknowledge the person's feelings and the situation they are going through.
2. Offer words of comfort and support.
3. Provide any advice or perspective that might help them cope.
4. Be sincere, compassionate, and understanding.

Submit your letter as a plain text string in the following format:

Dear [Recipient],

[Body of the letter]

Sincerely,
[Your Name]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The letter should acknowledge the person's feelings and situation.",
            "The letter should offer words of comfort and support.",
            "The letter should provide any advice or perspective that might help them cope.",
            "The letter should be sincere, compassionate, and understanding.",
            "The letter should follow the required format: 'Dear [Recipient],\n\n[Body of the letter]\n\nSincerely,\n[Your Name]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
