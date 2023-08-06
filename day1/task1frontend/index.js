let sendBtn= document.querySelector("#send-btn");


sendBtn.onclick=(event)=>{
    const prompt= document.querySelector("#input-bar").value;
    const url= `http://localhost:8888/main/chat?prompt=${prompt}`;
 sendChat(url);

};

const sendChat= (url)=>{
    
    fetch(url,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
       
    })
     .then((response)=>response.json())
     .then((data)=>display(data.choices))
     .catch((error)=>console.log(error));
};


const display= (data)=>{
    const chatBox= document.querySelector("#display-box");
    chatBox.innerHTML="";

    data.forEach(ele => {
        let message= ele.message;
        let role= message.role;
        let content=message.content;
        let div= document.createElement("div");
        div.innerHTML=`As a <h6>${role} :</h6> <p>${content}</p>`;
        chatBox.append(div);
    });

};

