// implementation of Carbon Interface API request
const response = await fetch('https://www.carboninterface.com/api/v1/estimates', {
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
});