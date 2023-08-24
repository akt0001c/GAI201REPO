

const inputElement= document.querySelector('input[type="text"]') as HTMLInputElement;
const addButton= document.querySelector('button') as HTMLButtonElement;
const todoList= document.querySelector('ul') as HTMLUListElement;

addButton.addEventListener('click',()=>{
    const inputtext= inputElement.value.trim();
    if(inputtext!='')
    {
        const todoItem= document.createElement("li");
        todoItem.setAttribute('class','flex space-x-4 w-100');
        todoItem.textContent= inputtext;
        const checkbox= document.createElement("input");
        checkbox.type='checkbox';

        checkbox.addEventListener('change',()=>{
            if(checkbox.checked){
                todoItem.classList.add('completed')
            }
            else
             {
                todoItem.classList.remove('completed')
             }
        });
  
        const deleteButton= document.createElement("button");
        deleteButton.textContent='delete';

        deleteButton.addEventListener('click',()=>{
            todoList.removeChild(todoItem);
        });

        todoItem.appendChild(checkbox);
        todoItem.appendChild(deleteButton);

        todoList.appendChild(todoItem);
        inputElement.value="";
        inputElement.focus();   
    }
})
