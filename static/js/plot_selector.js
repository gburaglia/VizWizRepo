$('default_plot').on('change',function(){

    $.ajax({
        url: "/plot_map",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('default_plot').value

        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('map', data );
        }
    });
})
