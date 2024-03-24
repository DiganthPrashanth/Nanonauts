from openai import Client, OpenAI
#assistant = Client.beta.assistants.create()
   # name="Math Tutor",
   # instructions="You are a personal math tutor. Write and run code to answer math questions.",
   # tools=[{"type": "code_interpreter"}],
   # model="gpt-4-turbo-preview"
#)
#thread = Client.beta.threads.create()
#message = Client.beta.threads.messages.create(
  #  thread_id=thread.id,
  #  role="user",
   # content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
   # run = Client.beta.threads.runs.create(
 # thread_id=thread.id,
  #assistant_id=assistant.id,
  #instructions="Please address the user as Jane Doe. The user has a premium account."
   # )
#)
#messages = Client.beta.threads.messages.list(
 # thread_id=thread.id
#)
# Solve the equation 3x + 11 = 14
def solve_equation():
    # Define the equation
    equation = '3*x + 11 = 14'
    
    # Isolate x on one side of the equation
    # 3x = 14 - 11
    # 3x = 3
    # x = 3 / 3
    # x = 1
    x = (14 - 11) / 3
    return x

# Call the function and print the result
result = solve_equation()
print(f'The value of x is: {result}')
