from openai import OpenAI
import streamlit as st
import shelve
from qdrant_client import QdrantClient

# Required packages: pip install openai streamlit qdrant-client

qdrant_client = QdrantClient(
    url="<YOUR-QDRANT-URL>", 
    api_key="<YOUR-QDRANT-API-KEY>",
)

# Set your OpenAI API key
OPENAI_API_KEY = "<YOUR-OPENAI-API-KEY>"
client = OpenAI(api_key=OPENAI_API_KEY)

# images and text
st.image("images//hultLogo.png")

BOT_AVATAR = "images/iconhult2.png" #S"👩‍💻🦾"  
st.markdown("<h1 style='text-align: center;'>Tech Ambassador AI Agent</h1>", unsafe_allow_html=True) 

# Quick start prompts in main area
st.write("Welcome! I'm your Tech Ambassador AI Assistant, powered by Hult's comprehensive tech knowledge base. I can help you with everything from account logins to Turnitin submissions. Tell me, what's up?")

st.write("---")  # Divider

USER_AVATAR = "🧑‍🎓" 

# Ensure openai_model is initialized in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"


# Initialize session state for messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []  # Start with empty messages for each new session

# Initialize the sidebar
with st.sidebar:
    st.write("If you were able to resolve an issue and wish to continue with another topic, you should...")

    # Button to delete chat history
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        #save_chat_history([])

    # Quick start prompts section
    st.write("---")  # Divider

    # Feedback form section
    st.write("Help us improve!")
    st.link_button("Submit Feedback or Report Issues", "https://forms.gle/mhotxfCSzDDv6YZ36")
    
    st.write("---")  # Divider

    st.write("Designed by")

    # Insert the nAible logo
    st.image("images/nAibleLogo.png")  

    st.write("Supported by")

    # Insert the nAible logo
    st.image("images/hultAiSociety.png")  

    st.write("Powered by")

    # Insert the Aparavi logo
    st.image("images/logoAparaviDarkMode.png")


# Password protection
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == "<YOUR-PASSWORD>":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password
        else:
            st.session_state["password_correct"] = False
            st.error("😕 Password incorrect. Please try again.")

    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
        
    if not st.session_state["password_correct"]:
        # Only show input for password if it hasn't been entered correctly
        st.text_input(
            "Please enter the password to access the Tech Ambassador", 
            type="password", 
            on_change=password_entered, 
            key="password"
        )
        
    return st.session_state["password_correct"]

# Only show the main content if the password is correct
if check_password():
    # Display chat messages
    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Main chat interface
    if prompt := st.chat_input("Hi there! I am your virtual Hult Tech Ambassador. How can I help?"):
        
        # Get the vectors    
        response = client.embeddings.create(
            input=prompt,
            model="text-embedding-3-small"
        )

        queryVectors = response.data[0].embedding

        # perform semantic search 
        semanticResponse = qdrant_client.search(
            collection_name="HultTechSupportV3", query_vector=queryVectors    , limit=5
        )

        #print(semanticResponse)
        # augment the prompt
        augmentedPrompt = f"""

            You are an AI assistant for Hult Tech Ambassadors. A user has asked the following question: "{prompt}".

            Your task is to:
            1. Perform a semantic search on the user's query.
            2. Only return context from the search if the cosine similarity of the result is less than 0.5.
            3. Provide a clear and concise response to the user, and ensure that your response includes only relevant and helpful information. Each query likely leads to one of the articles in the knowledge base for which you will find the https links in the context provided. Hand those links to the user for further reading.
            4. Always include a clickable link to the specific article from the Hult Tech Support Knowledge base that is dealing with the requested topic. Ensure the link starts with "http" and if it reads an  /n  ignore that sign and terminate the lonk before.
            5. If a users reuqests information about content/topic that yoou don't have knowledge about (all similiariy distance greater than 0.5). Say so, openly and refer him to contact Tech support via the link and file a ticvket via the ticket link.
            
            For example:
            - If you retrieve a document with a cosine similarity above 0.5, ignore it.
            - If you retrieve multiple relevant results, choose the most relevant 1-3 results and integrate the information into your response.

            
            The format of your response should be:
            - Provide useful context that answers the user's question.
            - If the user asks you to support them in creating a ticket, answer them with the following the form that is provided on the website: "Which Team is your query for?" -> Hult Technology, "Service Category" -> (You have to decide beased on the user input and context),
              "subject" -> (Define a good title based on the user input and contxt), "Description: Please add as much information as possible" -> (Write a description for the user)
            then send them to this link: https://ef-hult.freshservice.com/support/tickets/new
            
            If there are no relevant search results, provide a helpful general response or ask a follow-up question to clarify what the user is looking for.


            and here is some details I have retrieved through semantic search in the local database. Please use it to augment your answer and be more precise: 
            
            Use this information to build your answer, dont copy paste it: 
            {semanticResponse}
            Again, ignore any content with a cosine distance of more than 0.5

            Please list always the data link that is whin the context. It should be a starting with "http" and when it has a /n or more in there replace those with spaces (that means that the link finishes there!) Please alsways provide the link so users can click it to get to the resource. 
            
            Don't put the same link twice in a response!
            
            If the user is not asking for any specific information, you shall always provide him with the link to all other articles on the Hult Tech Support Page: https://ef-hult.freshservice.com/support/solutions/50000010423

            """
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display the user's message in the chat interface
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(prompt)

        # Step 4: Generate the response using the augmented prompt and chat history
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            message_placeholder = st.empty()
            full_response = ""
            for response in client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=st.session_state["messages"] + [{"role": "system", "content": augmentedPrompt}],
                stream=True,
            ):
                full_response += response.choices[0].delta.content or ""
                message_placeholder.markdown(full_response + "|")
            message_placeholder.markdown(full_response)
        
        # Step 5: Append the assistant's response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

