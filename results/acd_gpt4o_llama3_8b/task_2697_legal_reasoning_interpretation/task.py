class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "legal_text": "In a contract for the sale of goods, the seller must deliver the goods, and the buyer must accept and pay for the goods in accordance with the terms of the contract. If the seller delivers goods that do not conform to the contract, the buyer may reject them, provided that the rejection is made within a reasonable time after delivery and the buyer notifies the seller of the rejection. If the buyer accepts the goods despite their non-conformity, the buyer may claim damages for the non-conformity.",
                "scenario": "Jane purchases 100 widgets from Acme Corp. The contract specifies that the widgets must be blue. Acme Corp delivers 100 red widgets. Jane does not notify Acme Corp of the rejection within a reasonable time and uses the red widgets in her production line. She now wants to claim damages for the non-conformity. Can Jane claim damages?"
            },
            "2": {
                "legal_text": "A person who is negligently injured by another may recover damages for the injury. Negligence is the failure to exercise the care that a reasonably prudent person would exercise in like circumstances. To prove negligence, the injured party must demonstrate that the defendant owed a duty of care to the plaintiff, the defendant breached that duty, and the breach caused the plaintiff's injuries.",
                "scenario": "John is walking through a park and is hit by a cyclist who is riding on a path clearly marked for pedestrians only. John suffers a broken leg and incurs medical expenses. Can John recover damages from the cyclist?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "You will be given a legal text and a hypothetical scenario. Your task is to interpret the legal text and apply it to the scenario to determine the legal outcome. Provide a detailed explanation of your reasoning and conclusion."
        instructions += "\nLegal Text: " + t['legal_text']
        instructions += "\nScenario: " + t['scenario']
        instructions += "\nSubmit your response as a plain text string in the following format:"
        instructions += "\nResponse: [Your detailed explanation and conclusion]"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should accurately interpret the legal text and apply it to the scenario.", "The response should provide a detailed explanation of the reasoning and conclusion."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
