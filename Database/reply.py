intents = {
    "greeting": {
        "patterns": [
            "Hello", "Hi", "Howdy", "Greetings", "Good Morning", "Good afternoon",
            "Good evening", "Hi there", "Hey there", "Whats up", "Hello there", "Salutations",
            "Yo", "Hey", "Well! Hello", "Hi, Friend", "Hey Buddy", "Hi Buddy!",
            "नमस्ते", "प्रणाम", "अभिवादन", "नमस्कार", "शुभ प्रभात", "जय हिन्द", "सुप्रभात", "राम राम", "नमस्ते नमस्ते"
        ],
        "responses": [
            "Hello How can I assist you?", "Hi there!", "Hey! What can I do for you?",
            "Howdy! What brings you here?", "Greetings! How may I help you?",
            "Good Morning! How can I be of service", "Good afternoon! What do you need assistance with?",
            "Good evening! How may I assist you?", "Hey there! How can I help you?", "Hi! What's on your mind",
            "Hello there! How can I assist you there?", "Yes sir how may I assist you!", "Yes Sir please tell your need!",
            "Hey! How can I be of service", "Hello sir, How can I help you", "Hello dear! How may I help you",
            "Hello buddy! How may I help you", "Yes buddy, What brings you here?",
            "नमस्ते बताइए मैं आपकी कैसे सेवा कर सकती हूँ?", "प्रनाम सेवा बताइये?",
            "अभिवादन मैं आपकी क्या सेवा कर सकती हूँ?", "नमस्कार बताइए मैं आपकी कैसे सेवा कर सकती हूँ?", "शुभ प्रभात सेवा बताइये?",
            "जय हिन्द मैं आपकी क्या सेवा कर सकती हूँ? ", "सुप्रभात सेवा बताइये? ", "राम राम सेवा बताइये?",
            "नमस्ते बताइए मैं आपकी कैसे सेवा कर सकती हूँ?"
        ]
    },
    "Police": {
    "patterns": [
        "assault and battery", "bomb threat", "breach of peace", "carjacking", "child abduction",
        "credit card fraud", "cyberstalking", "domestic abuse", "embezzlement", "extortion",
        "hit-and-run", "human trafficking", "identity theft", "illegal gambling", "kidnapping",
        "manslaughter", "missing person", "money laundering", "narcotics trafficking", "public intoxication",
        "reckless driving", "resisting arrest", "sexual assault", "stalking", "suspicious package",
        "terrorist threat", "vandalism", "warrant arrest", "weapons possession", "white-collar crime",
        "धारा 377", "अपहरण और लूट", "आतंकवादी धमकी", "हिंसा और बैटरी", "जाली नकली",
        "ड्रग्स तस्करी", "धरना-प्रदर्शन", "कारबारी धोखाधड़ी", "भ्रष्टाचार", "आतंकवाद",
        "मानहानि", "समुद्री डकैती", "अवैध शराब", "सार्वजनिक शराब", "जाली नकली",
        "पर्यवेक्षण", "मिलावट", "समुद्री डकैती", "किसी की बातचीत का अनधिकृत रूप से सुनना",
        "सार्वजनिक व्यवहार", "धारा 302", "हिंसा और बैटरी", "उग्रता और आपातकालीन स्थितियों का निर्माण",
        "क्राइम स्थान की जांच", "शांति अभियान", "अवैध शिकार", "भ्रष्टाचार और अपराध",
        "सामाजिक न्याय", "न्यायिक शिकायत", "उग्र नागरिकों का निर्माण", "हिंसा और बल",
        "धर्मांतरण", "आत्म हत्या", "विचित्र प्रकरण", "धोखाधड़ी और लूट", "बच्चों की अपहरण",
        "उद्धारण", "स्पष्ट बंदूक", "आतंकवादी हमला", "उद्धार और रक्षा", "न्यायिक अधिकार का उल्लंघन",
        "अपराधिक मामला", "गवाह बदल", "विचारात्मक अधिकार", "संशोधित उपयोगी सूचना", "गार्डियनशिप अधिकार",
        "प्रतिबंध कार्यवाही", "द्वंद्विता", "आपराधिक रूप से अतिक्रमण", "पुलिस स्थिति का निरीक्षण",
        "अपराधिक रूप से बहाव"
    ],
    "responses": [
        "Police is on the way to handle the situation. Their GPS location is being sent to you on your phone number!",
        "Please remain calm. Police assistance is being dispatched to your location. Stay safe!",
        "Law enforcement is being deployed to your location. Keep yourself safe and await their arrival.",
        "पुलिस आ रही है स्थिति का संभालन करने के लिए। उनकी जीपीएस स्थान को आपके फोन नंबर पर भेजा जा रहा है!"
    ]
},

   "ambulance": {
    "patterns": [
        "heart attack", "stroke", "choking", "severe bleeding", "respiratory distress",
        "unconsciousness", "overdose", "poisoning", "allergic reaction", "seizure",
        "high fever", "diabetic emergency", "traumatic injury", "burns", "drowning",
        "electrocution", "major accident", "fall from height", "car crash", "sports injury",
        "acute abdominal pain", "difficulty breathing", "chest pain", "head injury",
        "neck or back injury", "suspected fracture", "bleeding wounds", "loss of consciousness",
        "सिरदर्द", "हार्ट अटैक", "स्ट्रोक", "अत्यधिक रक्तस्राव", "संकुचित श्वसन",
        "अवचेतना", "अधिक तापमान", "डायबिटिक आपातकालीन", "चोट", "जलन",
        "विद्युत द्वारा दुर्घटना", "मुख्य दुर्घटना", "उच्चतम दुर्घटना", "गाड़ी का क्रैश",
        "खेल की चोट", "गंभीर पेट दर्द", "सांस लेने में कठिनाई", "सीने में दर्द", "सिर में चोट",
        "गर्दन या पीठ की चोट", "संदिग्ध टूट", "रक्तस्राव या वायदंड", "चेतना की हानि"
    ],
    "responses": [
        "An ambulance is en route to your location. Please stay calm and await assistance.",
        "Emergency medical services are on their way. Keep yourself safe and await their arrival.",
        "Medical assistance is being dispatched to your location. Help is on the way!",
        "आपके स्थान के लिए एक रोगी वाहन रास्ते में है। कृपया शांत रहें और सहायता का इंतजार करें।"
    ]
},

    "Firebrigade": {
    "patterns": [
        "house fire", "building fire", "wildfire", "forest fire", "vehicle fire",
        "industrial fire", "chemical spill", "gas leak", "explosion", "smoke alarm",
        "carbon monoxide alarm", "fire evacuation", "fire safety inspection",
        "fire drill", "fire suppression", "firefighting equipment", "fire hydrant",
        "fire prevention", "fire damage assessment", "emergency fire response",
        "fire department contact", "fire emergency", "fire safety tips",
        "घर में आग", "इमारत में आग", "जंगली आग", "वाहन आग",
        "औद्योगिक आग", "रासायनिक धमाका", "गैस छिद्रण", "विस्फोट", "धुआं अलार्म",
        "कार्बन मोनोक्साइड अलार्म", "आग निकासी", "आग सुरक्षा निरीक्षण",
        "आग ड्रिल", "आग का दमन", "आग बुझाने की उपकरण", "आग नल",
        "आग निवारण", "आग के क्षति का मूल्यांकन", "आपात आग्रह संबंधित",
        "आग विभाग संपर्क", "आग आपात", "आग सुरक्षा सुझाव"
    ],
    "responses": [
        "The fire brigade is on their way to your location. Stay safe and await assistance.",
        "Emergency firefighting services are being dispatched. Please follow safety protocols until help arrives.",
        "Firefighting units are en route to your location. Keep calm and await assistance.",
        "आपके स्थान के लिए अग्निशमन दल रास्ते में है। कृपया सुरक्षित रहें और सहायता का इंतजार करें।"
    ]
}

}
