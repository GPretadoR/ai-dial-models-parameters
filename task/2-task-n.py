from task.app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

# Try GPT-4o with n=3
print("\n" + "="*60)
print("Testing GPT-4o with n=3")
print("="*60)
run(
    deployment_name='gpt-4o',
    n=3
)

# Try Claude 3.7 Sonnet with n=2
print("\n" + "="*60)
print("Testing Claude 3.7 Sonnet with n=2")
print("="*60)
run(
    deployment_name='claude-3-7-sonnet@20250219',
    n=2
)

# Try Gemini 2.5 Pro with n=5
print("\n" + "="*60)
print("Testing Gemini 2.5 Pro with n=5")
print("="*60)
run(
    deployment_name='gemini-2.5-pro',
    n=5
)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
