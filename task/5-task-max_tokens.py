from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?

# With max_tokens=10 - response will be cut short
print("\n" + "="*60)
print("Testing with max_tokens=10 (response will be truncated)")
print("="*60)
run(
    deployment_name='gpt-4o',
    max_tokens=10
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.