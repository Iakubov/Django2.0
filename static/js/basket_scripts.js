window.onload = function () {
    console.log('DOM LOADED');
    $(".basket-list").on('change',
        'input[type="number"]',
        function (event) {
        // console.log(event.target);
        // console.log(event.target.value);
        // console.log(event.target.name);
        $.ajax({
            url: "/basket/update/" + event.target.name + "/" + event.target.value + "/",
            success: function (data) {
                $('.basket-list').html(data.result);
            }
        })
    })
};