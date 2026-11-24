# Generate a blog with openAI

import openai
from dotenv import dotenv_values

# get API key from .env file
config = dotenv_values('.env')
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3 # 1 is most random, 0 is least random
  )
  retrieve_blog = response.choices[0].text
  return retrieve_blog

#print(generate_blog('How to make a blog with openAI'))

# Multiple Paragraphs

keep_writing = True # let user choose when to stop writing paragraphs

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False