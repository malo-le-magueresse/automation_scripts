from imessage_reader import fetch_data
import pandas as pd 

### DATA READING AND SORTING

def get_messages(DB_PATH):
    fd = fetch_data.FetchData(DB_PATH)
    messages = fd.get_messages()
    return messages

def get_df(messages, contact_numbers):
    df = pd.DataFrame(messages, columns=['User', 'Message', 'Date', 'Service', 'Account', 'IsFromMe'])
    df = df[df['User'].isin(contact_numbers.keys())]
    return df

def messages_data(DB_PATH, contact_numbers):
    messages = get_messages(DB_PATH)
    df = get_df(messages, contact_numbers)
    sorted_df = df.sort_values(by=['Date'], ascending=False)
    return sorted_df 

### DATA CLEANING

# Some messages are reaction messages. We want to remove them, as they may be considered noise. 
def starts_with_prefix(s):
    prefixes = ('Loved ', 'Laughed at ', 'Liked ', 'Disliked ', 'Emphasized ', 'Questioned ')
    you_prefixes = tuple('You ' + str.lower(prefix) for prefix in prefixes)
    return s.startswith(prefixes) or s.startswith(you_prefixes)

def cleaning_messages(df):
    # We need to clean our iMessages, because some of them are not real text messages (e.g., they are images, or they are a reaction). 
    # We will only keep the messages that are real text messages.
    df['Message'] = df['Message'].fillna('')
    df['has_reaction'] = df['Message'].apply(starts_with_prefix)
    attachment_filter = df['Message'].str.contains('<Message with no text, but an attachment.>')
    reaction_filter = df['has_reaction']==True
    df = df[~(attachment_filter | reaction_filter)]
    df.reset_index(inplace=True)
    return df    

def actions_to_take(sorted_df, contact_numbers):
    last_messages = sorted_df.groupby('User').first()
    last_messages['has_reaction'] = last_messages['Message'].apply(starts_with_prefix)

    attachment_filter = last_messages['Message'].str.contains('<Message with no text, but an attachment.>')
    reaction_filter = last_messages['has_reaction']==True
    should_answer = {}
    for k in contact_numbers:
        if k in last_messages.index and not (attachment_filter[k] | reaction_filter[k]):
            should_answer[k] = last_messages.loc[k, 'IsFromMe'] == 0
        else:
            should_answer[k] = False
    return should_answer

def last_messages(cleaned_df, should_answer):
    """ Get the last messages from the interlocutor. There can be several messages. We'll concatenate them. """
    last_messages = {}
    for contact in should_answer.keys():
        print("Contact: " + contact)
        print("Calculating last messages...")
        print("Should we take action? " + str(should_answer[contact]))
        if should_answer[contact]:
            last_user_message_index = cleaned_df[cleaned_df['IsFromMe'] == 1].index[0]
            messages = cleaned_df.iloc[:last_user_message_index].sort_values(by=['Date'], ascending=True)
            last_messages[contact] = ' '.join(messages['Message'])
        print("\n")
    return last_messages

def format_message(row, user_name):
    if row['IsFromMe'] == 1:
        return f"me: {row['Message']}"
    else:
        return f"{user_name}: {row['Message']}"

