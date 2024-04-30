


let model = null;

//Cargar modelo
(async () => {
    console.log("Cargando modelo...");
    model = await tf.loadLayersModel("Data/model.json");
    console.log("Modelo cargado...");
})();

let form = document.getElementById("converter");

function isNotNumber(value){
  return isNaN(value);
}

function ChangeMeters(){
  let meters = document.getElementById("form-label").value;
  if (model != null) {
    if (!isNotNumber(meters) && meters >= 0){
      let tensor = tf.tensor1d([parseInt(meters)]);
      let prediction = model.predict(tensor).dataSync();
       
      document.getElementById("lbl_convertion").textContent = `The conversion from ${meters} meters to yards is: `;

      document.getElementById("lbl_convertion").textContent = "gaaa";
      document.getElementById("label-result").value = prediction;
      
     

    }else{
    document.getElementById("label-result").value = "Type a VALID NUMBER"
    }
  } else {
    document.getElementById("label-result").value = "Try Later Please..";
    //document.getElementById("form-label").value = "";
    
  }
    
}
form.addEventListener("submit", function(event){
    event.preventDefault();
    ChangeMeters();
    
});