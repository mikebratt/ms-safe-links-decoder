import urllib.parse

# Get SafeLink URL from user input
safelink_url = input("Enter SafeLink URL: ")

# Find the start of the original URL
start_index = safelink_url.find("?url=")
if start_index == -1:
    print("Invalid SafeLink URL")
    exit()

# Extract the original URL part
original_url = safelink_url[start_index + len("?url="):]

# Find the end of the original URL
end_index = original_url.find("&data=05%7C02%7C")
if end_index != -1:
    original_url = original_url[:end_index]

# Decode the URL
decoded_url = urllib.parse.unquote(original_url)

# Print the decoded URL
print("\n", decoded_url, "\n")