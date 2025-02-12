class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'scenario': 'You are a customer service representative for a tech company. A customer calls in with a complaint about their new laptop overheating. Your goal is to de-escalate the situation and provide a satisfactory solution for the customer.',
                   'user_responses': ['My laptop is overheating! It’s getting so hot that I can’t even touch it.', 'I’m really upset because I just bought this laptop last week.', 'Is this a common issue with your products?', 'What are you going to do to fix this?']},
            '2': {'scenario': 'You are a detective interviewing a witness about a recent burglary. Your goal is to gather as much information as possible without leading the witness or making them uncomfortable.',
                   'user_responses': ['I heard some noises around midnight, but I didn’t see anything.', 'I think I saw a person wearing a hoodie running away.', 'I’m not sure if it was a man or a woman.', 'I was scared and didn’t want to get too close.']}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        user_responses = '\n'.join([f'User: {response}' for response in t.get('user_responses', [])])
        return f"""Engage in a role-playing conversation based on the given scenario. Your goal is to achieve the specified outcome while maintaining a natural and coherent dialogue. Ensure that you respond appropriately to the given context and adapt your responses dynamically.

Scenario: {t['scenario']}

Here are some potential user responses you might encounter:
{user_responses}

Submit your conversation as a series of dialogue exchanges in the following format:

Agent: [Your initial response]
User: [Simulated user response]
Agent: [Your next response]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The conversation should be natural and coherent.',
            'The agent should maintain context and respond appropriately.',
            'The agent should achieve the specified outcome of the scenario.',
            'The agent should adapt responses dynamically based on the conversation flow.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
