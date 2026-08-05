data={
     "NLP":
 {"domain_name":"NLP",
"description":"natural language procesing",
"two_real_world_aplication":"1.Virtual Assistants,2.Machine Translation",
"popular_python_libaries_useed":"1.spaCy,2.Toolkit"
},
"computer_vision":
{"domain_name":"computer_vision",
"description":"natural language procesing",
"two_real_world_aplication":"1.Virtual Assistants,2.Machine Translation",
"popular_python_libaries_useed":"1.spaCy,2.Toolkit"
},
"speech_processing":
{"domain_name":"speech_processing",
"description":"natural language procesing",
"two_real_world_aplication":"1.Voice Assistants 2.Automatic Medical Transcription",
"popular_python_libaries_useed":"1.OpenAI Whisper,2.SpeechRecognition"
},
"robotics":
{"domain_name":"robotics",
"description":"natural language procesing",
"two_real_world_aplication":"1.automated warehouse logistics 2.industrial manufacturing assembly lines",
"popular_python_libaries_useed":"1.Robot Operating System (ROS 2.opencv"
},
}
print("slecte option:")
print('1.NLP')
print('2.computer_vision')
print('3.speech_processing')
print('4.robotics')
choice=int(input("pls enter your choice :"))
print('user choice',choice)
if choice==1:
    print(data['NLP'])
elif choice==2:
    print(data['computer_vision'])
elif choice==3:
    print(data['speech_processing'])
elif choice==4:
    print(data['robotics'])
