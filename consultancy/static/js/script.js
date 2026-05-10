function showMessage() {
    alert("Consultation booking feature coming soon!");
}

document.addEventListener("DOMContentLoaded", () => {

    const counters = document.querySelectorAll('.counter');

    counters.forEach(counter => {

        const target = parseInt(counter.getAttribute('data-target'));

        let count = 0;

        const speed = target / 50;

        const updateCounter = () => {

            if(count < target){

                count += speed;

                counter.innerText = Math.floor(count);

                setTimeout(updateCounter, 30);

            } else {

                counter.innerText = target + "+";
            }
        };

        updateCounter();

    });

});

// ===== AI CHATBOT =====

function toggleAIChat(){

    const chatBox = document.getElementById("aiChatBox");

    if(chatBox.style.display === "flex"){

        chatBox.style.display = "none";

    } else {

        chatBox.style.display = "flex";
    }
}

function handleKey(event){

    if(event.key === "Enter"){

        sendAIMessage();
    }
}

function sendAIMessage() {

    const input = document.getElementById("aiUserInput");
    const chatBody = document.getElementById("aiChatBody");

    const message = input.value.trim();

    if(message === "") return;

    // USER MESSAGE

    const userMsg = document.createElement("div");

    userMsg.classList.add("ai-user-message");

    userMsg.innerText = message;

    chatBody.appendChild(userMsg);

    // BOT MESSAGE

    const botMsg = document.createElement("div");

    botMsg.classList.add("ai-bot-message");

    let reply = "";

    const lowerMsg = message.toLowerCase();

    // GST

    if(lowerMsg.includes("gst")){

        reply =
        "We provide GST Registration, GST Filing, GST Return Filing, GST Notices handling and Compliance services.";

    }

    // INCOME TAX FILING

    else if(
        lowerMsg.includes("income tax filing") ||
        lowerMsg.includes("itr filing") ||
        lowerMsg.includes("file tax")
    ){

        reply =
        "Income Tax Filing includes preparing and submitting your tax return to the Income Tax Department. We help individuals, salaried employees and businesses file returns accurately and on time.";

    }

    // TAX SAVING

    else if(
        lowerMsg.includes("tax saving")
    ){

        reply =
        "We help clients reduce tax legally through deductions, investments and smart tax planning strategies.";

    }

    // TDS / TCS

    else if(
        lowerMsg.includes("tds") ||
        lowerMsg.includes("tcs")
    ){

        reply =
        "We provide E-TDS/TCS filing, corrections, notices handling and compliance support.";

    }

    // COMPANY REGISTRATION

    else if(
        lowerMsg.includes("company registration") ||
        lowerMsg.includes("startup registration") ||
        lowerMsg.includes("llp")
    ){

        reply =
        "We assist with Company Formation, LLP Registration, Startup Registration and ROC Compliance.";

    }

    // LICENSES

    else if(
        lowerMsg.includes("fssai") ||
        lowerMsg.includes("trade license") ||
        lowerMsg.includes("license")
    ){

        reply =
        "We help obtain FSSAI, Trade, Fire, Hostel, Drug and other business licenses.";

    }

    // CONTACT

    else if(
        lowerMsg.includes("contact") ||
        lowerMsg.includes("phone") ||
        lowerMsg.includes("email")
    ){

        reply =
        "📞 Phone: +91 9566956176\n📧 Email: nexgentax2025@gmail.com";

    }

    // PRICE

    else if(
        lowerMsg.includes("price") ||
        lowerMsg.includes("fees") ||
        lowerMsg.includes("cost")
    ){

        reply =
        "Pricing depends on the service required. Please tell us your requirement for an exact quotation.";

    }

    // HELLO

    else if(
        lowerMsg.includes("hello") ||
        lowerMsg.includes("hi") ||
        lowerMsg.includes("hey")
    ){

        reply =
        "Hello 👋 Welcome to NexGen Tax Consultancy. How can we help you today?";

    }

    // GENERAL TAX

    else if(
        lowerMsg.includes("income tax") ||
        lowerMsg.includes("tax")
    ){

        reply =
        "We provide Income Tax Filing, Tax Planning, Notices handling, Business Tax Consultancy and TDS/TCS services.";

    }
    else if(message.includes("none")){

    reply = "Please contact our support team directly at 📧 nexgentax2025@gmail.com or call 📞 +91 9566956176 We will assist you personally.";
}

    // DEFAULT

    else{

        reply =
        "Sorry, I could not fully understand your query. Please contact NexGen Tax Consultancy for detailed assistance.\n\n📞 +91 9566956176\n📧 nexgentax2025@gmail.com";
    }

    // APPEND BOT MESSAGE

    chatBody.appendChild(botMsg);

    // TYPING EFFECT

    let index = 0;

    const typing = setInterval(() => {

        botMsg.innerText = reply.slice(0, index);

        index++;

        if(index > reply.length){

            clearInterval(typing);

            chatBody.scrollTop = chatBody.scrollHeight;
        }

    }, 20);

    // CLEAR INPUT

    input.value = "";
}



// QUICK QUESTION BUTTONS

function quickMessage(text){

    document.getElementById("aiUserInput").value = text;

    sendAIMessage();
}



// ENTER KEY SUPPORT

document.getElementById("aiUserInput").addEventListener("keypress", function(e){

    if(e.key === "Enter"){

        sendAIMessage();
    }

});



// CHAT OPEN/CLOSE

function toggleAIChat(){

    const chatbot = document.getElementById("aiChatContainer");

    chatbot.classList.toggle("show-chat");

}
let index = 0;

function slideTestimonials() {
    const track = document.getElementById("sliderTrack");
    const cards = document.querySelectorAll(".testimonial-card");

    index++;

    if (index >= cards.length) {
        index = 0;
    }

    track.style.transform = `translateX(-${index * 100}%)`;
}

// 2 seconds auto slide
setInterval(slideTestimonials, 2000);