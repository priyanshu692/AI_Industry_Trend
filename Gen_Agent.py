import openai

# Set your API key
openai.api_key = 'your-openai-api-key'


def generate_use_cases(industry, company_focus):
    prompt = f"""
    You are a market research assistant. Given the following industry and company's focus areas, propose 3 actionable use cases that leverage AI, ML, or Generative AI to improve business operations and customer experience.

    Industry: {industry}
    Company Focus: {company_focus}

    Please provide three concrete and detailed use cases.
    """

    # Use the new OpenAI API method
    response = openai.completions.create(
        model="text-davinci-003",  # You can replace this with the appropriate model
        prompt=prompt,
        max_tokens=300
    )

    return response['choices'][0]['text'].strip()


if __name__ == "__main__":
    industry = "Automotive Industry"
    company_focus = "Supply Chain Optimization, Predictive Maintenance"
    #use_cases = generate_use_cases(industry, company_focus)
#    print("Generated Use Cases:\n", use_cases)
