// https://webdrawer.net/javascript/geolocation.html#toc9
function getAddress(){
    if( navigator.geolocation ){
        navigator.geolocation.getCurrentPosition(success, error, option);
        function success(position){
            var data = position.coords;
            var lat = data.latitude;
            var lng = data.longitude;
            // console上に出力
            console.log(lat);console.log(lng);
        }
        function error(error){
            var errorMessage = {
                0: "原因不明のエラーが発生しました。",
                1: "位置情報が許可されませんでした。",
                2: "位置情報が取得できませんでした。",
                3: "タイムアウトしました。",
            };
            alert( errorMessage[error.code]);
        }
        var option = {
            "enableHighAccuracy": false,
            "timeout": 100 ,
            "maximumAge": 100 ,
        } ;
    } else {
        alert("あなたの端末では、現在位置を取得できません。");
    }
}
if(false){
    getAddress()
}
const navDetailsElm = document.querySelectorAll(".nav-details");

for (const navDetailsE of navDetailsElm) {
    navDetailsE.querySelector(".nav-summary").addEventListener('click', () => {
        navDetailsE.classList.toggle("open")
        const navDetailsContentsE = navDetailsE.querySelector(".nav-details-contents")
        if(navDetailsE.classList.contains("open")){
            navDetailsContentsE.style.height = navDetailsContentsE.scrollHeight + 'px';
        } else {
            navDetailsContentsE.style.height = 0;
        }
    });
}
