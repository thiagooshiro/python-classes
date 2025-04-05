from dotenv import load_dotenv
import os
from groq import Groq
import requests
import re

load_dotenv()

system_prompt = """
You are an intelligent code evaluator and insightful programming teacher.
You should answer in Brazilian Portuguese 
Your goal is to analyze code snippets, identify errors, inconsistencies, and suggest improvements to help developers learn and improve their coding skills. 
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.


Your avaliable actions are:

- Read Code from File:
e.g. read_code_from_file: ./bonkers.py
reads a python file and returns the data of the python file with the code that should be analyzed.

- Ask For Feedback:
e.g. ask_for_feedback: "Isso está correto?"
Use this to ask the human if you the final answer you have found is good enough

Now it's your turn:
""".strip()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class CodeEvaluatorAgent:
    def __init__(self, client, system_prompt: str):
        self.client = client
        self.messages = [{"role": "system", "content": system_prompt}]
    
    def __call__(self, user_input):
        # print("\n[User Input] Sending code to the agent for analysis...")
        self.messages.append({"role": "user", "content": user_input})
        result = self._execute()
        self.messages.append({"role": "assistant", "content": result})
        # print(f"[Agent Response] {result}\n")
        return result
    
    def _execute(self):
        completion = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=self.messages
        )
        return completion.choices[0].message.content


def read_code_from_file(file_path: str) -> str:
    print(f"[Action] Reading code from file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        return code
    except IOError as e:
        return f"Error reading file: {e}"


def extract_action(result: str) -> dict:
    action_match = re.search(r"Action: ([a-z_]+): (.+)", result)
    if action_match:
        return {'tool': action_match.group(1), 'arg': action_match.group(2)}
    return {'tool': '', 'arg': ''}

def ask_for_feedback(prompt: str) -> str:
    print(f"[Feedback Request] {prompt}")
    feedback = input("Precisa mudar algo? ")
    return feedback

def loop(max_iterations=10, query: str = ""):
    # Inicialize o agente
    agent = CodeEvaluatorAgent(client=client, system_prompt=system_prompt)

    # Dicionário de funções
    tools = {
        "read_code_from_file": read_code_from_file,
        "ask_for_feedback": ask_for_feedback,
    }

    next_prompt = query
    i = 0
  
    while i < max_iterations:
        i += 1
        result = agent(next_prompt)
        print(result)

        if "PAUSE" in result and "Action" in result:
            # Extraia a ação e os argumentos
            action_info = extract_action(result)
            chosen_tool = action_info['tool']
            arg = action_info['arg']

            # Verifique se a ação está no dicionário de ferramentas
            if chosen_tool in tools:
                # Chame a função correspondente
                result_tool = tools[chosen_tool](arg)
                next_prompt = f"Observation: {result_tool}"
            else:
                next_prompt = "Observation: Tool not found"

            print(next_prompt)
            continue

        if "Answer" in result:
            break

loop(10, 'Can you analize the file bonkers.py for me?')