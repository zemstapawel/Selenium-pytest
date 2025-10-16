function createVehicle() {
  $("#model2 .js-name").val($("#model1 .js-name").val());
  $("#model2 .js-model").val($("#model1 .js-model").val());
  $("#model2 .js-year").val($("#model1 .js-year").val());
  $("#model2 .js-color").val($("#vehColor").val());
}

$(document).ready(function () {
  $("#cloneVehicle").click(function () {
    createVehicle();
  });
});
