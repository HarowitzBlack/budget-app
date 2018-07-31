
let income_field = document.querySelector(".income-field-box");
let data_submit_btn = document.querySelector(".post-btn");
let action_type_dropdown = document.querySelector("#action-type-dropdown");
let item_top_box_container = document.querySelector(".item-type-box");

function checkIncomeField(e){
  if(income_field.value == ""){
    e.preventDefault();
    alert("Not gonna let thee pass unless thee give me ze amount!")
  }
}

function toggleItemBox(e){
  if(action_type_dropdown.value == "spent"){
    item_top_box_container.style.display = "block";
  }else{
    item_top_box_container.style.display = "None";
  }
}

data_submit_btn.addEventListener("click",checkIncomeField);
action_type_dropdown.addEventListener("click",toggleItemBox)
