// Function to fetch and parse JSON data
function fetchData() {
	fetch("data.json") // Assuming the JSON file is named "data.json"
		.then((response) => {
			if (!response.ok) {
				throw new Error("Network response was not ok")
			}
			return response.json()
		})
		.then((data) => {
			// Do something with the JSON data
			console.log(data)
		})
		.catch((error) => {
			console.error("There was a problem with your fetch operation:", error)
		})
}

// Call the function to fetch and parse JSON data
fetchData()
