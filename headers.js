const ApiKey = 'mx0vglo09a68ctj7tf';
const ApiSec = '0d7038e59c2a431784e9c9ee534751ec';
const stemp = new Date().getTime().toString()
const method = 'POST';


let objectString = ApiKey + stemp
console.log(objectString)
let params = {}
if (method === 'POST') {
    objectString += pm.request.body.raw;
} else {
    params = pm.request.url.query;

    // objectString += params.map((key) => {
    //     console.log(`key->`,!!params[key] == true );

    //     return !key.disabled ? `${key}=${encodeURIComponent(params[key])}`:'';
    // }).join('&');

    // for(var i in params){
    //      console.log( params[i].key+params[i].value);
    //      console.log(params[i].value != '');

    // }

    objectString += params;
}

console.log(`objectString: ${objectString}`);



const sign = CryptoJS.enc.Hex.stringify(CryptoJS.HmacSHA256(objectString, ApiSec))

console.log(`Request-Time: ${stemp}`)
console.log(`ApiKey: ${ApiKey}`)
console.log(`Content-Type: application/json`)
console.log(objectString)
console.log(`Signature: ${sign}`)
pm.request.headers.add({
    key: 'Request-Time',
    value: stemp
});

pm.request.headers.add({
    key: 'ApiKey',
    value: ApiKey
});

pm.request.headers.add({
    key: 'Content-Type',
    value: 'application/json'
});

pm.request.headers.add({
    key: 'Signature',
    value: sign
});
