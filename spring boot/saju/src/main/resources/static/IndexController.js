document.getElementById("sendbtn").addEventListener("click", function (event) {
    event.preventDefault();
    const name = document.getElementById("mNA").value;
    const birthyear = document.getElementById("mYY").value;
    const birthmonth = document.getElementById("mMM").value;
    const birthday = document.getElementById("mDD").value;
    const birthtime = document.getElementById("mHH").value;
    const gender = document.getElementById("mSE").value;
    const month = document.getElementById("mSL").value;

    const Data = {
        Name: name,
        BirthYear: birthyear,
        BirthMonth: birthmonth,
        BirthDay: birthday,
        BirthTime: birthtime,
        isMale: gender,
        Calendar: month
    };

    sendDataToServer(Data);
});

function sendDataToServer(Data) {
    fetch('http://127.0.0.1:5000/send-json', {
        method: 'POST',
        body: JSON.stringify(Data),
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
         sessionStorage.setItem('resultData', JSON.stringify(data));

         // 새로운 페이지로 이동
         window.location.href = 'result';
    })
    .catch(error => {
        console.error('오류 발생:', error);
    });
}