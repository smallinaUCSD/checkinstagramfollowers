from bs4 import BeautifulSoup

# Function to extract Instagram handles from the HTML file
def extract_handles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        handles = []
        for a_tag in soup.find_all('a', href=True):
            handle = a_tag.text.strip()
            if handle:
                handles.append(handle)
        return set(handles)

# Load the follower and following data
followers = extract_handles('/path/to/your/followers_1.html')
following = extract_handles('/path/to/your/following.html')

# Find accounts you follow that don't follow you back
not_following_back = following - followers

# Display the list of handles not following back
if not_following_back:
    print("Accounts that don't follow you back:")
    for handle in sorted(not_following_back):
        print(handle)
else:
    print("Everyone you follow follows you back!")
