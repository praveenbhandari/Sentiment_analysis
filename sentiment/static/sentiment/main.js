import tableCSV from "./tableCSV.js";

const tableRoot = document.querySelector("#csvRoot");
const csvFileInput = document.querySelector("#csvFileInput");
const tablecsv = new tableCSV(tableRoot); 


csvFileInput.addEventListener("change", e => {
    console.log(csvFileInput.files[0]);

    Papa.parse(csvFileInput.files[0], {
        delimiter: ",",
        skipEmptyLines: true,
        complete: (results) => {
            tablecsv.update(results.data.slice(1), results.data[0]);
        }
    });
});

