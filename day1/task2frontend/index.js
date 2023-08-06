const baseurl= `http://localhost:8888/main/chat`;
let zenbtn= document.querySelector("#zoke-btn");
zenbtn.onclick=()=>{
    console.log("working");
   let input= document.querySelector("#input-box").value;
   let prompt= `zenerate zoke for ${input}`;
   let  newurl= baseurl +`?prompt=${prompt}`;
   zenerate(newurl);
};

let zenerate= (url)=>{
    fetch(url,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        }
    })
      .then(response=>response.json())
      .then(data=>display(data.choices))
      .catch(error=>console.log(error));
};

const display= (data)=>{
    let box= document.querySelector("#output-box");
    box.innerHTML="";

    data.forEach((ele) => {
        let content= ele.message.content;
        let line= document.createElement("p");
        line.setAttribute("class","main_content");
        line.textContent=content;
        box.append(line);
    });

};