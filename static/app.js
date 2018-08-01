
/*

 TODO:

 * Select All items
 * Delete All Selected Items
 * Delete single Items

Delete btn function:

The function of the delete btn is to check if any of the checkboxes are
checked.

Put it under a form, then use the preventDefault function to stop the POST
and validate, then just send the required data to /remove endpoint.

*/

let income_field = document.querySelector(".income-field-box");
let data_submit_btn = document.querySelector(".post-btn");
let action_type_dropdown = document.querySelector("#action-type-dropdown");
let item_top_box_container = document.querySelector(".item-type-box");


let allCheckBoxes = document.querySelectorAll('.checkbox-tick');
let selectAllCheckBox_btn = document.querySelector('#select-all-btn');


// delete selected items
let delete_item_btn = document.querySelector("#delete-item-btn");
let delete_item_form = document.querySelector("#delete-item-form");

delete_item_btn.addEventListener("click",deleteSelectedItems);

function deleteSelectedItems(e){
  e.preventDefault();
  let selected_items = [];
  if (allCheckBoxes.length == 0) {
    alert("Select some items to delete!")
  }else{
    for (var i = 0; i < allCheckBoxes.length; i++) {
      if (allCheckBoxes[i].checked) {
        selected_items.push(allCheckBoxes[i].getAttribute("data-item_id"));
      }
    }
    // create a new attr to store the list
    let id_list_attr = document.createAttribute("data-item-list");
    id_list_attr.value = selected_items
    // add the attr to the btn
    delete_item_btn.setAttributeNode(id_list_attr)
    //submit the form
    delete_item_form.submit()
  }

}


// Select and Deselect all checkboxes
let AllCheckBoxesChecked = false
selectAllCheckBox_btn.addEventListener("click",ToggleAllCheckBoxes);

function ToggleAllCheckBoxes(){
  if (!AllCheckBoxesChecked) {
    for (var i = 0; i < allCheckBoxes.length; i++) {
      //console.log(allCheckBoxes[i]);
      allCheckBoxes[i].checked = true;
    }
    AllCheckBoxesChecked = true;
    selectAllCheckBox_btn.innerHTML = "<i class='fas fa-times'></i> Deselect All";
  }else{
    for (var i = 0; i < allCheckBoxes.length; i++) {
      //console.log(allCheckBoxes[i]);
      allCheckBoxes[i].checked = false;
    }
    AllCheckBoxesChecked = false;
    selectAllCheckBox_btn.innerHTML = "<i class='fas fa-check-square'></i> Select All";
  }

}

// Shows the dropdown if the user selects "spent"
// Hides it if "saved" is selected
data_submit_btn.addEventListener("click",checkIncomeField);
action_type_dropdown.addEventListener("click",toggleItemBox);

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
