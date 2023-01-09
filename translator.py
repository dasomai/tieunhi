import googletrans

def translate(text, direction):
  # Initialize the Google Translate API client
  translator = googletrans.Translator()

  # Translate the text from Vietnamese to English or vice versa
  try:
    if direction == 'vi_en':
      translated_text = translator.translate(text, dest='en', src='vi').text
    elif direction == 'en_vi':
      translated_text = translator.translate(text, dest='vi', src='en').text
  except:
      translated_text = ''




  return translated_text

# # Translate a message from Vietnamese to English
# text = "Xin chào, thế giới!"
# translated_text = translate(text, 'vi_en')
# print(translated_text)

# # Translate a message from English to Vietnamese
# text = "Hello, world!"
# translated_text = translate(text, 'en_vi')
# print(translated_text)
