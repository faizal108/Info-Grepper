function run() {

  document.getElementById("tool-output").style.cssText = "display: block;"
  const input_value = document.getElementById("search-input").value;

  const output = "helloo,myname, is faizal, kadiwal.";
  const table = document.getElementById("output-table");
  const tableHeader = table.createTHead();
  const tableRow = tableHeader.insertRow();
  const headers = ["Links"]; // Replace with actual column headers
  headers.forEach((header) => {
    const th = document.createElement("th");
    th.appendChild(document.createTextNode(header));
    tableRow.appendChild(th);
  });
  const tableBody = table.createTBody();
  const rows = output.split(","); // Replace delimiter with actual delimiter used in output
  rows.forEach((row) => {
    const tableRow = tableBody.insertRow();
    const cells = row.split(","); // Replace delimiter with actual delimiter used in output
    cells.forEach((cell) => {
      const td = document.createElement("td");
      td.appendChild(document.createTextNode(cell));
      tableRow.appendChild(td);
    });
  });

  document.getElementById("web-url").href = input_value;
  document.getElementById("web-url").innerHTML = input_value;
}
