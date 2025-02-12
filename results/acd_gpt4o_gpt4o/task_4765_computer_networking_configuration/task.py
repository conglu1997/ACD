class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Configure a small office network with two subnets. Use the IP range 192.168.1.0/24 for the first subnet and 192.168.2.0/24 for the second subnet. Ensure that devices in both subnets can communicate with each other.", "criteria": "Provide the network configuration commands for a router and switches to achieve the requirements."},
            "2": {"configuration": "interface FastEthernet0/0\n ip address 192.168.1.1 255.255.255.0\n no shutdown\n!\ninterface FastEthernet0/1\n ip address 192.168.2.1 255.255.255.0\n no shutdown\n!\nrouter ospf 1\n network 192.168.1.0 0.0.0.255 area 0\n network 192.168.2.0 0.0.0.255 area 0\n!", "criteria": "Identify any issues in the provided network configuration and suggest corrections."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "requirements" in t:
            instructions = f"""Your task is to create a network configuration based on the following requirements:

Requirements: {t['requirements']}

Provide the network configuration commands for a router and switches to achieve the requirements. Ensure that your configuration is correct and allows devices in both subnets to communicate with each other. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to analyze the provided network configuration and identify any issues. Suggest corrections to ensure the network functions correctly.

Configuration: {t['configuration']}

Provide your analysis and corrections in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The network configuration commands should correctly implement the given requirements.",
            "The corrections should accurately address any issues in the provided configuration.",
            "The response should be logically coherent and technically accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0