String HTML = "<!DOCTYPE html>\
<html>\
<head>\
<title>PID Analyzer</title>\
</head>\
<body>\
<h1> PID Analyzer </h1>\
<p>Please select any Gas Mixture option below</p>\
<input type ='radio' id ='mixture1' name='gas_select' value='mixture1'>\
<label for='mixture1'>vinyl chloride,Toluene</label><br>\
<input type = 'radio' id ='mixture2' name='gas_select' value='mixture2'>\
<label for = 'mixture2'>methylene chloride,Perchloroethylene</label><br>\
<input type = 'radio' id ='mixture3' name='gas_select' value='mixture3'>\
<label for='mixture3'>3 chloro propene,Chlorobenzene</label><br>\
<input type = 'radio' id ='mixture4' name='gas_select' value='mixture4'>\
<label for='mixture4'>Benzene, 1,2,4 trichloro benzene</label><br>\
<input type = 'radio' id ='mixture5' name='gas_select' value='mixture5'>\
<label for='mixture5'>vinyl chloride,cis 1,3 dichloropropene,Toluene</label><br>\
<input type = 'radio' id ='mixture6' name='gas_select' value='mixture6'>\
<label for = 'mixture6'>methylene chloride,trans 1,3 dichloropropene,Perchloroethylene</label><br>\
<input type = 'radio' id ='mixture7' name='gas_select' value='mixture7'>\
<label for='mixture7'>3 chloro propene,Toluene,Chlorobenzene</label><br><br>\
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
  else if (document.getElementById('mixture5').checked){\
    pageStr = 'mixture5';\
  }\
  else if (document.getElementById('mixture6').checked){\
    pageStr = 'mixture6';\
  }\
  else if (document.getElementById('mixture7').checked){\
    pageStr = 'mixture7';\
  }\
  window.location.href='/'+pageStr;\
}\
</script>\
</body>\
</html>";
