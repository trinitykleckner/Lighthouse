//chatGPT webhook running as a webapp from a google appscript (so code is just here to show it)
function doPost(e) {
  var requestContent = JSON.parse(e.postData.contents);

  const task = requestContent["task"]
  const content = requestContent["text"];
  const language = requestContent["language"];

  // task = "list"
  // content = "can you make some suggestions about where an immigrant could find food while new to the US"
  // language = "english"

  var ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();  
  ss.getRange("A1:A3").clear();
  ss.getRange("A1").setValue(content);

  if (task == "translate"){
    ss.getRange("A2").setValue('=GPT_TRANSLATE(A1,"'+language+'")');
  } else if (task == "list"){
    ss.getRange("B2").setValue('=CONCAT("Please answer in '+language+'",A1)')
    ss.getRange("A2").setValue('=GPT_LIST(B2)');
  } else {
    ss.getRange("B2").setValue('=CONCAT("Please answer in '+language+'",A1)')
    ss.getRange("A2").setValue('=GPT(B2)');
  }
  var translated = ss.getRange(2,1,ss.getLastRow()-1,1).getValues();
  // var translated = ss.getRange("A2").getValue();

  output = {}
  output["translated"] = translated
  Logger.log(translated)
  var params = JSON.stringify(output);

  return ContentService.createTextOutput(params)
}
