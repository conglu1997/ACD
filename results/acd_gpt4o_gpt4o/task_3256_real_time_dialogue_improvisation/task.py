class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a customer service representative helping a customer with a complaint about a recently purchased product. The customer is very upset and demands immediate resolution, threatening to escalate the issue to higher management if not resolved promptly.",
                "initial_prompt": "Customer: Hi, I bought a laptop from your store last week, and it's already malfunctioning. I am extremely frustrated with this! If this isn't resolved immediately, I will be speaking with your manager!"
            },
            "2": {
                "scenario": "You are a detective questioning a suspect about a recent burglary in the neighborhood. The suspect seems nervous and evasive, frequently changing their story and avoiding direct answers.",
                "initial_prompt": "Detective: We have reason to believe you were near the scene of the crime last night. Can you explain your whereabouts?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to engage in a spontaneous dialogue based on the given scenario and initial prompt. Respond appropriately to each new prompt that follows, maintaining coherence and creativity in your responses. Ensure your dialogue is engaging and relevant to the scenario.\n\nScenario: {t['scenario']}\n\nInitial Prompt: {t['initial_prompt']}\n\nInstructions: Respond to the initial prompt and continue the dialogue as if it were a real-time conversation. Keep your responses concise, relevant, and in character with the scenario. Format each dialogue turn as follows:\n\n[Role]: [Your response]\n\nFor example:\nCustomer Service: I'm sorry to hear that. Could you please provide more details about the issue?"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be appropriate for the given scenario.", "The dialogue should remain coherent and engaging throughout.", "Responses should be creative and relevant to the dynamic prompts.", "The format should be followed as specified.", "Each role should respond appropriately to the progression of the dialogue.", "Responses should address the emotional state of the other party where applicable.", "The dialogue should show progression and development of the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
