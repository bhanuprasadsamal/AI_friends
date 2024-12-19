let btn=document.querySelector("#btn")
let content=document.querySelector("#content")
let voice=document.querySelector("#voice")
// const os = require("os");
let volumeDisplay = document.querySelector("#volumeDisplay");

function speak(text){
    let text_speak=new SpeechSynthesisUtterance(text)
    text_speak.rate=1
    text_speak.pitch=1
    text_speak.volume=1
    text_speak.lang="hi-GB"
    window.speechSynthesis.speak(text_speak)
}

function wishMe(){
    let day=new Date()
    let hours=day.getHours()
    if(hours>=0 && hours<12){
        speak("Good Morning Sir")
    }
    else if(hours>=12 && hours <16){
        speak("Good afternoon Sir")
    }else{
        speak("Good Evening Sir")
    }
}
window.addEventListener('load',()=>{
    wishMe()
})
let speechRecognition= window.SpeechRecognition || window.webkitSpeechRecognition 
let recognition =new speechRecognition()
recognition.onresult=(event)=>{
    let currentIndex=event.resultIndex
    let transcript=event.results[currentIndex][0].transcript
    content.innerText=transcript
   takeCommand(transcript.toLowerCase())
}

btn.addEventListener("click",()=>{
    recognition.start()
    voice.style.display="block"
    btn.style.display="none"
})
function takeCommand(message){
   voice.style.display="none"
    btn.style.display="flex"
    if(message.includes("hello")||message.includes("hey")){
        speak("hello sir,I am chhotu your ai assistant, what can i help you?")
    }
    else if(message.includes("who are you")){
        speak("i am virtual assistant ,created by Bhanu Prasad")
    }else if(message.includes("open youtube")){
        speak("opening youtube...")
        window.open("https://youtube.com/","_blank")
    }
    else if(message.includes("open google")){
        speak("opening google...")
        window.open("https://google.com/","_blank")
    }
    else if(message.includes("open facebook")){
        speak("opening facebook...")
        window.open("https://facebook.com/","_blank")
    }
    else if(message.includes("open instagram")){
        speak("opening instagram...")
        window.open("https://instagram.com/","_blank")
    }
    else if(message.includes("open calculator")){
        speak("opening calculator..")
        window.open("calculator://")
    }
    else if(message.includes("open whatsapp")){
        speak("opening whatsapp..")
        window.open("whatsapp://")
    } else if (message.includes("open notepad")) {
        speak("Opening Notepad...");
        window.open('C:\\Windows\\System32\\notepad.exe');
    } else if (message.includes("open excel")) {
        speak("Opening Excel...");
        window.open("excel://");
    } else if (message.includes("open cmd")) {
        speak("Opening Command Prompt...");
        window.open("cmd://");
    } else if (message.includes("open msword")) {
        speak("Opening MS Word...");
        window.open("msword://");
    } else if (message.includes("sleep")) {
        speak("Going to sleep mode...");
        setTimeout(() => {
            speak("I am back! What can I help you with?");
        }, 5000);  // Simulates sleep for 5 seconds
    } 
    else if(message.includes("time")){
      let time=new Date().toLocaleString(undefined,{hour:"numeric",minute:"numeric"})
      speak(time)
    }
    else if(message.includes("date")){
        let date=new Date().toLocaleString(undefined,{day:"numeric",month:"short"})
        speak(date)
    }else if (message.includes("increase volume")) {
        let audio = document.querySelector("audio");
        if (audio) {
            // Increase volume by 10% (limit to max of 1)
            audio.volume = Math.min(1, audio.volume + 0.1);
            updateVolumeDisplay(audio.volume);
            speak("Increasing volume...");
        }
    } else if (message.includes("decrease volume")) {
        let audio = document.querySelector("audio");
        if (audio) {
            // Decrease volume by 10% (limit to min of 0)
            audio.volume = Math.max(0, audio.volume - 0.1);
            updateVolumeDisplay(audio.volume);
            speak("Decreasing volume...");
        }
    } 
    else if (message.includes("system check")) {
        // Get number of CPU cores (available in browser)
        const cpuCores = navigator.hardwareConcurrency;
        
        // You can check performance metrics here (e.g., memory load, etc.)
        let performanceMetrics = window.performance.memory ? 
            `Total JS memory usage: ${(window.performance.memory.totalJSHeapSize / 1048576).toFixed(2)} MB` : 
            "Memory metrics not available.";
        
        const systemStatus = `Your system has ${cpuCores} CPU cores. ${performanceMetrics}`;
        speak(systemStatus);
    }else if (message.includes("sing a song")) {
        speak("Here's a song for you!");
        // You can change the lyrics to your choice
        speak("🎶 Ek din bik jayega maati ke mol  Jaag me reh jayenge pyare tere bol,La la lalal la la La la lalla la la, Ek din mar jayega kutte ki maut Jaag me sab kahenge maar gya madarchod 🎶");
    } 
    else{
        let finalText="this is what i found on internet regarding" + message.replace("chhotu","") || message.replace("chhotu","")
        speak(finalText)
        window.open(`https://www.google.com/search?q=${message.replace("chhotu","")}`,"_blank")
    }
}
function updateVolumeDisplay(volume) {
    if (volumeDisplay) {
        // Show the current volume as a percentage (multiplied by 100)
        volumeDisplay.innerText = `Volume: ${(volume * 100).toFixed(0)}%`;
    }
}