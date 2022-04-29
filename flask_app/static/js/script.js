import fetch from 'node-fetch';

/* const response = await fetch('https://www.carboninterface.com/api/v1/estimates', {
    method: 'POST',
    headers: {
        'Authorization': `Bearer ${appKey}`,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        type: "electricity",
        electricity_unit: unit,
        electricity_value: value,
        country: country
    })
}); */

async function getCoderData() {
    let response = await fetch("https://api.github.com/users/adion81");
    // We then need to convert the data into JSON format.
    let coderData = await response.json();
    return coderData;
}
    
console.log(getCoderData());

async function getVehicleInfo(){
    let response = await fetch("https://www.carboninterface.com/api/v1/estimates")

    let vehicleInfo = await response.json();
    return vehicleInfo;
}

// Carbon Interface API key IBLKMnDgx21tRNU1nt1OQg

// Authorization: Token a4329a3b6a117d5c353e71557878193d9caf559b