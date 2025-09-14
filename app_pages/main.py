from google import genai
import requests
import streamlit as st

# Dictionary
def get_dictionary_word(word):
    dict_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    dict_response = requests.get(dict_url)
    if dict_response.status_code == 200:
        dict_data = dict_response.json()
        dict_result = []

        for meaning in dict_data[0]["meanings"]:
            part_of_speech = meaning.get("partOfSpeech", "N/A")
            
            for definitions in meaning["definitions"]:
                definition_text = definitions.get("definition")
                example_text = definitions.get("example", None)
                
                dict_result.append({
                    "part_of_speech": part_of_speech,
                    "definition_text": definition_text,
                    "example_text": example_text
                    })
        return dict_result
    else:
        return None


# AI
client = genai.Client(api_key=st.secrets["genai"]["api_key"])

# Streamlit UI
st.title("WordMania!")
st.write("### Enter a word above to get started!")
word = st.text_input("Search for a word")

st.write("---")
selection = st.selectbox("Explain like:", ["Pirate", "Shakespeare", "Naruto", "Wizard", "Goku", "Sherlock Holmes", "Vampire", "Napoleon Bonaparte", "Socrates", "Luffy", "Tsundere Girl", "Over-the-top battle announcer", "Charlie Kirk", "Superman", "Batman", "Yandere", "Dio Brando"])

if not word.strip():
    st.error("Please enter a word.")
else:
    with st.spinner("Please wait..."):
        ai_response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents = f"You are {selection}, speaking exactly like {selection}'s character or stereotype. Explain the word '{word}' in exactly three sentences, no more, no less. Use {selection}'s typical tone, vocabulary, and style. Make it entertaining and clear for someone learning the word."   
        )
    st.write(ai_response.text)
    st.write("---")

# Result
if word:
    results = get_dictionary_word(word)
    if results:
        for item in results:
            st.write(f"***Part of Speech***: {item['part_of_speech'].capitalize()}")
            st.write(f"***Definition***: {item['definition_text'].capitalize()}")
            if item['example_text']:
                st.write(f"***Example***: {item['example_text'].capitalize()}")
            st.write("---")

        

          



