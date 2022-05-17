String HTML = "<!DOCTYPE html>\
<html>\
<head>\
<title>PID Analyzer</title>\
</head>\
<body>\
<h1> PID Analyzer </h1>\
<p>Please select any Gas Mixture option below</p>\
<input type ='radio' id ='mixture1' name='gas_select' value='mixture1'>\
<label for='mixture1'>oxygen, hydrogen</label><br>\
<input type = 'radio' id ='mixture2' name='gas_select' value='mixture2'>\
<label for = 'mixture2'>Nitrogen, benzene</label><br>\
<input type = 'radio' id ='mixture3' name='gas_select' value='mixture3'>\
<label for='mixture3'>Toluene, hydrogen</label><br>\
<input type = 'radio' id ='mixture4' name='gas_select' value='mixture4'>\
<label for='mixture4'>Oxygen, nitrogen</label><br><br>\
<input type='submit' onclick=onStart() value='START'>\
<p id='demo'></p>\
<script>\
function onStart() {\
  var pageStr = '';\
  if (document.getElementById('mixture1').checked){\
    pageStr = 'mixture1';\
  }\
  else if (document.getElementById('mixture2').checked){\
    pageStr = 'mixture2';\
  }\
  else if (document.getElementById('mixture3').checked){\
    pageStr = 'mixture3';\
  }\
  else if (document.getElementById('mixture4').checked){\
    pageStr = 'mixture4';\
  }\
  window.location.href='/'+pageStr;\
}\
</script>\
</body>\
</html>";
