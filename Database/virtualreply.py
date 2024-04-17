reply_dictionary = {
    "Hi":"Hi, How can I help you.","Hello":"Hello, How can I assist you.","Good morning":"Good morning, What can I do for you.",
    "Good afternoon": "Good afternoon, How may I help you.","Good evening":"Good evening, How can I assist you.",
    "Hey there":"Hey, How can I help you.","Hey":"Hey, How can I help you",
    "नमस्ते":"नमस्ते बताइए मैं आपकी कैसे सेवा कर सकती हूँ","प्रणाम":"प्रनाम सेवा बताइये","अभिवादन":"अभिवादन मैं आपकी क्या सेवा कर सकती हूँ",
    "शुभ प्रभात":"शुभ प्रभात मैं आपकी क्या सेवा कर सकती हूँ","राम-राम ":"राम-राम, मैं आपकी क्या सेवा कर सकती हूँ"
}

def virtual_reply(text):
    
    if text in reply_dictionary:
        return reply_dictionary[text]
    else:
        return "Please speak clearly. कृपया स्पष्ट भाषा का प्रयोग करें"

msg = input("Enter caller's name: ")
print(virtual_reply(msg))
