alert("test");

document.getElementById("sendbtn").addEventListener("click", function (event) {
    event.preventDefault();
    alert(document.getElementById("mNA"));
    const name = document.getElementById("mNA").value;
    const birthyear = document.getElementById("mYY").value;
    const birthmonth = document.getElementById("mMM").value;
    const birthday = document.getElementById("mDD").value;
    const birthtime = document.getElementById("mHH").value;
    const gender = document.getElementById("mSE").value;
    const month = document.getElementById("mSL").value;

    const Data={
        sajuname : mNA,
        sajubirthyear : mYY,
        sajubirthmonth : mMM,
        sajubirthday : mDD,
        sajubirthtime : mHH,
        sajugender : mSE,
        sajumonth : mSL
    }
    sendDataToServer(Data);
});

function sendDataToServer(Data)
{
    fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        body: JSON.stringify(Data),
        headers: {
            'Content-Type': 'application/json',
        },
        mode : 'no-cors',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = JSON.stringify(data, null, 6);
    });
}

