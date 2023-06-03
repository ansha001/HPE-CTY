package main

import (
	"encoding/json"
	"html/template"
	"log"
	"net/http"
	"os"
	"sync"
)

type Device struct {
	Vendor string `json:"vender"`
	Model  string `json:"model"`
	SerialNo  string `json:"SerialNo"`
	IP  string `json:"IP"`
	Status  string `json:"Status"`
	}

var (
	jsonDataObj map[string]Device
	mutex       sync.Mutex
)

const tpl = `
<!DOCTYPE html>
<html>
<head>
    <title>Server Info</title>
	<link rel="stylesheet" href="styles.css">

</head>
<body>
    <h2>JSON to HTML Table</h2>
    <table>
        <tr>
            <th>Vendor</th>
            <th>Model</th>
			<th>Serial Number</th>
			<th>ip address</th>
			<th>Status</th>
        </tr>
        {{range $key, $device := .}}
        <tr>
            <td>{{$device.Vendor}}</td>
            <td>{{$device.Model}}</td>
			<td>{{$device.SerialNo}}</td>
			<td>{{$device.IP}}</td>
			<td>{{$device.Status}}</td>
        </tr>
        {{end}}
    </table>
</body>
</html>
`

func indexHandler(w http.ResponseWriter, r *http.Request) {
	t, err := template.New("index").Parse(tpl)
	if err != nil {
		log.Println("Error parsing template:", err)
		return
	}

	mutex.Lock()
	defer mutex.Unlock()

	err = t.Execute(w, jsonDataObj)
	if err != nil {
		log.Println("Error executing template:", err)
		return
	}
}

func main() {
	// Open the JSON file
	file, err := os.Open("data.json")
	if err != nil {
		log.Println("Error opening JSON file:", err)
		return
	}
	defer file.Close()

	// Decode the JSON data
	decoder := json.NewDecoder(file)
	err = decoder.Decode(&jsonDataObj)
	if err != nil {
		log.Println("Error parsing JSON:", err)
		return
	}

	http.HandleFunc("/", indexHandler)

	log.Println("Server listening on http://localhost:8080")
	err = http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal("Error starting server:", err)
	}
}
