function parseDate(remark) {
    var regex = /year(\d{4}).*?month(\d{1,2}).*?day(\d{1,2})/i;
    var match = regex.exec(remark);
    console.log(match);
    if (match !== null) {
        var year = match[1];
        var month = match[2];
        var day = match[3];
        return "".concat(year, "-").concat(month, "-").concat(day);
    }
    else {
        return 'Date cannot be found';
    }
}
var remark = "HGI_YEAR2019testmonth12DATE12ABU1234DAY23";
var date = parseDate(remark);
console.log(date);