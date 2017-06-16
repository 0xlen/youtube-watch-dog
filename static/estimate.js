function number_format(number, decimals, dec_point, thousands_sep) {
    var n = number,
    c = isNaN(decimals = Math.abs(decimals)) ? 0 : decimals;
    var d = dec_point == undefined ? "." : dec_point;
    var t = thousands_sep == undefined ? "," : thousands_sep,
    s = n < 0 ? "-" : "";
    var i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "",
    j = (j = i.length) > 3 ? j % 3 : 0;
    return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
}

function calcValue() {
    var views = $("#daily-views").val();
    var minCPM = $('#min-cpm-range-value').val();
    var maxCPM = $('#max-cpm-range-value').val();
    if (minCPM.length == 0) {
        minCPM = 0.25;
        maxCPM = 4.00;
    }
    var tempView = parseFloat(views);
    var tempMinCPM = parseFloat(minCPM);
    var tempMaxCPM = parseFloat(maxCPM);
    if (tempMinCPM >= tempMaxCPM)
        tempMinCPM = tempMaxCPM;
    if (tempMaxCPM <= tempMinCPM)
        tempMinCPM = tempMaxCPM;
    var earningsLow = (tempView / 1000) * tempMinCPM;
    var earningsHigh = (tempView / 1000) * tempMaxCPM;
    $("#user-min-cpm").text(number_format(earningsLow, 2));
    $("#user-max-cpm").text(number_format(earningsHigh, 2));
    $("#user-min-cpm-monthly").text(number_format((earningsLow * 30), 2));
    $("#user-max-cpm-monthly").text(number_format((earningsHigh * 30), 2));
    $("#user-min-cpm-yearly").text(number_format((earningsLow * 30 * 12), 2));
    $("#user-max-cpm-yearly").text(number_format((earningsHigh * 30 * 12), 2));
}
