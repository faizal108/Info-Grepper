function run() {

  document.getElementById("tool-output").style.cssText = "display: block;"
  const input_value = document.getElementById("search-input").value;
  document.getElementById("web-url").href = input_value;
  document.getElementById("web-url").innerHTML = input_value;
}
